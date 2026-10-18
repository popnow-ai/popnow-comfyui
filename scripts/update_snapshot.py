"""Refresh data/catalog-snapshot.json, the model list used before a user has set a key.

Once a key is set, ComfyUI fetches the live list at every start, so the snapshot only decides
which nodes exist on a fresh install. Two sources:

    POPNOW_API_KEY=sk-popnow-... python scripts/update_snapshot.py
        The authoritative list: GET https://api.popnow.ai/api/v1/models?includeSchema=1.
        This endpoint needs an API key.

    python scripts/update_snapshot.py --public
        No key needed. Rebuilt from the public model reference (https://popnow.ai/docs/models,
        which lists every call name per model) and the public per-model files on popnow.ai
        (https://popnow.ai/catalog/<model>.json, the input schemas and credit prices the
        website and the API reference pages use).

Both write the same shape. Run python scripts/render_docs.py afterwards.
"""

from __future__ import annotations

import argparse
import asyncio
import html
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

TARGET = ROOT / "data" / "catalog-snapshot.json"
SITE = "https://popnow.ai"
USER_AGENT = "popnow-comfyui-snapshot/1.0 (+https://github.com/popnow-ai/popnow-comfyui)"
# Fields the website form shows that the API does not accept; the API would reject them.
WEB_ONLY_FIELDS = ("official_fallback",)
# Call names publish image editing as ".../edit"; the website files classify it like this.
EDIT_TASKS = ("image-to-image", "image-edit")
ROW = re.compile(
    r'<tr><td><a href="/docs/models/([^"]+)">([^<]+)</a><span class="pn-provider">([^<]*)</span></td><td>(.*?)</td>',
    re.S,
)
CALL = re.compile(r'<code class="pn-id-line">([^<]+)</code>')


def _get(url: str) -> bytes:
    # An explicit User-Agent: the API edge rejects default client agents.
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json, text/html"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return response.read()
        except OSError:  # URLError and dropped connections; a few retries ride out a blip
            if attempt == 3:
                raise
            time.sleep(2**attempt)
    raise AssertionError("unreachable")


def task_label(call_name: str) -> str:
    """``text-to-video`` -> ``Text to Video``, ``edit`` -> ``Edit``."""
    words = call_name.rsplit("/", 1)[-1].split("-")
    return " ".join(w if w == "to" else w.capitalize() for w in words)


def _endpoint_for(call_name: str, endpoints: list[dict[str, Any]]) -> dict[str, Any] | None:
    suffix = call_name.rsplit("/", 1)[-1]
    for endpoint in endpoints:
        task = endpoint.get("task")
        if task == suffix or (suffix == "edit" and task in EDIT_TASKS):
            return endpoint
    return None


def _clean_schema(schema: dict[str, Any]) -> dict[str, Any]:
    schema = json.loads(json.dumps(schema))
    properties = schema.get("properties") or {}
    for name in WEB_ONLY_FIELDS:
        properties.pop(name, None)
    if isinstance(schema.get("required"), list):
        schema["required"] = [r for r in schema["required"] if r not in WEB_ONLY_FIELDS]
    return schema


def build_public() -> list[dict[str, Any]]:
    page = _get(f"{SITE}/docs/models").decode("utf-8")
    rows = ROW.findall(page)
    if not rows:
        raise SystemExit("the public model reference changed shape; no model rows found")
    items: list[dict[str, Any]] = []
    for slug, name, provider, cell in rows:
        name, provider = html.unescape(name), html.unescape(provider)
        record = json.loads(_get(f"{SITE}/catalog/{slug}.json"))
        for call_name in CALL.findall(cell):
            endpoint = _endpoint_for(call_name, record.get("endpoints") or [])
            if endpoint is None:
                print(f"skipped {call_name}: no matching endpoint in {slug}.json", file=sys.stderr)
                continue
            items.append(
                {
                    "model": call_name,
                    "displayName": f"{name} · {task_label(call_name)}",
                    "familyDisplayName": name,
                    "provider": provider,
                    "modality": record.get("category"),
                    "tasks": [endpoint.get("task")],
                    "inputSchema": _clean_schema(endpoint.get("inputSchema") or {}),
                    "credits": endpoint.get("credits"),
                    "summary": record.get("tagline") or "",
                    "docsSlug": slug,
                }
            )
    return items


async def build_live(api_key: str) -> list[dict[str, Any]]:
    from popnow_nodes import catalog

    return await catalog.fetch_live(api_key)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--public", action="store_true", help="build from public popnow.ai pages, no key needed")
    args = parser.parse_args()
    if args.public:
        items, source = build_public(), "public"
    else:
        api_key = os.environ.get("POPNOW_API_KEY", "").strip()
        if not api_key:
            raise SystemExit("set POPNOW_API_KEY, or pass --public to build from the public pages")
        items, source = asyncio.run(build_live(api_key)), "api"
    if not items:
        raise SystemExit("no models came back; refusing to write an empty snapshot")
    with open(TARGET, "w", encoding="utf-8") as handle:
        # ensure_ascii keeps the file pure ASCII whatever the model data contains.
        json.dump({"fetchedAt": int(time.time()), "source": source, "items": items}, handle, ensure_ascii=True, indent=1)
        handle.write("\n")
    print(f"wrote {len(items)} models to {TARGET.relative_to(ROOT)} (source: {source})")


if __name__ == "__main__":
    main()
