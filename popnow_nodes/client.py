"""A small asynchronous PopNow API client built on aiohttp, which ComfyUI already ships.

It covers only what the nodes need: the model catalog, quotes, task creation and polling,
uploads, LoRA imports and downloads. It follows the same contract as the official Python SDK
(https://github.com/popnow-ai/popnow-python); the SDK is not a dependency because a custom node
that installs nothing is one that cannot break somebody's ComfyUI environment.
"""

from __future__ import annotations

import asyncio
import json
import os
import random
import urllib.parse
from collections.abc import Awaitable, Callable, Mapping
from typing import Any

import aiohttp

from . import VERSION

# The API rejects anonymous default client User-Agents, so every request names this package.
USER_AGENT = f"popnow-comfyui/{VERSION} (+https://github.com/popnow-ai/popnow-comfyui)"
REQUEST_TIMEOUT_SECONDS = 30.0
UPLOAD_TIMEOUT_SECONDS = 600.0
LORA_UPLOAD_TIMEOUT_SECONDS = 7200.0
IMPORT_TIMEOUT_SECONDS = 900.0
DOWNLOAD_TIMEOUT_SECONDS = 900.0
MAX_JSON_BYTES = 32 * 1024 * 1024
MAX_DOWNLOAD_BYTES = 2 * 1024 * 1024 * 1024

RETRYABLE_HTTP = frozenset({408, 429, 500, 502, 503, 504})
RETRYABLE_CODES = frozenset({429, 500, 503, 50301})
# 50302 rides on a 503 but resending under the same Idempotency-Key only replays the recorded
# failure, so it is checked before the status code.
NON_RETRYABLE_CODES = frozenset({50302})
MAX_RETRIES = 3

TERMINAL_STATES = frozenset({"succeeded", "failed", "canceled", "expired"})
ACTIVE_STATES = frozenset({"queued", "running"})

# What to do about a business code. Branch on the code, never on the message: messages follow
# the account's API error language, codes never change.
RECOVERY_BY_CODE: Mapping[int, str] = {
    40003: "The uploaded file did not match its upload ticket. Run the node again to re-upload it.",
    40004: (
        "The model cannot serve this combination of settings right now. Change the setting named "
        "in the message, or pick another model."
    ),
    40201: "Not enough credits for this run. Buy credits at https://popnow.ai/pricing, then run it again.",
    40202: "This key reached its spend cap. Raise the cap in the API console, or wait for it to reset.",
    40301: "This key may not call this model. Add the model to the key's allowed list in the API console.",
    40302: "This request came from an address outside the key's IP allow-list.",
    40310: (
        "Your PopNow account has not verified its email address yet. Open the verification link "
        "sent at sign-up, then run the node again."
    ),
    40901: "The price changed before the task was created. Run the node again to accept the new price.",
    50301: "This model cannot take tasks right now. Try again later or pick another model.",
    50302: "The generation failed and was refunded. Run the node again.",
}

InterruptCheck = Callable[[], None]


class PopNowApiError(RuntimeError):
    """An HTTP, envelope or network failure, with the fields support asks for."""

    def __init__(
        self,
        message: str,
        *,
        status: int = 0,
        code: int | None = None,
        request_id: str = "",
        retry_after: float | None = None,
    ) -> None:
        super().__init__(message)
        self.status = status
        self.code = code
        self.request_id = request_id
        self.retry_after = retry_after

    @property
    def recovery(self) -> str:
        return RECOVERY_BY_CODE.get(self.code or 0, "")

    def __str__(self) -> str:
        parts = [super().__str__()]
        if self.code:
            parts[0] = f"PopNow {self.code}: {parts[0]}"
        if self.recovery:
            parts.append(self.recovery)
        if self.request_id:
            parts.append(f"(request_id {self.request_id})")
        return " ".join(parts)


class PopNowTaskFailed(RuntimeError):
    """The task reached a terminal state other than succeeded."""

    def __init__(self, task: Mapping[str, Any]) -> None:
        self.task = dict(task)
        state = task.get("state")
        code = task.get("errorCode") or state
        message = task.get("errorMessage") or f"the task ended as {state}"
        hint = " Failed runs are refunded."
        if code == "content_rejected":
            hint = " The model declined this request. Unless the model page says refusals are billed, nothing was charged."
        super().__init__(f"PopNow {code}: {message}{hint} (task {task.get('taskId')})")


def _parse_retry_after(value: str | None) -> float | None:
    if not value:
        return None
    try:
        return max(0.0, float(value))
    except ValueError:
        return None


def _retry_delay(attempt: int, retry_after: float | None) -> float:
    exponential = min(0.5 * (2**attempt), 8.0) * (0.8 + random.random() * 0.4)
    return max(exponential, retry_after or 0.0)


async def _read_capped(response: aiohttp.ClientResponse, limit: int) -> bytes:
    chunks: list[bytes] = []
    total = 0
    async for chunk in response.content.iter_chunked(256 * 1024):
        total += len(chunk)
        if total > limit:
            raise PopNowApiError(f"response body exceeded the local limit of {limit} bytes")
        chunks.append(chunk)
    return b"".join(chunks)


async def interruptible_sleep(seconds: float, check: InterruptCheck | None) -> None:
    """Sleep in short slices so a cancel in ComfyUI takes effect within half a second."""
    remaining = max(0.0, seconds)
    while remaining > 0:
        if check is not None:
            check()
        step = min(0.5, remaining)
        await asyncio.sleep(step)
        remaining -= step
    if check is not None:
        check()


class PopNowClient:
    def __init__(
        self,
        api_key: str,
        base_url: str,
        *,
        interrupt_check: InterruptCheck | None = None,
    ) -> None:
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.interrupt_check = interrupt_check
        self._session: aiohttp.ClientSession | None = None

    async def __aenter__(self) -> PopNowClient:
        return self

    async def __aexit__(self, *_: Any) -> None:
        await self.close()

    async def close(self) -> None:
        if self._session is not None and not self._session.closed:
            await self._session.close()
        self._session = None

    def _session_or_new(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            # trust_env makes HTTPS_PROXY and friends work, which is how many people behind a
            # corporate or regional proxy reach the API at all.
            self._session = aiohttp.ClientSession(trust_env=True, headers={"User-Agent": USER_AGENT})
        return self._session

    def _auth_headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.api_key}", "Accept": "application/json"}

    # -- Envelope requests ------------------------------------------------

    async def request(
        self,
        method: str,
        path: str,
        *,
        body: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        timeout: float = REQUEST_TIMEOUT_SECONDS,
        retryable: bool = True,
    ) -> Any:
        """Call an endpoint that answers with the ``{code, msg, data, request_id}`` envelope."""
        session = self._session_or_new()
        request_headers = self._auth_headers()
        request_headers.update(headers or {})
        payload = None
        if body is not None:
            payload = json.dumps(body, separators=(",", ":")).encode()
            request_headers["Content-Type"] = "application/json"

        for attempt in range(MAX_RETRIES + 1):
            if self.interrupt_check is not None:
                self.interrupt_check()
            try:
                async with session.request(
                    method,
                    f"{self.base_url}{path}",
                    data=payload,
                    headers=request_headers,
                    timeout=aiohttp.ClientTimeout(total=timeout),
                ) as response:
                    status = response.status
                    retry_after = _parse_retry_after(response.headers.get("Retry-After"))
                    raw = await _read_capped(response, MAX_JSON_BYTES)
            except (aiohttp.ClientError, asyncio.TimeoutError) as error:
                if retryable and attempt < MAX_RETRIES:
                    await interruptible_sleep(_retry_delay(attempt, None), self.interrupt_check)
                    continue
                raise PopNowApiError(f"network request to PopNow failed: {error!r}") from error

            try:
                envelope = json.loads(raw)
            except (ValueError, UnicodeDecodeError) as error:
                if retryable and attempt < MAX_RETRIES and status in RETRYABLE_HTTP:
                    await interruptible_sleep(_retry_delay(attempt, retry_after), self.interrupt_check)
                    continue
                raise PopNowApiError(
                    f"PopNow answered HTTP {status} with a body that is not JSON; a proxy or "
                    "firewall between ComfyUI and api.popnow.ai may be intercepting the request",
                    status=status,
                ) from error

            envelope = envelope if isinstance(envelope, dict) else {}
            code = envelope.get("code")
            failed = not 200 <= status < 300 or code != 200
            resend_helps = code not in NON_RETRYABLE_CODES and (status in RETRYABLE_HTTP or code in RETRYABLE_CODES)
            if failed and retryable and resend_helps and attempt < MAX_RETRIES:
                await interruptible_sleep(_retry_delay(attempt, retry_after), self.interrupt_check)
                continue
            if failed:
                message = envelope.get("msg")
                raise PopNowApiError(
                    message if isinstance(message, str) and message else f"request failed with HTTP {status}",
                    status=status,
                    code=code if isinstance(code, int) else None,
                    request_id=str(envelope.get("request_id") or ""),
                    retry_after=retry_after,
                )
            if "data" not in envelope:
                raise PopNowApiError("successful response omitted data", status=status)
            return envelope["data"]
        raise AssertionError("retry loop exited unexpectedly")

    # -- Catalog and account ----------------------------------------------

    async def list_models(self) -> list[dict[str, Any]]:
        """Every image, video and audio model this key can call, with input schemas and credit prices."""
        data = await self.request("GET", "/api/v1/models?includeSchema=1", timeout=30)
        items = data.get("items") if isinstance(data, dict) else None
        return [item for item in items or [] if isinstance(item, dict)]

    async def balance(self) -> dict[str, Any]:
        return await self.request("GET", "/api/v1/chat/credit")

    # -- Tasks ------------------------------------------------------------

    async def quote(self, model: str, input_data: Mapping[str, Any]) -> dict[str, Any]:
        return await self.request("POST", "/api/v1/jobs/quote", body={"model": model, "input": dict(input_data)})

    async def create_task(
        self,
        model: str,
        input_data: Mapping[str, Any],
        *,
        idempotency_key: str,
        quote_id: str | None = None,
        expected_credits: int | None = None,
    ) -> dict[str, Any]:
        """Submit one task. Every resend of this submission must reuse the same key."""
        body: dict[str, Any] = {"model": model, "input": dict(input_data)}
        if quote_id:
            body["quoteId"] = quote_id
        if expected_credits is not None:
            body["expectedCredits"] = int(expected_credits)
        return await self.request(
            "POST",
            "/api/v1/jobs/createTask",
            body=body,
            headers={"Idempotency-Key": idempotency_key},
        )

    async def get_task(self, task_id: str) -> dict[str, Any]:
        query = urllib.parse.urlencode({"taskId": task_id})
        return await self.request("GET", f"/api/v1/jobs/recordInfo?{query}")

    async def wait_for_task(
        self,
        task_id: str,
        *,
        timeout_seconds: float,
        on_poll: Callable[[dict[str, Any], float], Awaitable[None] | None] | None = None,
    ) -> dict[str, Any]:
        """Poll until the task is terminal and every output file has a URL."""
        loop = asyncio.get_running_loop()
        started = loop.time()
        interval = 2.0
        while True:
            elapsed = loop.time() - started
            if elapsed > timeout_seconds:
                raise PopNowApiError(
                    f"task {task_id} did not finish within {int(timeout_seconds)} seconds; it may "
                    "still be running on PopNow. Check it in the API console under Logs."
                )
            try:
                task = await self.get_task(task_id)
            except PopNowApiError as error:
                # One failed poll is not a failed task: keep polling while the budget lasts.
                if error.status and error.status < 500 and error.status not in (408, 429):
                    raise
                task = None
            if task is not None:
                if on_poll is not None:
                    result = on_poll(task, elapsed)
                    if asyncio.iscoroutine(result):
                        await result
                state = task.get("state")
                if state in TERMINAL_STATES and not _has_pending_assets(task):
                    return task
                if state not in TERMINAL_STATES and state not in ACTIVE_STATES:
                    raise PopNowApiError(f"unknown task state {state!r} for task {task_id}")
            await interruptible_sleep(interval, self.interrupt_check)
            interval = min(interval * 1.5, 10.0)

    # -- Files ------------------------------------------------------------

    async def upload(self, data: bytes, content_type: str) -> str:
        """Ticket, PUT and commit. Returns the ``popnow://f/...`` URI that goes into task input."""
        return await self._upload(data, len(data), content_type, UPLOAD_TIMEOUT_SECONDS)

    async def upload_file(self, path: str, content_type: str) -> str:
        """Same as ``upload`` for a file on disk, streamed so a 2 GiB LoRA never sits in memory."""
        size = os.path.getsize(path)
        with open(path, "rb") as handle:
            return await self._upload(handle, size, content_type, LORA_UPLOAD_TIMEOUT_SECONDS)

    async def _upload(self, data: Any, size: int, content_type: str, timeout: float) -> str:
        # The ticket is never retried: each one is a signed write authorization, and a second
        # ticket does not make the first one usable.
        ticket = await self.request(
            "POST",
            "/api/v1/common/upload-url",
            body={"contentType": content_type, "bytes": size},
            retryable=False,
        )
        max_bytes = ticket.get("maxBytes")
        if isinstance(max_bytes, int) and size > max_bytes:
            raise PopNowApiError(f"the file is {size} bytes but this upload accepts at most {max_bytes}")
        session = self._session_or_new()
        # Every ticket header goes out exactly as received: Content-Type and Content-Length are
        # both part of the signature. No Authorization header, the URL is its own credential.
        put_headers = {str(k): str(v) for k, v in (ticket.get("headers") or {}).items()}
        put_headers.setdefault("Content-Length", str(size))
        try:
            async with session.request(
                str(ticket.get("method") or "PUT"),
                str(ticket["uploadUrl"]),
                data=data,
                headers=put_headers,
                skip_auto_headers=("Content-Type",),
                timeout=aiohttp.ClientTimeout(total=timeout),
            ) as response:
                status = response.status
                await response.read()
        except (aiohttp.ClientError, asyncio.TimeoutError) as error:
            raise PopNowApiError(f"uploading the file failed: {error!r}") from error
        if not 200 <= status < 300:
            raise PopNowApiError(f"uploading the file failed with HTTP {status}", status=status)
        file_id = urllib.parse.quote(str(ticket["fileId"]), safe="")
        committed = await self.request("POST", f"/api/v1/files/{file_id}/commit")
        return _uri_of(committed)

    async def import_lora(self, url: str, token: str = "") -> str:
        """Have PopNow download a ``.safetensors`` LoRA once; returns its ``popnow://f/...`` URI.

        ``url`` is a Hugging Face repo id (``owner/repo``), a Hugging Face or Civitai page, or a
        direct https link. ``token`` is used for this one download only and never stored.
        """
        body: dict[str, Any] = {"url": url}
        if token:
            body["token"] = token
        # Not retried automatically: a second import of a large file is a second download.
        committed = await self.request("POST", "/api/v1/files/import", body=body, timeout=IMPORT_TIMEOUT_SECONDS, retryable=False)
        return _uri_of(committed)

    async def download(self, url: str, *, max_bytes: int = MAX_DOWNLOAD_BYTES) -> bytes:
        """Fetch an output file. The signed URL is the credential; no API key is attached."""
        session = self._session_or_new()
        last_error: Exception | None = None
        for attempt in range(MAX_RETRIES + 1):
            if self.interrupt_check is not None:
                self.interrupt_check()
            try:
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=DOWNLOAD_TIMEOUT_SECONDS)) as response:
                    if response.status in RETRYABLE_HTTP and attempt < MAX_RETRIES:
                        last_error = PopNowApiError(f"HTTP {response.status}", status=response.status)
                    elif not 200 <= response.status < 300:
                        raise PopNowApiError(
                            f"downloading the result failed with HTTP {response.status}",
                            status=response.status,
                        )
                    else:
                        return await _read_capped(response, max_bytes)
            except (aiohttp.ClientError, asyncio.TimeoutError) as error:
                last_error = error
            if attempt < MAX_RETRIES:
                await interruptible_sleep(_retry_delay(attempt, None), self.interrupt_check)
        raise PopNowApiError(f"downloading the result failed: {last_error!r}")


def _uri_of(committed: Any) -> str:
    uri = committed.get("uri") if isinstance(committed, dict) else None
    if not isinstance(uri, str) or not uri:
        raise PopNowApiError("the file was stored but no popnow:// URI came back")
    return uri


def _has_pending_assets(task: Mapping[str, Any]) -> bool:
    """A succeeded task can still have output files that have not landed yet."""
    if task.get("state") != "succeeded":
        return False
    return any(
        isinstance(asset, Mapping) and asset.get("pending") and not asset.get("unavailable") for asset in output_assets(task)
    )


def output_assets(task: Mapping[str, Any]) -> list[dict[str, Any]]:
    output = task.get("output")
    if not isinstance(output, Mapping):
        return []
    assets = output.get("assets")
    if not isinstance(assets, list):
        return []
    return [dict(asset) for asset in assets if isinstance(asset, Mapping)]


def output_text(task: Mapping[str, Any]) -> str | None:
    output = task.get("output")
    if not isinstance(output, Mapping):
        return None
    text = output.get("text")
    return text if isinstance(text, str) else None
