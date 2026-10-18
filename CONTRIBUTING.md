# Contributing

Thanks for helping improve PopNow for ComfyUI.

## Development setup

```bash
git clone https://github.com/popnow-ai/popnow-comfyui
cd popnow-comfyui
python -m venv .venv && . .venv/bin/activate
pip install aiohttp
python -m unittest discover -s tests -t .
```

The tests never call the live API and need no key: ComfyUI is replaced by `tests/comfy_stub.py` and the
API by a local fake (`tests/fake_api.py`). To try the nodes for real, link or clone the repository into
`ComfyUI/custom_nodes` and restart ComfyUI.

## Guidelines

- Install nothing: use only what ComfyUI ships (aiohttp, torch, Pillow, NumPy, PyAV). Keep Python 3.10
  support.
- Keep `fields`, `pricing`, `catalog`, `config` and `client` free of ComfyUI imports so they stay testable.
- Follow the API contract in the [OpenAPI spec](https://popnow.ai/docs/openapi.yaml); do not add endpoints or
  fields that are not documented. Every request sends the package's `User-Agent`.
- Node types (`PopNow_<call name>`, `PopNowGenerate`, `PopNow_LoRA`) are stored in saved workflows: never
  rename them.
- After changing the bundled catalog, run `python scripts/render_docs.py`; a test fails when README.md or
  MODELS.md is stale.
- Write code, comments, docs and commit messages in English. Never commit API keys or real output links.

## Pull requests

1. Fork the repository and create a branch.
2. Add or update tests and run the suite.
3. Describe the change and link any related issue.
