"""A local fake of the PopNow API for the tests, built on aiohttp's test server."""

from __future__ import annotations

import os
from typing import Any

from aiohttp import web
from aiohttp.test_utils import TestServer


def envelope(data: Any, code: int = 200, status: int = 200, **headers: str) -> web.Response:
    body = {"code": code, "msg": "success" if code == 200 else f"failed {code}", "request_id": "req_test"}
    if data is not None:
        body["data"] = data
    return web.json_response(body, status=status, headers=headers)


class FakePopNow:
    """Records every call; tests tweak ``self.behaviour`` to change what it answers."""

    def __init__(self) -> None:
        self.calls: dict[str, int] = {}
        self.bodies: dict[str, list[Any]] = {}
        self.headers: dict[str, list[dict[str, str]]] = {}
        self.behaviour: dict[str, Any] = {}
        self.app = web.Application()
        router = self.app.router
        router.add_get("/api/v1/models", self.models)
        router.add_get("/api/v1/chat/credit", self.credit)
        router.add_post("/api/v1/jobs/quote", self.quote)
        router.add_post("/api/v1/jobs/createTask", self.create)
        router.add_get("/api/v1/jobs/recordInfo", self.record)
        router.add_post("/api/v1/common/upload-url", self.ticket)
        router.add_put("/storage/object", self.put)
        router.add_post("/api/v1/files/{file_id}/commit", self.commit)
        router.add_post("/api/v1/files/import", self.import_file)
        router.add_get("/files/result.bin", self.result_file)
        self.server = TestServer(self.app)
        self._saved_env: dict[str, str | None] = {}

    async def start(self) -> str:
        # The client honours HTTP(S)_PROXY like any aiohttp client; the fake server is local.
        for name in ("NO_PROXY", "no_proxy"):
            self._saved_env[name] = os.environ.get(name)
            os.environ[name] = "127.0.0.1,localhost"
        await self.server.start_server()
        self.base = str(self.server.make_url("")).rstrip("/")
        return self.base

    async def close(self) -> None:
        await self.server.close()
        for name, value in self._saved_env.items():
            if value is None:
                os.environ.pop(name, None)
            else:
                os.environ[name] = value

    def _note(self, name: str, request: web.Request, body: Any = None) -> int:
        self.calls[name] = self.calls.get(name, 0) + 1
        self.bodies.setdefault(name, []).append(body)
        self.headers.setdefault(name, []).append(dict(request.headers))
        return self.calls[name]

    async def models(self, request: web.Request) -> web.Response:
        n = self._note("models", request)
        if n == 1 and self.behaviour.get("models_503_first"):
            return envelope(None, code=503, status=503, **{"Retry-After": "0"})
        return envelope({"items": self.behaviour.get("models", [{"model": "a/b/c", "inputSchema": {}}]), "total": 1})

    async def credit(self, request: web.Request) -> web.Response:
        self._note("credit", request)
        return envelope(
            {"available": "1.00", "held": "0", "total": "1.00", "availableCredits": 100, "heldCredits": 0, "totalCredits": 100}
        )

    async def quote(self, request: web.Request) -> web.Response:
        body = await request.json()
        self._note("quote", request, body)
        credits = self.behaviour.get("quote_credits", 8)
        return envelope(
            {
                "quoteId": f"q_{self.calls['quote']}",
                "model": body["model"],
                "estimatedCost": f"{credits / 100:.2f}",
                "maxCharge": f"{credits / 100:.2f}",
                "maxCredits": credits,
                "expectedCredits": credits,
                "currency": "USD",
                "quantity": "1",
                "unit": "per_image",
                "expiresAt": "2030-01-01T00:00:00Z",
            }
        )

    async def create(self, request: web.Request) -> web.Response:
        body = await request.json()
        n = self._note("create", request, body)
        if body["model"] == "always/refunded/x":
            return envelope(None, code=50302, status=503)
        if n == 1 and self.behaviour.get("create_503_first"):
            return envelope(None, code=503, status=503, **{"Retry-After": "0"})
        if n == 1 and self.behaviour.get("create_40901_first"):
            return envelope(None, code=40901, status=409)
        return envelope({"taskId": "job_1", "state": "queued", "estimatedCost": "0.08", "estimatedCredits": 8}, status=202)

    async def record(self, request: web.Request) -> web.Response:
        n = self._note("record", request)
        output = self.behaviour.get("output")
        if output is None:
            pending = {"mime": "image/png", "pending": True}
            ready = {"mime": "image/png", "url": "https://x/y.png"}
            output = {"assets": [pending if n == 1 else ready]}
        state = self.behaviour.get("state", "succeeded")
        return envelope(
            {"taskId": "job_1", "model": "m/x/y", "state": state, "output": output, "credits": 8, "cost": "0.08", "settled": True}
        )

    async def ticket(self, request: web.Request) -> web.Response:
        body = await request.json()
        self._note("ticket", request, body)
        return envelope(
            {
                "fileId": "fil_1",
                "key": "popnow://f/fil_1",
                "uploadUrl": f"{self.base}/storage/object",
                "method": "PUT",
                "headers": {"Content-Type": body["contentType"], "X-Signed": "yes"},
                "expiresAt": "2030-01-01T00:00:00Z",
                "maxBytes": self.behaviour.get("max_bytes", 1024),
            }
        )

    async def put(self, request: web.Request) -> web.Response:
        data = await request.read()
        self._note("put", request, data)
        ok = request.headers.get("X-Signed") == "yes" and "Authorization" not in request.headers
        return web.Response(status=200 if ok else 403)

    async def commit(self, request: web.Request) -> web.Response:
        self._note("commit", request)
        return envelope(
            {"fileId": request.match_info["file_id"], "status": "ready", "uri": f"popnow://f/{request.match_info['file_id']}"}
        )

    async def import_file(self, request: web.Request) -> web.Response:
        body = await request.json()
        self._note("import", request, body)
        return envelope({"fileId": "fil_lora", "status": "ready", "uri": "popnow://f/fil_lora"})

    async def result_file(self, request: web.Request) -> web.Response:
        self._note("result", request)
        return web.Response(body=b"RESULT-BYTES", content_type="audio/mpeg")
