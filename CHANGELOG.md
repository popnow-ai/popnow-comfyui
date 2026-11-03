# Changelog

## 0.3.0 — 2026-11-03

- Refresh all media and embedding model schemas and exact USD rates from the current API catalog.
- Add reproducible offline catalog snapshot updates.

## 0.2.0 - 2026-11-01

The PopNow API bills in US dollars from its own API balance, separate from popnow.ai website credits.
This release follows it everywhere.

- Price badges, node descriptions and MODELS.md show USD rates (`$0.037/s`, `$0.048/image`) from the
  catalog's `usd` rate table. A catalog cached by 0.1 (credit rates only) is converted, so it still shows a
  price.
- Each run confirms the quote in USD: `createTask` gets `expectedCostUsd` (the quote's `maxChargeUsd`)
  with the `quoteId`, instead of the deprecated `expectedCredits`. The node shows the estimated and the
  charged amount in USD (`expectedChargeUsd`, `costUsd`).
- The spending limit is now **Settings > PopNow > Max USD per run** (`maxUsdPerRun`). A limit saved in
  credits (`maxCreditsPerRun`) keeps applying at 1 credit = $0.001 until a USD limit is saved, and the
  settings route still accepts it. Saved workflows are unaffected: no node input changed.
- The key check shows the API balance in USD (`availableUsd`). Error 40201 points to adding funds in the API
  console.
- The bundled catalog snapshot is refreshed (305 models) and stores USD rates.
- Links point to the developer MCP server (popnow.ai/api/mcp, popnow-api-mcp) and developer skills
  (popnow.ai/api/skills).
- Deprecated, still working: `pricing.format_credits`, `pricing.format_usd` (credit input),
  `config.get_max_credits_per_run`, `config.save_max_credits_per_run`, and the `expected_credits` argument of
  `PopNowClient.create_task`.

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
