<div align="center">
  <a href="https://popnow.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/popnow-ai/popnow-comfyui/main/assets/popnow-wordmark-light.png">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/popnow-ai/popnow-comfyui/main/assets/popnow-wordmark.png">
      <img alt="PopNow" src="https://raw.githubusercontent.com/popnow-ai/popnow-comfyui/main/assets/popnow-wordmark.png" width="260">
    </picture>
  </a>

  <h1>PopNow for ComfyUI: AI Video, Image and Music Generation Nodes</h1>

  <p><strong>popnow-comfyui</strong> is a ComfyUI custom node pack that runs every PopNow AI video, image and audio model (Kling, Seedance, Wan, MiniMax, Nano Banana, GPT Image, Flux, Suno and more) as a node in the cloud, with no GPU and no model downloads.</p>

  <p>
    <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
    <img alt="Python 3.10+" src="https://img.shields.io/badge/python-3.10%2B-3776AB.svg?logo=python&logoColor=white">
    <img alt="ComfyUI custom nodes" src="https://img.shields.io/badge/ComfyUI-custom%20nodes-222222.svg">
    <a href="https://github.com/popnow-ai/popnow-comfyui/actions/workflows/tests.yml"><img alt="Tests" src="https://github.com/popnow-ai/popnow-comfyui/actions/workflows/tests.yml/badge.svg"></a>
    <a href="https://popnow.ai"><img alt="Website: popnow.ai" src="https://img.shields.io/badge/site-popnow.ai-E65A2F.svg"></a>
    <a href="https://popnow.ai/docs/comfyui"><img alt="Docs" src="https://img.shields.io/badge/docs-popnow.ai%2Fdocs-111111.svg"></a>
  </p>
</div>

PopNow is a browser-based AI studio for videos, images and music: image-to-video, text-to-video, AI images,
music and speech, one-tap trending video effects and image styles. This pack brings its developer API
(`https://api.popnow.ai/api/v1`) into ComfyUI graphs. Each model is one node whose inputs come from that
model's published input schema, so the node offers exactly what the model accepts. Generation runs on
PopNow's servers and is paid in credits from the same wallet as popnow.ai (1 credit = $0.01; credit packs,
no subscription; failed runs are refunded). *Make it pop.*

<!-- stats:start -->
**248 model nodes** (115 video, 116 image, 17 audio) from 127 model families, plus **PopNow Generate** and **PopNow LoRA**.
<!-- stats:end -->

## Quickstart

1. **Install.** In **ComfyUI Manager**, search for **PopNow** and click **Install**, or use the
   [Comfy CLI](https://github.com/Comfy-Org/comfy-cli):

   ```bash
   comfy node install popnow-comfyui
   ```

2. **Add your key.** Create a key at [popnow.ai/api/console/keys](https://popnow.ai/api/console/keys), restart
   ComfyUI, open **Settings > PopNow** and paste it (or start ComfyUI with `POPNOW_API_KEY=sk-popnow-...` set).
   A notice shows your credit balance. Restart once more so the node list comes from your account.
3. **Add a node and run.** Double-click the canvas and type a model name (`seedance`, `kling`, `wan`,
   `minimax`, `nano banana`, `suno`...), or browse **PopNow > Video / Image / Audio**. Wire **Load Image**
   into its image input if it takes one, connect **Save Image**, **Save Video** or **Save Audio**, and queue.

Prefer a ready graph? Open ComfyUI's template browser and look under **popnow-comfyui**: text to image,
image to video, text to image to video, text to speech, LoRA, and PopNow Generate.

## Features

| | |
| --- | --- |
| What it adds | One node per PopNow model, a **PopNow Generate** node that takes any model by name, and a **PopNow LoRA** node |
| Inputs and outputs | Standard ComfyUI `IMAGE`, `MASK`, `VIDEO`, `AUDIO` and `STRING` |
| Hardware | None: models run on PopNow, so it works on laptops, Macs and CPU-only machines |
| Dependencies | None beyond ComfyUI itself (Python 3.10+, the V3 node API) |
| Pricing | Credits from your PopNow wallet; the rate is shown on every node and each run is quoted first |
| New models | Picked up automatically: the node list is rebuilt from your account's catalog at each start |
| License | MIT |

## Supported models

The node list follows the live PopNow catalog (`GET /api/v1/models`). At the time of this release:

<!-- models:start -->
### Video (115 nodes)

| Maker | Models |
| --- | --- |
| MiniMax | [MiniMax H3](https://popnow.ai/docs/models/minimax-h3), [MiniMax H3 Singularity LoRA](https://popnow.ai/docs/models/minimax-h3-singularity-lora), [MiniMax H3 Max](https://popnow.ai/docs/models/minimax-h3-max), [MiniMax H3 LoRA](https://popnow.ai/docs/models/minimax-h3-lora), [MiniMax H3 360 Orbit](https://popnow.ai/docs/models/minimax-h3-360-orbit) |
| ByteDance | [Seedance 2.5](https://popnow.ai/docs/models/seedance-2-5), [Seedance 2.0 Mini](https://popnow.ai/docs/models/seedance-2-0-mini), [Seedance 2.0](https://popnow.ai/docs/models/seedance-2-0), [Seedance 2.0 Fast](https://popnow.ai/docs/models/seedance-2-0-fast), [Seedance 1.5 Pro](https://popnow.ai/docs/models/seedance-1-5-pro) |
| Kuaishou | [Kling 3.0](https://popnow.ai/docs/models/kling-3-0), [Kling O3](https://popnow.ai/docs/models/kling-o3), [Kling 4.0](https://popnow.ai/docs/models/kling-4-0), [Kling 3.0 Turbo](https://popnow.ai/docs/models/kling-3-0-turbo), [Kling 2.6](https://popnow.ai/docs/models/kling-2-6), [Kling 2.5 Turbo](https://popnow.ai/docs/models/kling-2-5-turbo), [Kling 2.1 Master](https://popnow.ai/docs/models/kling-2-1-master), [Kling 2.1](https://popnow.ai/docs/models/kling-2-1) |
| Vidu | [Vidu Q4 Preview](https://popnow.ai/docs/models/vidu-q4-preview), [Vidu Q3 Turbo](https://popnow.ai/docs/models/vidu-q3-turbo), [Vidu Q3](https://popnow.ai/docs/models/vidu-q3), [Vidu Q3 Pro](https://popnow.ai/docs/models/vidu-q3-pro) |
| Alibaba | [Wan 3.0](https://popnow.ai/docs/models/wan-3-0), [Wan 3.0 Prime](https://popnow.ai/docs/models/wan-3-0-prime), [Wan 3.0 Pro Prime](https://popnow.ai/docs/models/wan-3-0-pro-prime), [Wan 3.0 Pro](https://popnow.ai/docs/models/wan-3-0-pro), [HappyHorse 1.1](https://popnow.ai/docs/models/happyhorse-1-1), [Wan 2.6 Flash](https://popnow.ai/docs/models/wan-2-6-flash), [Wan 2.6](https://popnow.ai/docs/models/wan-2-6), [Wan 2.5](https://popnow.ai/docs/models/wan-2-5), [Wan 2.2 Animate](https://popnow.ai/docs/models/wan-2-2-animate), [Wan 2.2 LoRA](https://popnow.ai/docs/models/wan-2-2-lora), [Wan 2.2](https://popnow.ai/docs/models/wan-2-2), [Wan 2.2 5B LoRA](https://popnow.ai/docs/models/wan-2-2-5b-lora), [Wan 2.1 LoRA](https://popnow.ai/docs/models/wan-2-1-lora) |
| Lightricks | [LTX 2.5](https://popnow.ai/docs/models/ltx-2-5), [LTX-2.3 LoRA](https://popnow.ai/docs/models/ltx-2-3-lora), [LTX-2 19B](https://popnow.ai/docs/models/ltx-2-19b), [LTX-2 19B LoRA](https://popnow.ai/docs/models/ltx-2-19b-lora) |
| Black Forest Labs | [FLUX 3](https://popnow.ai/docs/models/flux-3) |
| Tencent | [HunyuanVideo 1.5](https://popnow.ai/docs/models/hunyuan-video-1-5) |
| PopNow tools | [Video Upscaler](https://popnow.ai/docs/models/video-upscaler-v1) |

### Image (116 nodes)

| Maker | Models |
| --- | --- |
| Google | [Nano Banana 2.1](https://popnow.ai/docs/models/nano-banana-2-1), [Nano Banana Pro](https://popnow.ai/docs/models/nano-banana-pro), [Nano Banana 2](https://popnow.ai/docs/models/nano-banana-2) |
| OpenAI | [GPT Image 2.5 Sunburst](https://popnow.ai/docs/models/gpt-image-2-5-sunburst), [GPT Image 2.5 Flare](https://popnow.ai/docs/models/gpt-image-2-5-flare), [GPT Image 2](https://popnow.ai/docs/models/gpt-image-2) |
| ByteDance | [Seedream 5.0 Pro](https://popnow.ai/docs/models/seedream-5-0-pro), [Seedream 5.0 Flash](https://popnow.ai/docs/models/seedream-5-0-flash), [Seedream 5.0 Lite](https://popnow.ai/docs/models/seedream-5-0-lite), [Seedream 4.0](https://popnow.ai/docs/models/seedream-4-0) |
| Black Forest Labs | [FLUX.2 Max](https://popnow.ai/docs/models/flux-2-max), [FLUX 3 Klein Base LoRA](https://popnow.ai/docs/models/flux-3-klein-base-lora), [FLUX 3 Klein Base](https://popnow.ai/docs/models/flux-3-klein-base), [FLUX.2 Klein 9B LoRA](https://popnow.ai/docs/models/flux-2-klein-9b-lora), [FLUX.2 Klein Base 9B LoRA](https://popnow.ai/docs/models/flux-2-klein-base-9b-lora), [FLUX.2 Klein 4B LoRA](https://popnow.ai/docs/models/flux-2-klein-4b-lora), [FLUX.2 Klein Base 4B LoRA](https://popnow.ai/docs/models/flux-2-klein-base-4b-lora), [FLUX.2 Klein 9B](https://popnow.ai/docs/models/flux-2-klein-9b), [FLUX.2 Klein 4B](https://popnow.ai/docs/models/flux-2-klein-4b), [FLUX.2 Dev LoRA](https://popnow.ai/docs/models/flux-2-dev-lora), [FLUX.2 Pro](https://popnow.ai/docs/models/flux-2-pro), [FLUX.2 Flex](https://popnow.ai/docs/models/flux-2-flex), [FLUX.2 Dev](https://popnow.ai/docs/models/flux-2-dev), [FLUX.1 Krea Dev LoRA](https://popnow.ai/docs/models/flux-1-krea-dev-lora), [FLUX.1 Dev ControlNet LoRA](https://popnow.ai/docs/models/flux-1-dev-controlnet-lora), [FLUX.1 Fill Dev LoRA](https://popnow.ai/docs/models/flux-1-fill-dev-lora), [FLUX.1 Dev LoRA](https://popnow.ai/docs/models/flux-1-dev-lora), [FLUX.1 Schnell LoRA](https://popnow.ai/docs/models/flux-1-schnell-lora) |
| Alibaba | [Qwen Image 2.1 Pro](https://popnow.ai/docs/models/qwen-image-2-1-pro), [Qwen Image 2.1 Turbo](https://popnow.ai/docs/models/qwen-image-2-1-turbo), [Qwen Image 2.1](https://popnow.ai/docs/models/qwen-image-2-1), [Qwen Image 2.1 LoRA](https://popnow.ai/docs/models/qwen-image-2-1-lora), [Qwen Image 3.0 Pro](https://popnow.ai/docs/models/qwen-image-3-0-pro), [Qwen Image 3.0](https://popnow.ai/docs/models/qwen-image-3-0), [Wan 2.7 Pro](https://popnow.ai/docs/models/wan-2-7-pro), [Wan 2.7](https://popnow.ai/docs/models/wan-2-7), [Qwen Image 2](https://popnow.ai/docs/models/alibaba-qwen-image-2), [Z-Image Base LoRA](https://popnow.ai/docs/models/z-image-base-lora), [Qwen Image 2512 LoRA](https://popnow.ai/docs/models/qwen-image-2512-lora), [Z-Image](https://popnow.ai/docs/models/z-image), [Z-Image Turbo LoRA](https://popnow.ai/docs/models/z-image-turbo-lora), [Qwen Image Edit 2509 LoRA](https://popnow.ai/docs/models/qwen-image-edit-2509-lora), [Qwen Image 1.0 LoRA](https://popnow.ai/docs/models/qwen-image-1-0-lora), [Wan 2.2 Image LoRA](https://popnow.ai/docs/models/wan-2-2-image-lora), [Wan 2.1 Image LoRA](https://popnow.ai/docs/models/wan-2-1-image-lora) |
| Krea | [Krea 3](https://popnow.ai/docs/models/krea-3), [Krea 2 Turbo LoRA](https://popnow.ai/docs/models/krea-2-turbo-lora), [Krea 2 Large](https://popnow.ai/docs/models/krea-2-large), [Krea 2 Medium](https://popnow.ai/docs/models/krea-2-medium), [Krea 2 Medium Turbo](https://popnow.ai/docs/models/krea-2-medium-turbo) |
| MiniMax | [MiniMax H3 Image LoRA](https://popnow.ai/docs/models/minimax-h3-image-lora) |
| CircleStone Labs | [Anima Turbo](https://popnow.ai/docs/models/anima-turbo), [Anima Turbo LoRA](https://popnow.ai/docs/models/anima-turbo-lora) |
| Pruna AI | [P-Image LoRA](https://popnow.ai/docs/models/p-image-lora) |
| J1B | [Jib Mix Qwen](https://popnow.ai/docs/models/jib-mix-qwen-image), [Jib Mix Qwen LoRA](https://popnow.ai/docs/models/jib-mix-qwen-image-lora) |
| Prefect | [Prefect Pony XL LoRA](https://popnow.ai/docs/models/prefect-pony-xl-lora), [Prefect Pony XL](https://popnow.ai/docs/models/prefect-pony-xl) |
| Neta.art Lab | [Neta Lumina](https://popnow.ai/docs/models/neta-lumina) |
| PopNow tools | [Background Remover](https://popnow.ai/docs/models/background-remover-v1), [Image Upscaler](https://popnow.ai/docs/models/image-upscaler-v1), [Object Eraser](https://popnow.ai/docs/models/object-eraser-v1), [Image Expander](https://popnow.ai/docs/models/image-expander-v1), [Shadow Remover](https://popnow.ai/docs/models/shadow-remover-v1), [Pose Changer](https://popnow.ai/docs/models/pose-changer-v1), [Anime to Real](https://popnow.ai/docs/models/anime-to-real-v1), [Camera Angle Changer](https://popnow.ai/docs/models/camera-angle-changer-v1), [Relight](https://popnow.ai/docs/models/relight-v1) |

### Audio (17 nodes)

| Maker | Models |
| --- | --- |
| Suno | [Suno v6](https://popnow.ai/docs/models/suno-v6), [Suno v6 Mini](https://popnow.ai/docs/models/suno-v6-mini), [Suno v6 Wild](https://popnow.ai/docs/models/suno-v6-wild) |
| Google | [Gemini 3.8 Flash TTS](https://popnow.ai/docs/models/gemini-3-8-flash-tts), [Gemini 3.8 Flash-Lite TTS](https://popnow.ai/docs/models/gemini-3-8-flash-lite-tts), [Gemini 2.5 Pro TTS](https://popnow.ai/docs/models/gemini-2-5-pro-tts) |
| MiniMax | [MiniMax Speech 2.8 HD](https://popnow.ai/docs/models/minimax-speech-2-8-hd), [MiniMax Music 3.0](https://popnow.ai/docs/models/minimax-music-3-0), [MiniMax Speech 2.8 Turbo](https://popnow.ai/docs/models/minimax-speech-2-8-turbo) |
| ByteDance | [Seed Audio 1.0](https://popnow.ai/docs/models/seed-audio-1-0), [Seed Speech 2.0](https://popnow.ai/docs/models/seed-speech-2-0) |
| HeartMuLa | [HeartMuLa Transcribe](https://popnow.ai/docs/models/heartmula-transcribe) |
| xAI | [Grok STT](https://popnow.ai/docs/models/grok-stt), [Grok TTS](https://popnow.ai/docs/models/grok-tts) |
| Alibaba | [Qwen3 TTS](https://popnow.ai/docs/models/qwen-3-tts) |
| Resemble AI | [Chatterbox](https://popnow.ai/docs/models/chatterbox-v1) |
| PopNow tools | [Video Sound Effects](https://popnow.ai/docs/models/foley-v1) |

Every node with its call name and starting price: [MODELS.md](MODELS.md).
<!-- models:end -->

## Install

The pack is on the [Comfy Registry](https://registry.comfy.org/nodes/popnow-comfyui) as `popnow-comfyui`. There
is nothing else to install: the nodes only use packages ComfyUI already ships.

**ComfyUI Manager.** Open **Manager > Custom Nodes Manager**, search for **PopNow**, click **Install** and restart
ComfyUI.

**Comfy CLI.** `comfy node install popnow-comfyui`

**git.**

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/popnow-ai/popnow-comfyui
# later, to update:
cd popnow-comfyui && git pull
```

**ZIP.** Download [main.zip](https://github.com/popnow-ai/popnow-comfyui/archive/refs/heads/main.zip), unpack it
into `ComfyUI/custom_nodes`, and restart.

Used the single-file node from [popnow.ai/docs/comfyui](https://popnow.ai/docs/comfyui) before? Delete
`custom_nodes/popnow_api.py` when you install this pack. Its **PopNow Generate** node is the same node type
with the same inputs, so saved workflows keep working.

## How the nodes work

- **Inputs follow the model.** Dropdowns, sliders and switches mirror each model's schema. Image, video and
  audio inputs are sockets, uploaded for you when the node runs (`popnow://f/...` files that only your key can
  use). Models that take several references grow a new socket each time you connect one.
- **Defaults are the model's own.** A dropdown set to `model default`, or a number set to `-1`, is left out
  of the request so the model decides.
- **Outputs are ordinary ComfyUI values.** Video nodes return `VIDEO` (and the last frame as `IMAGE` when
  `return_last_frame` is on), audio nodes return `AUDIO`, image nodes return `IMAGE`, and background removal
  and layer decomposition also return an `alpha` mask. Transcription returns `STRING`. Every node also
  returns its `task id`.
- **Progress on the node.** The node shows the estimate, the queue and generation time, and finally what
  the run was charged.

### PopNow Generate

One node for any model, the same node as the single-file version on popnow.ai:

| Input | What to put in it |
| --- | --- |
| `model` | A call name from [popnow.ai/docs/models](https://popnow.ai/docs/models), for example `minimax/h3/image-to-video` |
| `prompt` | What to make. It goes into `prompt` (or `text` for speech models) unless `options` already sets it |
| `options` | The model's other fields as JSON, such as `{"resolution": "2k"}` or `{"duration_seconds": 5}` |
| `image` (optional) | An `IMAGE`, uploaded and placed in the field named by `image_field` |
| `image_field` | `image_url` for most video models, `image_urls` for image editing (a list; every image in the batch is sent) |

Outputs: `image` (the result for image models, a blank placeholder otherwise), `url` (the signed file URL,
valid for about 20 minutes) and `path` (video and audio are saved to `ComfyUI/output/popnow_<task>.mp4` and
similar). Load a saved video back with a video loader node to get its frames.

### PopNow LoRA

LoRA models (their names end in `LoRA`) take a `loras` input. Add a **PopNow LoRA** node, set its `source`
and `scale`, and connect it; chain several to stack them (most accept up to three). `source` can be:

| Source | What happens |
| --- | --- |
| A file in `ComfyUI/models/loras`, such as `my_style.safetensors` | Uploaded once (up to 2 GiB) and reused for 12 hours |
| A Hugging Face repo id (`owner/repo`) or page, or a Civitai page | PopNow downloads it once with `POST /api/v1/files/import`; set `HF_TOKEN` or `CIVITAI_API_KEY` in ComfyUI's environment for gated files |
| Any other direct `https://` link, or a `popnow://f/...` URI | Sent as is |

Tokens are read from the environment only, never from a widget: widget values are saved in every workflow
and image you share.

## Costs and safety

- **Price on the node.** Each node's badge shows the current rate for the options you picked, for example
  `5.55 cr/s` for MiniMax H3 at 768p or `7.2 cr/image` for Nano Banana 2.1, and updates as you change them.
  `~` marks models whose final charge depends on the output.
- **Quote before every run.** Each run calls `jobs/quote` first and holds at most the quoted amount. Set
  **Settings > PopNow > Max credits per run** and any run quoted above it stops before anything is held.
- **No surprise re-runs.** Seeds start on `fixed`, so queueing the same graph twice reuses the first result.
  Switch **control after generate** to `randomize` for a new result each run (each run is billed).
- **Safe retries.** Every task is submitted with an `Idempotency-Key`; network retries reuse it, so a retry
  never creates a second task.
- **Your key stays out of shared files.** It is stored in the ComfyUI user folder
  (`user/popnow/config.json`, readable by your account only), never in a workflow or in image metadata. On a
  server, set `POPNOW_API_KEY` instead.
- **Cancelling stops the wait, not the job.** A cancelled run keeps going on PopNow, is charged if it
  succeeds, and its result stays in the [API console](https://popnow.ai/api/console) logs.

## Configuration

| Setting | Where | Purpose |
| --- | --- | --- |
| `POPNOW_API_KEY` | environment | API key (`sk-popnow-...`); takes precedence over the key saved in Settings |
| Settings > PopNow > API key | ComfyUI settings | Saves the key to `user/popnow/config.json` |
| Settings > PopNow > Max credits per run | ComfyUI settings | Spending ceiling per node run (0 = no limit) |
| `POPNOW_BASE_URL` | environment | API origin, default `https://api.popnow.ai` (for testing against a mock) |
| `POPNOW_COMFYUI_HOME` | environment | Folder for the saved key and catalog cache, instead of `user/popnow` |
| `HF_TOKEN`, `CIVITAI_API_KEY` | environment | Used once per LoRA import of a gated file; never stored |
| `HTTPS_PROXY` | environment | Honoured for every request |

## Troubleshooting

| You see | What to do |
| --- | --- |
| `No PopNow API key is set` | Add the key in Settings > PopNow, or set `POPNOW_API_KEY`, then run again |
| `PopNow 401` | The key is missing, mistyped or revoked; create a new one in the API console |
| `PopNow 400` naming a field | A value the model does not accept; check the model page linked in the node's description |
| `PopNow 40201` | Not enough credits: [buy credits](https://popnow.ai/pricing), or lower the resolution or length |
| `PopNow 40004` | The model cannot serve that combination of settings; change the one named in the message |
| `PopNow 40310` | Verify your email address with the link from your sign-up email |
| `PopNow content_rejected` / `generation_failed` | The model declined or could not finish; failed runs are refunded |
| An error ending in `request_id ...` | Send that id to [support](https://popnow.ai/contact); it identifies the request exactly |
| `a proxy or firewall ... may be intercepting the request` | Check that `HTTPS_PROXY`, if set, points at a working proxy |
| A model from popnow.ai is missing | Restart ComfyUI: the node list is built from your account's catalog at start |

## FAQ

### How do I generate a video from an image in ComfyUI without a GPU?

Install this pack and add your PopNow key, then add an image-to-video node such as **MiniMax H3 · Image to
Video**, **Kling 3.0 · Image to Video** or **Seedance 2.5 · Image to Video**. Connect **Load Image** to its
`image_url` input and **Save Video** to its `video` output, write a prompt and queue. The model runs on
PopNow's servers, so your machine only uploads the picture and downloads the clip.

### How do I use Kling, Seedance or Wan in ComfyUI?

Each of them is a set of nodes under **PopNow > Video** (one per task: text to video, image to video,
reference to video, video extend). Search the node list for the model name. Resolution, duration, audio and
the other options are widgets on the node, with the price for your settings on its badge.

### How much does a run cost?

Each model has its own rate in credits (1 credit = $0.01), shown on the node and in
[MODELS.md](MODELS.md): image models are priced per image, video models per second of output, speech per
1,000 characters or per request. Every run is quoted before it starts, the node prints the final charge
when it finishes, and failed runs are refunded. Prices: [popnow.ai/pricing](https://popnow.ai/pricing).

### Is my API key safe when I share a workflow or an image?

Yes. ComfyUI writes node settings into workflow files and PNG metadata, so the key is never a node setting.
It lives in a file in your ComfyUI user folder, or in the `POPNOW_API_KEY` environment variable.

### Can I use my own LoRA with a cloud model?

Yes, with the LoRA model nodes. Point a **PopNow LoRA** node at a `.safetensors` file in
`ComfyUI/models/loras`, a Hugging Face repo, a Civitai page or a direct link, and connect it to the model
node's `loras` input. The **lora** template comes ready to run with an Apache-2.0 pixel-art LoRA for Z-Image
Turbo (by tarn59 on Hugging Face).

### Can I call a model that has no node yet?

Yes. **PopNow Generate** takes any call name from [popnow.ai/docs/models](https://popnow.ai/docs/models) plus
its options as JSON. New models also get their own node after a restart once your key is set.

### Does it work with ComfyUI Desktop, portable builds or a remote server?

Yes, anywhere ComfyUI can load custom nodes and reach `api.popnow.ai`. On a server, set `POPNOW_API_KEY` in
its environment or enter the key in Settings from the browser. Proxies set through `HTTPS_PROXY` are used.

## Links

- Website: [popnow.ai](https://popnow.ai) · Pricing: [popnow.ai/pricing](https://popnow.ai/pricing)
- Docs: [popnow.ai/docs](https://popnow.ai/docs) · ComfyUI guide: [popnow.ai/docs/comfyui](https://popnow.ai/docs/comfyui)
- API reference: [OpenAPI spec](https://popnow.ai/docs/openapi.yaml) · Models: [popnow.ai/docs/models](https://popnow.ai/docs/models)
- MCP server for AI assistants: [popnow.ai/mcp](https://popnow.ai/mcp)
- Other PopNow repositories: [popnow-mcp](https://github.com/popnow-ai/popnow-mcp),
  [popnow-skills](https://github.com/popnow-ai/popnow-skills), [popnow-python](https://github.com/popnow-ai/popnow-python),
  [popnow-js](https://github.com/popnow-ai/popnow-js), [popnow-api](https://github.com/popnow-ai/popnow-api),
  [popnow-blender](https://github.com/popnow-ai/popnow-blender), [n8n-nodes-popnow](https://github.com/popnow-ai/n8n-nodes-popnow),
  [popnow-cli](https://github.com/popnow-ai/popnow-cli), [popnow-go](https://github.com/popnow-ai/popnow-go),
  [popnow-php](https://github.com/popnow-ai/popnow-php)

## Development

The tests need only `aiohttp`; ComfyUI, torch and the network are replaced by local stubs and a fake API.

```bash
python -m pip install aiohttp
python -m unittest discover -s tests -t .
python scripts/update_snapshot.py --public   # refresh the bundled model list from public popnow.ai pages
python scripts/render_docs.py                # rewrite the model lists in README.md and MODELS.md
```

`POPNOW_API_KEY=sk-popnow-... python scripts/update_snapshot.py` refreshes the snapshot from the
authenticated `GET /api/v1/models?includeSchema=1` instead. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE) © PopNow
