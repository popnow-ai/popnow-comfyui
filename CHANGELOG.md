# Changelog

## 0.1.0

First release.

- One node per PopNow image, video and audio model, generated from the live catalog
  (`GET /api/v1/models?includeSchema=1`) at startup, with a bundled snapshot for the first run before a
  key is set.
- Inputs follow each model's published schema: dropdowns, sliders, switches, image, video and audio
  sockets, growable groups for multi-reference models, and a LoRA socket.
- A credit price badge on every node, updated as the options change.
- A quote before every run, an optional per-run credit limit, and the charged credits on the node when it
  finishes.
- **PopNow Generate**: any model by call name with JSON options, the same node type and inputs as the
  single-file node on popnow.ai.
- **PopNow LoRA**: LoRA files from `ComfyUI/models/loras` (uploaded), Hugging Face or Civitai (imported by
  PopNow), or any direct link; chain several to stack them.
- The API key is kept in the ComfyUI user folder or `POPNOW_API_KEY`, never in workflows or image metadata.
- Example workflows: text to image, image to video, text to image to video, text to speech, LoRA and
  PopNow Generate.
