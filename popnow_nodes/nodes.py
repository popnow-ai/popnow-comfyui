"""ComfyUI node classes: one per catalog model, plus PopNow Generate and PopNow LoRA."""

from __future__ import annotations

import asyncio
import hashlib
import json
import logging
import mimetypes
import os
import re
import time
import urllib.parse
import uuid
from typing import Any

from comfy_api.latest import io

from . import config
from .client import (
    PopNowApiError,
    PopNowClient,
    PopNowTaskFailed,
    output_assets,
    output_text,
)
from .fields import (
    OMIT,
    FieldSpec,
    OutputPlan,
    build_fields,
    category_for,
    family_name,
    model_page,
    node_id_for,
    plan_outputs,
    widget_to_value,
)
from .pricing import badge_for, describe_price

log = logging.getLogger("popnow")

LORAS = io.Custom("POPNOW_LORAS")

NO_KEY_MESSAGE = (
    "No PopNow API key is set. Open Settings > PopNow and paste a key from "
    "https://popnow.ai/api/console/keys, or set the POPNOW_API_KEY environment variable, then run "
    "the workflow again."
)
UPLOAD_CACHE_SECONDS = 12 * 3600
DEFAULT_TASK_TIMEOUT_SECONDS = 3600
GENERATE_NODE_ID = "PopNowGenerate"
LORA_NODE_ID = "PopNow_LoRA"
# Defaults of the single-file node published on popnow.ai, so both read the same.
GENERATE_DEFAULT_MODEL = "google/nano-banana-2.1/text-to-image"
GENERATE_DEFAULT_PROMPT = "A lighthouse on a cliff at dusk, warm window light"
GENERATE_DEFAULT_OPTIONS = '{"aspect_ratio": "16:9", "resolution": "1k"}'
EXTENSION_BY_MIME = {"video/mp4": ".mp4", "video/webm": ".webm", "audio/mpeg": ".mp3", "audio/wav": ".wav"}
LORA_IMPORT_HOSTS = ("huggingface.co", "hf.co", "civitai.com")
HF_REPO_ID = re.compile(r"^[A-Za-z0-9][\w.-]*/[\w.-]+$")

# (account, content key) -> (popnow:// URI, stored at). Uploaded files are kept on PopNow for a
# while, so re-running a workflow with a different prompt does not send the same picture again.
_upload_cache: dict[tuple[str, str], tuple[str, float]] = {}
# Model call name -> input schema, filled by build_all; PopNow Generate reads it to name the
# prompt field ("prompt" for most models, "text" for speech).
_SCHEMAS: dict[str, dict[str, Any]] = {}


def _media() -> Any:
    """The tensor and file conversions; imported on first use so loading needs no torch."""
    from . import media

    return media


def _interrupt_check() -> None:
    import comfy.model_management

    comfy.model_management.throw_exception_if_processing_interrupted()


def _show(node_id: str | None, text: str) -> None:
    if not node_id:
        return
    try:
        from server import PromptServer

        PromptServer.instance.send_progress_text(text, node_id)
    except Exception:  # the status line is a courtesy; never fail a run over it
        pass


def _account(client: PopNowClient) -> str:
    return hashlib.sha256(client.api_key.encode()).hexdigest()[:16]


async def _cached(client: PopNowClient, key: str, make: Any) -> str:
    cache_key = (_account(client), key)
    cached = _upload_cache.get(cache_key)
    if cached and time.time() - cached[1] < UPLOAD_CACHE_SECONDS:
        return cached[0]
    uri = await make()
    _upload_cache[cache_key] = (uri, time.time())
    return uri


async def _upload(client: PopNowClient, data: bytes, content_type: str) -> str:
    digest = hashlib.sha256(data).hexdigest()
    return await _cached(client, f"sha256:{digest}", lambda: client.upload(data, content_type))


def _content_type_for_path(path: str) -> str:
    guessed, _ = mimetypes.guess_type(path)
    suffix = os.path.splitext(path)[1].lower()
    overrides = {
        ".md": "text/markdown",
        ".markdown": "text/markdown",
        ".key": "application/vnd.apple.keynote",
        ".pages": "application/vnd.apple.pages",
        ".numbers": "application/vnd.apple.numbers",
        ".mp3": "audio/mpeg",
        ".wav": "audio/wav",
        ".safetensors": "application/octet-stream",
    }
    return overrides.get(suffix) or guessed or "application/octet-stream"


def _input_file(name: str) -> str:
    """Resolve a file name inside ComfyUI's input folder, and nowhere else.

    Workflows are shared freely, so a path typed into a node must not be able to reach outside
    the folder meant for inputs (a workflow pointing at ~/.ssh would otherwise upload it).
    """
    import folder_paths

    base = os.path.realpath(folder_paths.get_input_directory())
    candidate = os.path.realpath(os.path.join(base, name))
    if os.path.commonpath([base, candidate]) != base:
        raise ValueError(
            f"{name} is outside ComfyUI's input folder. Put the file in {base} and give its name, or use an https:// link."
        )
    if not os.path.isfile(candidate):
        raise ValueError(f"{name} was not found in ComfyUI's input folder ({base}).")
    return candidate


def _socket_values(value: Any) -> list[Any]:
    """Values connected to an Autogrow group, in socket order."""
    if value is None:
        return []
    if isinstance(value, dict):

        def index(key: str) -> int:
            match = re.search(r"(\d+)$", key)
            return int(match.group(1)) if match else 0

        return [value[k] for k in sorted(value, key=index) if value[k] is not None]
    return [value]


async def _upload_images(client: PopNowClient, raw: Any) -> list[str]:
    media = _media()
    pictures = [p for value in _socket_values(raw) for p in media.split_image_batch(value)]
    return [await _upload(client, *media.encode_image(p)) for p in pictures]


async def _field_value(client: PopNowClient, spec: FieldSpec, raw: Any) -> Any:
    if spec.kind == "image":
        if raw is None:
            return OMIT
        media = _media()
        pictures = media.split_image_batch(raw)
        if not pictures:
            return OMIT
        if len(pictures) > 1:
            log.info("PopNow: '%s' takes one image; using the first of %d", spec.label, len(pictures))
        return await _upload(client, *media.encode_image(pictures[0]))
    if spec.kind == "images":
        refs = await _upload_images(client, raw)
        return refs or OMIT
    if spec.kind == "video":
        return OMIT if raw is None else await _upload(client, *_media().encode_video(raw))
    if spec.kind == "videos":
        clips = _socket_values(raw)
        return [await _upload(client, *_media().encode_video(c)) for c in clips] if clips else OMIT
    if spec.kind == "audio":
        return OMIT if raw is None else await _upload(client, *_media().encode_audio(raw))
    if spec.kind == "audios":
        clips = _socket_values(raw)
        return [await _upload(client, *_media().encode_audio(c)) for c in clips] if clips else OMIT
    if spec.kind == "loras":
        return list(raw) if raw else OMIT
    if spec.kind == "file":
        text = str(raw or "").strip()
        if not text:
            return OMIT
        if text.startswith(("http://", "https://", "popnow://")):
            return text
        path = _input_file(text)
        with open(path, "rb") as handle:
            data = handle.read()
        return await _upload(client, data, _content_type_for_path(path))
    value = widget_to_value(spec, raw)
    if value is not OMIT and spec.kind == "string" and spec.required and not str(value).strip():
        raise ValueError(f"'{spec.label}' is required")
    return value


def _input_for(spec: FieldSpec) -> io.Input:
    common = {"tooltip": spec.tooltip or None}
    optional = not spec.required
    label = spec.label if spec.label != spec.name else None
    if spec.kind in ("image", "video", "audio"):
        socket = {"image": io.Image, "video": io.Video, "audio": io.Audio}[spec.kind]
        return socket.Input(spec.name, display_name=label, optional=optional, **common)
    if spec.kind in ("images", "videos", "audios"):
        socket = {"images": io.Image, "videos": io.Video, "audios": io.Audio}[spec.kind]
        # Sockets are named after the field (reference_image_0, reference_image_1...), since the
        # group label itself is not drawn on the node.
        stem = re.sub(r"_urls?$", "", spec.name)
        prefix = f"{stem}_"
        return io.Autogrow.Input(
            spec.name,
            template=io.Autogrow.TemplatePrefix(
                socket.Input(stem, optional=spec.min_items == 0),
                prefix=prefix,
                min=spec.min_items,
                max=spec.max_items,
            ),
            display_name=label,
            optional=optional,
            **common,
        )
    if spec.kind == "loras":
        return LORAS.Input(spec.name, display_name=label, optional=True, **common)
    if spec.kind in ("int_socket", "float_socket"):
        number = io.Int if spec.kind == "int_socket" else io.Float
        return number.Input(spec.name, display_name=label, optional=True, force_input=True, **common)
    widget = {"advanced": spec.advanced or None, "display_name": label, **common}
    if spec.kind == "combo":
        return io.Combo.Input(spec.name, options=spec.options, default=spec.default, **widget)
    if spec.kind == "bool":
        return io.Boolean.Input(spec.name, default=bool(spec.default), **widget)
    if spec.kind == "int":
        extra: dict[str, Any] = {}
        if spec.seed:
            # Fixed, not randomize: every run is billed, so queueing the same workflow twice
            # should reuse the cached result instead of paying for a second one by surprise.
            extra["control_after_generate"] = io.ControlAfterGenerate.fixed
        if spec.slider:
            extra["display_mode"] = io.NumberDisplay.slider
        return io.Int.Input(
            spec.name,
            default=int(spec.default),
            min=int(spec.minimum) if spec.minimum is not None else -(2**31),
            max=int(spec.maximum) if spec.maximum is not None else 2**31 - 1,
            step=int(spec.step or 1),
            **extra,
            **widget,
        )
    if spec.kind == "float":
        extra = {"display_mode": io.NumberDisplay.slider} if spec.slider else {}
        step = float(spec.step or 0.01)
        return io.Float.Input(
            spec.name,
            default=float(spec.default),
            min=float(spec.minimum) if spec.minimum is not None else -1e9,
            max=float(spec.maximum) if spec.maximum is not None else 1e9,
            step=step,
            round=step,
            **extra,
            **widget,
        )
    if spec.kind in ("string", "file", "json"):
        placeholder = "File name in ComfyUI/input, or an https:// link" if spec.kind == "file" else None
        return io.String.Input(
            spec.name,
            default=str(spec.default or ""),
            multiline=spec.multiline,
            placeholder=placeholder,
            **widget,
        )
    raise ValueError(f"unhandled field kind {spec.kind}")


def _task_id_output() -> io.Output:
    return io.String.Output("task_id", display_name="task id", tooltip="The PopNow task id, for the API console logs or support.")


def _outputs_for(plan: OutputPlan) -> list[io.Output]:
    task_id = _task_id_output()
    if plan.primary == "image":
        outputs: list[io.Output] = [io.Image.Output("images", display_name="images")]
        if plan.alpha:
            outputs.append(io.Mask.Output("alpha", display_name="alpha", tooltip="Transparency of each image: 1 is opaque."))
        return [*outputs, task_id]
    if plan.primary == "video":
        outputs = [io.Video.Output("video", display_name="video")]
        if plan.last_frame:
            outputs.append(io.Image.Output("last_frame", display_name="last frame", tooltip="Needs return_last_frame turned on."))
        return [*outputs, task_id]
    if plan.primary == "audio":
        return [
            io.Audio.Output(
                "audio",
                display_name="audio",
                tooltip="Several results come back as a batch; Save Audio writes one file each.",
            ),
            task_id,
        ]
    return [io.String.Output("text", display_name="text"), task_id]


async def _download_all(client: PopNowClient, assets: list[dict[str, Any]], prefix: str, limit: int | None = None) -> list[bytes]:
    wanted = [a for a in assets if str(a.get("mime") or "").startswith(prefix) and a.get("url")]
    if limit is not None:
        wanted = wanted[:limit]
    return list(await asyncio.gather(*(client.download(str(a["url"])) for a in wanted)))


async def _collect_outputs(client: PopNowClient, plan: OutputPlan, task: dict[str, Any]) -> list[Any]:
    task_id = str(task.get("taskId") or "")
    assets = output_assets(task)
    if plan.primary == "text":
        return [_task_text(task), task_id]
    media = _media()
    if plan.primary == "image":
        blobs = await _download_all(client, assets, "image/")
        images, alpha = media.decode_images(blobs)
        return [images, alpha, task_id] if plan.alpha else [images, task_id]
    if plan.primary == "video":
        videos = await _download_all(client, assets, "video/", limit=1)
        if not videos:
            raise ValueError(f"task {task_id} finished without a video")
        result: list[Any] = [media.decode_video(videos[0])]
        if plan.last_frame:
            from comfy_execution.graph_utils import ExecutionBlocker

            frames = await _download_all(client, assets, "image/", limit=1)
            result.append(
                media.decode_images(frames)[0]
                if frames
                else ExecutionBlocker("Turn on return_last_frame on the PopNow node to get the last frame.")
            )
        return [*result, task_id]
    clips = [media.decode_audio(blob) for blob in await _download_all(client, assets, "audio/")]
    if not clips:
        raise ValueError(f"task {task_id} finished without audio")
    return [_audio_batch(clips), task_id]


def _task_text(task: dict[str, Any]) -> str:
    text = output_text(task)
    if text is not None:
        return text
    output = task.get("output")
    if isinstance(output, dict):
        rest = {k: v for k, v in output.items() if k != "assets"}
        if rest:
            return json.dumps(rest, ensure_ascii=False, indent=2)
    return ""


def _audio_batch(clips: list[dict[str, Any]]) -> dict[str, Any]:
    """Several clips as one AUDIO batch, padded to the longest and matched on sample rate."""
    import torch

    rate = clips[0]["sample_rate"]
    channels = max(c["waveform"].shape[1] for c in clips)
    waves = []
    for clip in clips:
        wave = clip["waveform"][0]
        if clip["sample_rate"] != rate:
            length = round(wave.shape[1] * rate / clip["sample_rate"])
            wave = torch.nn.functional.interpolate(wave.unsqueeze(0), size=length, mode="linear", align_corners=False)[0]
        if wave.shape[0] < channels:
            wave = wave.repeat(channels // wave.shape[0], 1)[:channels]
        waves.append(wave)
    length = max(w.shape[1] for w in waves)
    padded = [torch.nn.functional.pad(w, (0, length - w.shape[1])) for w in waves]
    return {"waveform": torch.stack(padded), "sample_rate": rate}


def _credits_of(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return int(value)
    try:
        return int(str(value))
    except (TypeError, ValueError):
        return None


async def _quote_within_limit(client: PopNowClient, model_id: str, payload: dict[str, Any]) -> dict[str, Any]:
    """Quote the run and stop, before anything is held, if it could exceed the user's limit."""
    quote = await client.quote(model_id, payload)
    ceiling = config.get_max_credits_per_run()
    worst = _credits_of(quote.get("maxCredits"))
    if ceiling is not None and worst is not None and worst > ceiling:
        raise ValueError(
            f"This run could cost up to {worst} credits, above your limit of {ceiling} credits per "
            "run (Settings > PopNow). Nothing was charged."
        )
    return quote


async def submit_and_wait(
    client: PopNowClient,
    model_id: str,
    payload: dict[str, Any],
    node_id: str | None,
    timeout_seconds: float,
) -> dict[str, Any]:
    """Quote, create the task, and poll it to a terminal state. Raises unless it succeeded."""
    quote = await _quote_within_limit(client, model_id, payload)
    expected = _credits_of(quote.get("maxCredits"))
    usual = _credits_of(quote.get("expectedCredits")) or expected
    _show(node_id, f"Submitting. Estimated {usual} credits")

    idempotency_key = str(uuid.uuid4())
    try:
        task = await client.create_task(
            model_id, payload, idempotency_key=idempotency_key, quote_id=quote.get("quoteId"), expected_credits=expected
        )
    except PopNowApiError as error:
        if error.code != 40901:
            raise
        # The price moved between quote and submit: quote again and resend under the same key,
        # so a task the server did accept is recovered rather than created twice.
        quote = await _quote_within_limit(client, model_id, payload)
        expected = _credits_of(quote.get("maxCredits"))
        usual = _credits_of(quote.get("expectedCredits")) or expected
        task = await client.create_task(
            model_id, payload, idempotency_key=idempotency_key, quote_id=quote.get("quoteId"), expected_credits=expected
        )
    task_id = str(task.get("taskId") or "")

    def on_poll(record: dict[str, Any], elapsed: float) -> None:
        state = str(record.get("state") or "")
        label = {"queued": "Queued", "running": "Generating"}.get(state, state.capitalize())
        _show(node_id, f"{label} {int(elapsed)}s. Estimated {usual} credits\nTask {task_id}")

    try:
        final = await client.wait_for_task(task_id, timeout_seconds=timeout_seconds, on_poll=on_poll)
    except BaseException as error:
        if type(error).__name__ == "InterruptProcessingException":
            log.warning(
                "PopNow: stopped waiting for task %s. It keeps running on PopNow and is charged if "
                "it succeeds; its result stays available in the API console logs.",
                task_id,
            )
            _show(node_id, f"Stopped waiting. Task {task_id} keeps running on PopNow.")
        raise
    if final.get("state") != "succeeded":
        _show(node_id, f"Failed: {final.get('errorCode') or final.get('state')}\nTask {task_id}")
        raise PopNowTaskFailed(final)
    return final


def _done_text(final: dict[str, Any], started: float) -> str:
    credits = final.get("credits")
    verb = "Charged" if final.get("settled") else "Held"
    amount = f"{credits} credits" if credits is not None else "the quoted amount"
    return f"Done in {int(time.monotonic() - started)}s. {verb} {amount}\nTask {final.get('taskId')}"


async def run_model(
    model: dict[str, Any],
    specs: list[FieldSpec],
    plan: OutputPlan,
    node_id: str | None,
    values: dict[str, Any],
) -> list[Any]:
    api_key, _ = config.get_api_key()
    if not api_key:
        raise ValueError(NO_KEY_MESSAGE)
    model_id = str(model["model"])
    started = time.monotonic()
    async with PopNowClient(api_key, config.get_base_url(), interrupt_check=_interrupt_check) as client:
        _show(node_id, "Preparing inputs...")
        payload: dict[str, Any] = {}
        for spec in specs:
            value = await _field_value(client, spec, values.get(spec.name))
            if value is not OMIT:
                payload[spec.name] = value
        timeout = float(model.get("taskTimeoutSeconds") or DEFAULT_TASK_TIMEOUT_SECONDS) + 300
        final = await submit_and_wait(client, model_id, payload, node_id, timeout)
        _show(node_id, "Downloading result...")
        outputs = await _collect_outputs(client, plan, final)
        _show(node_id, _done_text(final, started))
        return outputs


def make_model_node(model: dict[str, Any]) -> type[io.ComfyNode]:
    specs = build_fields(model.get("inputSchema") or {})
    plan = plan_outputs(model)
    node_id = node_id_for(str(model["model"]))
    badge = badge_for(model)
    description = "\n\n".join(
        part
        for part in (
            str(model.get("summary") or "").strip(),
            describe_price(badge),
            f"Model: {model['model']}",
            f"Fields, prices and examples: {model_page(model)}",
        )
        if part
    )
    aliases = [str(model["model"]), "popnow", family_name(model)]

    def define_schema(cls: type[io.ComfyNode]) -> io.Schema:
        return io.Schema(
            node_id=node_id,
            display_name=str(model.get("displayName") or model["model"]),
            category=category_for(model),
            description=description,
            inputs=[_input_for(spec) for spec in specs],
            outputs=_outputs_for(plan),
            hidden=[io.Hidden.unique_id],
            search_aliases=aliases,
        )

    async def execute(cls: type[io.ComfyNode], **kwargs: Any) -> io.NodeOutput:
        unique_id = cls.hidden.unique_id if cls.hidden is not None else None
        outputs = await run_model(model, specs, plan, unique_id, kwargs)
        return io.NodeOutput(*outputs)

    return type(
        node_id,
        (io.ComfyNode,),
        {"define_schema": classmethod(define_schema), "execute": classmethod(execute)},
    )


# -- PopNow Generate ---------------------------------------------------------


def prompt_field_for(model_id: str, options: dict[str, Any]) -> str:
    """Where the prompt goes: ``prompt`` for most models, ``text`` for speech models."""
    if "prompt" in options or "text" in options:
        return "prompt" if "prompt" in options else "text"
    properties = (_SCHEMAS.get(model_id) or {}).get("properties") or {}
    if "prompt" not in properties and "text" in properties:
        return "text"
    return "prompt"


def build_generate_input(model_id: str, prompt: str, options: str, image_refs: list[str], image_field: str) -> dict[str, Any]:
    """The task input PopNow Generate sends; the same rules as the single-file node."""
    try:
        task_input = json.loads(options or "{}")
    except ValueError as error:
        raise ValueError(f'\'options\' must be a JSON object, for example {{"resolution": "2k"}}: {error}') from error
    if not isinstance(task_input, dict):
        raise ValueError('\'options\' must be a JSON object, for example {"resolution": "2k"}')
    if prompt.strip():
        task_input.setdefault(prompt_field_for(model_id, task_input), prompt)
    if image_refs:
        field = (image_field or "image_url").strip()
        task_input[field] = image_refs if field.endswith("s") else image_refs[0]
    return task_input


class PopNowGenerate(io.ComfyNode):
    """Any model by call name, with the options as JSON. Same node type as the single-file node."""

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id=GENERATE_NODE_ID,
            display_name="PopNow Generate",
            category="PopNow",
            description=(
                "Runs any PopNow image, video or audio model by its call name. Write the model's "
                "other fields as JSON in options. Image models return an IMAGE; video and audio are "
                "saved to ComfyUI's output folder and returned as a path. For typed inputs and a "
                "price badge, use the model's own node instead.\n\nModel IDs: https://popnow.ai/docs/models"
            ),
            inputs=[
                io.String.Input(
                    "model",
                    default=GENERATE_DEFAULT_MODEL,
                    tooltip="A call name from https://popnow.ai/docs/models, such as minimax/h3/image-to-video.",
                ),
                io.String.Input("prompt", multiline=True, default=GENERATE_DEFAULT_PROMPT),
                io.String.Input(
                    "options",
                    multiline=True,
                    default=GENERATE_DEFAULT_OPTIONS,
                    tooltip='The model\'s other fields as JSON, such as {"resolution": "2k"}.',
                ),
                io.Image.Input("image", optional=True, tooltip="Uploaded for you and put in image_field."),
                io.String.Input(
                    "image_field",
                    default="image_url",
                    optional=True,
                    tooltip="Which field gets the image: image_url for most video models, image_urls for editing.",
                ),
            ],
            outputs=[
                io.Image.Output("image", display_name="image"),
                io.String.Output("url", display_name="url", tooltip="Signed file URL, valid for about 20 minutes."),
                io.String.Output("path", display_name="path", tooltip="Saved video or audio file, in ComfyUI/output."),
            ],
            hidden=[io.Hidden.unique_id],
            search_aliases=["popnow", "popnow api", "cloud generate"],
        )

    @classmethod
    async def execute(
        cls,
        model: str,
        prompt: str,
        options: str,
        image: Any = None,
        image_field: str = "image_url",
    ) -> io.NodeOutput:
        api_key, _ = config.get_api_key()
        if not api_key:
            raise ValueError(NO_KEY_MESSAGE)
        model_id = model.strip()
        if not model_id:
            raise ValueError("Set 'model' to a call name from https://popnow.ai/docs/models.")
        node_id = cls.hidden.unique_id if cls.hidden is not None else None
        started = time.monotonic()
        async with PopNowClient(api_key, config.get_base_url(), interrupt_check=_interrupt_check) as client:
            refs = await _upload_images(client, image) if image is not None else []
            task_input = build_generate_input(model_id, prompt, options, refs, image_field)
            final = await submit_and_wait(client, model_id, task_input, node_id, DEFAULT_TASK_TIMEOUT_SECONDS + 300)
            assets = [a for a in output_assets(final) if a.get("url")]
            if not assets:
                raise ValueError(f"task {final.get('taskId')} finished without a file")
            _show(node_id, "Downloading result...")
            first = assets[0]
            mime = str(first.get("mime") or "")
            media = _media()
            if mime.startswith("image/"):
                blobs = await _download_all(client, assets, "image/")
                images, _alpha = media.decode_images(blobs)
                _show(node_id, _done_text(final, started))
                return io.NodeOutput(images, str(first["url"]), "")
            content = await client.download(str(first["url"]))
            path = _save_output(str(final.get("taskId") or uuid.uuid4().hex), mime, content)
            _show(node_id, _done_text(final, started))
            # Video and audio: a small blank IMAGE keeps the graph valid; use the path output.
            return io.NodeOutput(media.empty_image(), str(first["url"]), path)


def _save_output(task_id: str, mime: str, content: bytes) -> str:
    import folder_paths

    extension = EXTENSION_BY_MIME.get(mime) or mimetypes.guess_extension(mime) or ".bin"
    safe_id = re.sub(r"[^0-9A-Za-z_-]+", "_", task_id)
    path = os.path.join(folder_paths.get_output_directory(), f"popnow_{safe_id}{extension}")
    with open(path, "wb") as handle:
        handle.write(content)
    return path


# -- LoRA ------------------------------------------------------------------


def lora_source_kind(source: str) -> str:
    """How a LoRA reference is resolved: ``uri``, ``direct``, ``import`` or ``local``."""
    text = source.strip()
    if text.startswith("popnow://"):
        return "uri"
    if text.startswith(("http://", "https://")):
        host = (urllib.parse.urlparse(text).hostname or "").lower()
        if any(host == h or host.endswith("." + h) for h in LORA_IMPORT_HOSTS):
            return "import"
        return "direct"
    if HF_REPO_ID.match(text) and not text.lower().endswith(".safetensors"):
        return "import"
    return "local"


def _import_token(source: str) -> str:
    """A download token from the environment, never from a widget (widgets end up in workflows)."""
    lowered = source.lower()
    if "civitai.com" in lowered:
        return os.environ.get("CIVITAI_API_KEY", "").strip()
    return (os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN") or "").strip()


def _local_lora(name: str) -> str:
    import folder_paths

    path = folder_paths.get_full_path("loras", name)
    if not path or not os.path.isfile(path):
        raise ValueError(f"{name} is not a file in ComfyUI's loras folder, a Hugging Face repo id, or an https:// link.")
    return path


async def resolve_lora(client: PopNowClient, source: str) -> str:
    """A ``loras[].path`` value for this reference, uploading or importing it when needed."""
    text = source.strip()
    kind = lora_source_kind(text)
    if kind in ("uri", "direct"):
        return text
    if kind == "import":
        return await _cached(client, f"import:{text}", lambda: client.import_lora(text, _import_token(text)))
    path = _local_lora(text)
    stat = os.stat(path)
    key = f"local:{os.path.realpath(path)}:{stat.st_size}:{int(stat.st_mtime)}"
    return await _cached(client, key, lambda: client.upload_file(path, "application/octet-stream"))


class PopNowLoRA(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id=LORA_NODE_ID,
            display_name="PopNow LoRA",
            category="PopNow/Utils",
            description=(
                "Adds a LoRA weights file to a PopNow LoRA model (their names end in LoRA). Chain "
                "several to stack them; most LoRA models accept up to three. The source can be a "
                ".safetensors file in ComfyUI/models/loras (uploaded once), a Hugging Face repo id "
                "or page, a Civitai page (imported by PopNow; set HF_TOKEN or CIVITAI_API_KEY for "
                "gated files), or any direct https link."
            ),
            inputs=[
                io.String.Input(
                    "source",
                    default="",
                    placeholder="my_style.safetensors, owner/repo, or https://.../weights.safetensors",
                    tooltip="A file in ComfyUI/models/loras, a Hugging Face repo id or page, a Civitai page, or an https link.",
                ),
                io.Float.Input(
                    "scale",
                    default=1.0,
                    min=-1.0,
                    max=4.0,
                    step=0.05,
                    round=0.01,
                    tooltip="Strength of this LoRA. Most models accept 0 to 4; the model checks its own range.",
                ),
                LORAS.Input("loras", optional=True, tooltip="LoRAs from another PopNow LoRA node."),
            ],
            outputs=[LORAS.Output("loras", display_name="loras")],
            search_aliases=["lora", "popnow lora"],
        )

    @classmethod
    async def execute(cls, source: str, scale: float, loras: list[dict[str, Any]] | None = None) -> io.NodeOutput:
        stack = list(loras or [])
        text = source.strip()
        if text:
            kind = lora_source_kind(text)
            if kind in ("uri", "direct"):
                path = text
            else:
                api_key, _ = config.get_api_key()
                if not api_key:
                    raise ValueError(NO_KEY_MESSAGE)
                async with PopNowClient(api_key, config.get_base_url(), interrupt_check=_interrupt_check) as client:
                    path = await resolve_lora(client, text)
            stack.append({"path": path, "scale": round(float(scale), 4)})
        return io.NodeOutput(stack)


# -- Registry ----------------------------------------------------------------


def _badge_labels(specs: list[FieldSpec], badge: dict[str, Any]) -> dict[str, dict[str, str]]:
    """Dropdown label -> pricing value, for the pricing fields whose labels differ from values."""
    fields = set(badge.get("fields") or [])
    labels: dict[str, dict[str, str]] = {}
    for spec in specs:
        if spec.kind != "combo" or spec.name not in fields:
            continue
        mapping = {
            label: (str(value).lower() if isinstance(value, bool) else str(value))
            for label, value in zip(spec.options, spec.option_values, strict=False)
            if value is not OMIT
        }
        if any(label != value for label, value in mapping.items()):
            labels[spec.name] = mapping
    return labels


def is_media_model(model: dict[str, Any]) -> bool:
    """Image, video and audio models only: PopNow has no text or chat models on its API."""
    if model.get("enabled") is False:
        return False
    return model.get("modality") in ("image", "video", "audio") and "chat" not in (model.get("tasks") or [])


def build_all(items: list[dict[str, Any]]) -> tuple[list[type[io.ComfyNode]], dict[str, Any]]:
    """Node classes for the catalog, plus the price badge table keyed by node type."""
    nodes: list[type[io.ComfyNode]] = [PopNowGenerate, PopNowLoRA]
    badges: dict[str, Any] = {}
    seen: set[str] = set()
    _SCHEMAS.clear()
    for model in items:
        if not is_media_model(model):
            continue
        node_id = node_id_for(str(model["model"]))
        if node_id in seen:
            log.warning("PopNow: two models map to node type %s; keeping the first", node_id)
            continue
        try:
            node = make_model_node(model)
            node.GET_SCHEMA()  # fail here, per model, rather than taking the whole extension down
        except Exception as error:
            log.warning("PopNow: skipped %s: %s", model.get("model"), error)
            continue
        seen.add(node_id)
        nodes.append(node)
        _SCHEMAS[str(model["model"])] = model.get("inputSchema") or {}
        badge = badge_for(model)
        if badge:
            badge["labels"] = _badge_labels(build_fields(model.get("inputSchema") or {}), badge)
            badges[node_id] = badge
    return nodes, badges


__all__ = [
    "PopNowGenerate",
    "PopNowLoRA",
    "build_all",
    "build_generate_input",
    "lora_source_kind",
    "make_model_node",
    "run_model",
]
