# PopNow models available as ComfyUI nodes

344 PopNow models, one ComfyUI node each: 172 video, 139 image and 30 audio and 3 text/vector models. Any of them can also be called by name from the **PopNow Generate** node.

The list is generated from the model catalog bundled with this release. ComfyUI loads the live catalog at startup once an API key is set, so models added since then appear after a restart.
Prices are starting rates in US dollars, paid from your PopNow API balance; the badge on each node shows the rate for the options you pick, and every run is quoted before anything is held.

## Video

| Node | Call name | From | Node type |
| --- | --- | --- | --- |
| [HappyHorse 1.1 · image-to-video](https://popnow.ai/docs/models/happyhorse-1-1) | `alibaba/happyhorse-1.1/image-to-video` | $0.14 / second | `PopNow_alibaba_happyhorse_1_1_image_to_video` |
| [HappyHorse 1.1 · reference-to-video](https://popnow.ai/docs/models/happyhorse-1-1) | `alibaba/happyhorse-1.1/reference-to-video` | $0.14 / second | `PopNow_alibaba_happyhorse_1_1_reference_to_video` |
| [HappyHorse 1.1 · text-to-video](https://popnow.ai/docs/models/happyhorse-1-1) | `alibaba/happyhorse-1.1/text-to-video` | $0.14 / second | `PopNow_alibaba_happyhorse_1_1_text_to_video` |
| [Wan 2.1 LoRA · image-to-video](https://popnow.ai/docs/models/wan-2-1-lora) | `alibaba/wan-2.1-lora/image-to-video` | $0.24 / run | `PopNow_alibaba_wan_2_1_lora_image_to_video` |
| [Wan 2.1 LoRA · text-to-video](https://popnow.ai/docs/models/wan-2-1-lora) | `alibaba/wan-2.1-lora/text-to-video` | $0.24 / run | `PopNow_alibaba_wan_2_1_lora_text_to_video` |
| [Wan 2.1 LoRA · video-edit](https://popnow.ai/docs/models/wan-2-1-lora) | `alibaba/wan-2.1-lora/video-edit` | $0.24 / run | `PopNow_alibaba_wan_2_1_lora_video_edit` |
| [Wan 2.2 5B LoRA · image-to-video](https://popnow.ai/docs/models/wan-2-2-5b-lora) | `alibaba/wan-2.2-5b-lora/image-to-video` | $0.12 / run | `PopNow_alibaba_wan_2_2_5b_lora_image_to_video` |
| [Wan 2.2 5B LoRA · text-to-video](https://popnow.ai/docs/models/wan-2-2-5b-lora) | `alibaba/wan-2.2-5b-lora/text-to-video` | $0.12 / run | `PopNow_alibaba_wan_2_2_5b_lora_text_to_video` |
| [Wan 2.2 Animate · character-animation](https://popnow.ai/docs/models/wan-2-2-animate) | `alibaba/wan-2.2-animate/character-animation` | $0.053 / second | `PopNow_alibaba_wan_2_2_animate_character_animation` |
| [Wan 2.2 LoRA · image-to-video](https://popnow.ai/docs/models/wan-2-2-lora) | `alibaba/wan-2.2-lora/image-to-video` | $0.024 / second | `PopNow_alibaba_wan_2_2_lora_image_to_video` |
| [Wan 2.2 LoRA · text-to-video](https://popnow.ai/docs/models/wan-2-2-lora) | `alibaba/wan-2.2-lora/text-to-video` | $0.048 / second | `PopNow_alibaba_wan_2_2_lora_text_to_video` |
| [Wan 2.2 LoRA · video-extend](https://popnow.ai/docs/models/wan-2-2-lora) | `alibaba/wan-2.2-lora/video-extend` | $0.024 / second | `PopNow_alibaba_wan_2_2_lora_video_extend` |
| [Wan 2.2 · image-to-video](https://popnow.ai/docs/models/wan-2-2) | `alibaba/wan-2.2/image-to-video` | $0.24 / run | `PopNow_alibaba_wan_2_2_image_to_video` |
| [Wan 2.2 · text-to-video](https://popnow.ai/docs/models/wan-2-2) | `alibaba/wan-2.2/text-to-video` | $0.24 / run | `PopNow_alibaba_wan_2_2_text_to_video` |
| [Wan 2.5 · image-to-video](https://popnow.ai/docs/models/wan-2-5) | `alibaba/wan-2.5/image-to-video` | $0.045 / second | `PopNow_alibaba_wan_2_5_image_to_video` |
| [Wan 2.5 · text-to-video](https://popnow.ai/docs/models/wan-2-5) | `alibaba/wan-2.5/text-to-video` | $0.045 / second | `PopNow_alibaba_wan_2_5_text_to_video` |
| [Wan 2.5 · video-extend](https://popnow.ai/docs/models/wan-2-5) | `alibaba/wan-2.5/video-extend` | $0.045 / second | `PopNow_alibaba_wan_2_5_video_extend` |
| [Wan 2.6 Flash · image-to-video](https://popnow.ai/docs/models/wan-2-6-flash) | `alibaba/wan-2.6-flash/image-to-video` | $0.0225 / second | `PopNow_alibaba_wan_2_6_flash_image_to_video` |
| [Wan 2.6 Flash · reference-to-video](https://popnow.ai/docs/models/wan-2-6-flash) | `alibaba/wan-2.6-flash/reference-to-video` | $0.0225 / second | `PopNow_alibaba_wan_2_6_flash_reference_to_video` |
| [Wan 2.6 · image-to-video](https://popnow.ai/docs/models/wan-2-6) | `alibaba/wan-2.6/image-to-video` | $0.09 / second | `PopNow_alibaba_wan_2_6_image_to_video` |
| [Wan 2.6 · reference-to-video](https://popnow.ai/docs/models/wan-2-6) | `alibaba/wan-2.6/reference-to-video` | $0.065 / second | `PopNow_alibaba_wan_2_6_reference_to_video` |
| [Wan 2.6 · text-to-video](https://popnow.ai/docs/models/wan-2-6) | `alibaba/wan-2.6/text-to-video` | $0.09 / second | `PopNow_alibaba_wan_2_6_text_to_video` |
| [Wan 3.0 Prime · image-to-video](https://popnow.ai/docs/models/wan-3-0-prime) | `alibaba/wan-3.0-prime/image-to-video` | $0.0612 / second | `PopNow_alibaba_wan_3_0_prime_image_to_video` |
| [Wan 3.0 Prime · reference-to-video](https://popnow.ai/docs/models/wan-3-0-prime) | `alibaba/wan-3.0-prime/reference-to-video` | $0.0612 / second | `PopNow_alibaba_wan_3_0_prime_reference_to_video` |
| [Wan 3.0 Prime · text-to-video](https://popnow.ai/docs/models/wan-3-0-prime) | `alibaba/wan-3.0-prime/text-to-video` | $0.0612 / second | `PopNow_alibaba_wan_3_0_prime_text_to_video` |
| [Wan 3.0 Prime · video-extend](https://popnow.ai/docs/models/wan-3-0-prime) | `alibaba/wan-3.0-prime/video-extend` | $0.0612 / second | `PopNow_alibaba_wan_3_0_prime_video_extend` |
| [Wan 3.0 Pro Prime · image-to-video](https://popnow.ai/docs/models/wan-3-0-pro-prime) | `alibaba/wan-3.0-pro-prime/image-to-video` | $0.234 / second | `PopNow_alibaba_wan_3_0_pro_prime_image_to_video` |
| [Wan 3.0 Pro Prime · reference-to-video](https://popnow.ai/docs/models/wan-3-0-pro-prime) | `alibaba/wan-3.0-pro-prime/reference-to-video` | $0.234 / second | `PopNow_alibaba_wan_3_0_pro_prime_reference_to_video` |
| [Wan 3.0 Pro Prime · text-to-video](https://popnow.ai/docs/models/wan-3-0-pro-prime) | `alibaba/wan-3.0-pro-prime/text-to-video` | $0.234 / second | `PopNow_alibaba_wan_3_0_pro_prime_text_to_video` |
| [Wan 3.0 Pro Prime · video-extend](https://popnow.ai/docs/models/wan-3-0-pro-prime) | `alibaba/wan-3.0-pro-prime/video-extend` | $0.234 / second | `PopNow_alibaba_wan_3_0_pro_prime_video_extend` |
| [Wan 3.0 Pro · image-to-video](https://popnow.ai/docs/models/wan-3-0-pro) | `alibaba/wan-3.0-pro/image-to-video` | $0.144 / second | `PopNow_alibaba_wan_3_0_pro_image_to_video` |
| [Wan 3.0 Pro · reference-to-video](https://popnow.ai/docs/models/wan-3-0-pro) | `alibaba/wan-3.0-pro/reference-to-video` | $0.144 / second | `PopNow_alibaba_wan_3_0_pro_reference_to_video` |
| [Wan 3.0 Pro · text-to-video](https://popnow.ai/docs/models/wan-3-0-pro) | `alibaba/wan-3.0-pro/text-to-video` | $0.144 / second | `PopNow_alibaba_wan_3_0_pro_text_to_video` |
| [Wan 3.0 Pro · video-extend](https://popnow.ai/docs/models/wan-3-0-pro) | `alibaba/wan-3.0-pro/video-extend` | $0.144 / second | `PopNow_alibaba_wan_3_0_pro_video_extend` |
| [Wan 3.0 · image-to-video](https://popnow.ai/docs/models/wan-3-0) | `alibaba/wan-3.0/image-to-video` | $0.045 / second | `PopNow_alibaba_wan_3_0_image_to_video` |
| [Wan 3.0 · reference-to-video](https://popnow.ai/docs/models/wan-3-0) | `alibaba/wan-3.0/reference-to-video` | $0.045 / second | `PopNow_alibaba_wan_3_0_reference_to_video` |
| [Wan 3.0 · text-to-video](https://popnow.ai/docs/models/wan-3-0) | `alibaba/wan-3.0/text-to-video` | $0.045 / second | `PopNow_alibaba_wan_3_0_text_to_video` |
| [Wan 3.0 · video-extend](https://popnow.ai/docs/models/wan-3-0) | `alibaba/wan-3.0/video-extend` | $0.045 / second | `PopNow_alibaba_wan_3_0_video_extend` |
| [FLUX 3 · image-to-video](https://popnow.ai/docs/models/flux-3) | `black-forest-labs/flux-3/image-to-video` | $0.06 / second | `PopNow_black_forest_labs_flux_3_image_to_video` |
| [FLUX 3 · text-to-video](https://popnow.ai/docs/models/flux-3) | `black-forest-labs/flux-3/text-to-video` | $0.06 / second | `PopNow_black_forest_labs_flux_3_text_to_video` |
| [FLUX 3 · upscale](https://popnow.ai/docs/models/flux-3) | `black-forest-labs/flux-3/upscale` | $0.528 / second | `PopNow_black_forest_labs_flux_3_upscale` |
| [FLUX 3 · video-extend](https://popnow.ai/docs/models/flux-3) | `black-forest-labs/flux-3/video-extend` | $0.12 / second | `PopNow_black_forest_labs_flux_3_video_extend` |
| [OmniHuman 2.0 · talking-avatar](https://popnow.ai/docs/models/omnihuman-2-0) | `bytedance/omnihuman-2.0/talking-avatar` | $0.1084 / second | `PopNow_bytedance_omnihuman_2_0_talking_avatar` |
| [SeedVR2 Video · upscale](https://popnow.ai/docs/models/seedvr2-video) | `bytedance/seedvr2-video/upscale` | $0.024 / second | `PopNow_bytedance_seedvr2_video_upscale` |
| [Seedance 2.0 Fast · image-to-video](https://popnow.ai/docs/models/seedance-2-0-fast) | `bytedance/seedance-2.0-fast/image-to-video` | $0.04499712 / second | `PopNow_bytedance_seedance_2_0_fast_image_to_video` |
| [Seedance 2.0 Fast · reference-to-video](https://popnow.ai/docs/models/seedance-2-0-fast) | `bytedance/seedance-2.0-fast/reference-to-video` | $0.022539 / second | `PopNow_bytedance_seedance_2_0_fast_reference_to_video` |
| [Seedance 2.0 Fast · text-to-video](https://popnow.ai/docs/models/seedance-2-0-fast) | `bytedance/seedance-2.0-fast/text-to-video` | $0.04499712 / second | `PopNow_bytedance_seedance_2_0_fast_text_to_video` |
| [Seedance 2.0 Fast · video-extend](https://popnow.ai/docs/models/seedance-2-0-fast) | `bytedance/seedance-2.0-fast/video-extend` | $0.04499712 / second | `PopNow_bytedance_seedance_2_0_fast_video_extend` |
| [Seedance 2.0 Mini · image-to-video](https://popnow.ai/docs/models/seedance-2-0-mini) | `bytedance/seedance-2.0-mini/image-to-video` | $0.0246078 / second | `PopNow_bytedance_seedance_2_0_mini_image_to_video` |
| [Seedance 2.0 Mini · reference-to-video](https://popnow.ai/docs/models/seedance-2-0-mini) | `bytedance/seedance-2.0-mini/reference-to-video` | $0.010969 / second | `PopNow_bytedance_seedance_2_0_mini_reference_to_video` |
| [Seedance 2.0 Mini · text-to-video](https://popnow.ai/docs/models/seedance-2-0-mini) | `bytedance/seedance-2.0-mini/text-to-video` | $0.0246078 / second | `PopNow_bytedance_seedance_2_0_mini_text_to_video` |
| [Seedance 2.0 Mini · video-extend](https://popnow.ai/docs/models/seedance-2-0-mini) | `bytedance/seedance-2.0-mini/video-extend` | $0.0246078 / second | `PopNow_bytedance_seedance_2_0_mini_video_extend` |
| [Seedance 2.0 · image-to-video](https://popnow.ai/docs/models/seedance-2-0) | `bytedance/seedance-2.0/image-to-video` | $0.0721 / second | `PopNow_bytedance_seedance_2_0_image_to_video` |
| [Seedance 2.0 · reference-to-video](https://popnow.ai/docs/models/seedance-2-0) | `bytedance/seedance-2.0/reference-to-video` | $0.043531 / second | `PopNow_bytedance_seedance_2_0_reference_to_video` |
| [Seedance 2.0 · text-to-video](https://popnow.ai/docs/models/seedance-2-0) | `bytedance/seedance-2.0/text-to-video` | $0.0728 / second | `PopNow_bytedance_seedance_2_0_text_to_video` |
| [Seedance 2.0 · video-extend](https://popnow.ai/docs/models/seedance-2-0) | `bytedance/seedance-2.0/video-extend` | $0.0735 / second | `PopNow_bytedance_seedance_2_0_video_extend` |
| [Seedance 2.5 · image-to-video](https://popnow.ai/docs/models/seedance-2-5) | `bytedance/seedance-2.5/image-to-video` | $0.1234 / second | `PopNow_bytedance_seedance_2_5_image_to_video` |
| [Seedance 2.5 · reference-to-video](https://popnow.ai/docs/models/seedance-2-5) | `bytedance/seedance-2.5/reference-to-video` | $0.0738 / second | `PopNow_bytedance_seedance_2_5_reference_to_video` |
| [Seedance 2.5 · text-to-video](https://popnow.ai/docs/models/seedance-2-5) | `bytedance/seedance-2.5/text-to-video` | $0.1234 / second | `PopNow_bytedance_seedance_2_5_text_to_video` |
| [Seedance 2.5 · video-extend](https://popnow.ai/docs/models/seedance-2-5) | `bytedance/seedance-2.5/video-extend` | $0.0738 / second | `PopNow_bytedance_seedance_2_5_video_extend` |
| [OpenJutsu Character Swap · video-edit](https://popnow.ai/docs/models/openjutsu-character-swap) | `comfyui/openjutsu-character-swap/video-edit` | $0.105 / second | `PopNow_comfyui_openjutsu_character_swap_video_edit` |
| [OpenJutsu Object Swap · video-edit](https://popnow.ai/docs/models/openjutsu-object-swap) | `comfyui/openjutsu-object-swap/video-edit` | $0.105 / second | `PopNow_comfyui_openjutsu_object_swap_video_edit` |
| [Gemini Omni 1.1 Flash · image-to-video](https://popnow.ai/docs/models/gemini-omni-1-1-flash) | `google/gemini-omni-1.1-flash/image-to-video` | $0.3648 / run | `PopNow_google_gemini_omni_1_1_flash_image_to_video` |
| [Gemini Omni 1.1 Flash · reference-to-video](https://popnow.ai/docs/models/gemini-omni-1-1-flash) | `google/gemini-omni-1.1-flash/reference-to-video` | $0.3648 / run | `PopNow_google_gemini_omni_1_1_flash_reference_to_video` |
| [Gemini Omni 1.1 Flash · text-to-video](https://popnow.ai/docs/models/gemini-omni-1-1-flash) | `google/gemini-omni-1.1-flash/text-to-video` | $0.3648 / run | `PopNow_google_gemini_omni_1_1_flash_text_to_video` |
| [Veo 3.1 Fast · image-to-video](https://popnow.ai/docs/models/veo-3-1-fast) | `google/veo-3.1-fast/image-to-video` | $0.36 / run | `PopNow_google_veo_3_1_fast_image_to_video` |
| [Veo 3.1 Fast · reference-to-video](https://popnow.ai/docs/models/veo-3-1-fast) | `google/veo-3.1-fast/reference-to-video` | $0.72 / run | `PopNow_google_veo_3_1_fast_reference_to_video` |
| [Veo 3.1 Fast · text-to-video](https://popnow.ai/docs/models/veo-3-1-fast) | `google/veo-3.1-fast/text-to-video` | $0.36 / run | `PopNow_google_veo_3_1_fast_text_to_video` |
| [Veo 3.1 Fast · video-extend](https://popnow.ai/docs/models/veo-3-1-fast) | `google/veo-3.1-fast/video-extend` | $0.36 / run | `PopNow_google_veo_3_1_fast_video_extend` |
| [Veo 3.1 Lite · image-to-video](https://popnow.ai/docs/models/veo-3-1-lite) | `google/veo-3.1-lite/image-to-video` | $0.18 / run | `PopNow_google_veo_3_1_lite_image_to_video` |
| [Veo 3.1 Lite · reference-to-video](https://popnow.ai/docs/models/veo-3-1-lite) | `google/veo-3.1-lite/reference-to-video` | $0.36 / run | `PopNow_google_veo_3_1_lite_reference_to_video` |
| [Veo 3.1 Lite · text-to-video](https://popnow.ai/docs/models/veo-3-1-lite) | `google/veo-3.1-lite/text-to-video` | $0.18 / run | `PopNow_google_veo_3_1_lite_text_to_video` |
| [Veo 3.1 Lite · video-extend](https://popnow.ai/docs/models/veo-3-1-lite) | `google/veo-3.1-lite/video-extend` | $0.18 / run | `PopNow_google_veo_3_1_lite_video_extend` |
| [Veo 3.1 · image-to-video](https://popnow.ai/docs/models/veo-3-1) | `google/veo-3.1/image-to-video` | $1.44 / run | `PopNow_google_veo_3_1_image_to_video` |
| [Veo 3.1 · text-to-video](https://popnow.ai/docs/models/veo-3-1) | `google/veo-3.1/text-to-video` | $1.44 / run | `PopNow_google_veo_3_1_text_to_video` |
| [Veo 3.1 · video-extend](https://popnow.ai/docs/models/veo-3-1) | `google/veo-3.1/video-extend` | $1.44 / run | `PopNow_google_veo_3_1_video_extend` |
| [Kling 2.1 Master · image-to-video](https://popnow.ai/docs/models/kling-2-1-master) | `kling/2.1-master/image-to-video` | $0.216 / second | `PopNow_kling_2_1_master_image_to_video` |
| [Kling 2.1 Master · text-to-video](https://popnow.ai/docs/models/kling-2-1-master) | `kling/2.1-master/text-to-video` | $0.216 / second | `PopNow_kling_2_1_master_text_to_video` |
| [Kling 2.1 · image-to-video](https://popnow.ai/docs/models/kling-2-1) | `kling/2.1/image-to-video` | $0.035 / second | `PopNow_kling_2_1_image_to_video` |
| [Kling 2.5 Turbo · image-to-video](https://popnow.ai/docs/models/kling-2-5-turbo) | `kling/2.5-turbo/image-to-video` | $0.056 / second | `PopNow_kling_2_5_turbo_image_to_video` |
| [Kling 2.5 Turbo · text-to-video](https://popnow.ai/docs/models/kling-2-5-turbo) | `kling/2.5-turbo/text-to-video` | $0.056 / second | `PopNow_kling_2_5_turbo_text_to_video` |
| [Kling 2.6 · character-animation](https://popnow.ai/docs/models/kling-2-6) | `kling/2.6/character-animation` | $0.069 / second | `PopNow_kling_2_6_character_animation` |
| [Kling 2.6 · image-to-video](https://popnow.ai/docs/models/kling-2-6) | `kling/2.6/image-to-video` | $0.07038 / second | `PopNow_kling_2_6_image_to_video` |
| [Kling 2.6 · text-to-video](https://popnow.ai/docs/models/kling-2-6) | `kling/2.6/text-to-video` | $0.069 / second | `PopNow_kling_2_6_text_to_video` |
| [Kling 3.0 Turbo · image-to-video](https://popnow.ai/docs/models/kling-3-0-turbo) | `kling/3.0-turbo/image-to-video` | $0.112 / second | `PopNow_kling_3_0_turbo_image_to_video` |
| [Kling 3.0 Turbo · text-to-video](https://popnow.ai/docs/models/kling-3-0-turbo) | `kling/3.0-turbo/text-to-video` | $0.112 / second | `PopNow_kling_3_0_turbo_text_to_video` |
| [Kling 3.0 · character-animation](https://popnow.ai/docs/models/kling-3-0) | `kling/3.0/character-animation` | $0.1008 / second | `PopNow_kling_3_0_character_animation` |
| [Kling 3.0 · image-to-video](https://popnow.ai/docs/models/kling-3-0) | `kling/3.0/image-to-video` | $0.0672 / second | `PopNow_kling_3_0_image_to_video` |
| [Kling 3.0 · text-to-video](https://popnow.ai/docs/models/kling-3-0) | `kling/3.0/text-to-video` | $0.0672 / second | `PopNow_kling_3_0_text_to_video` |
| [Kling 4.0 · image-to-video](https://popnow.ai/docs/models/kling-4-0) | `kling/4.0/image-to-video` | $0.1884 / second | `PopNow_kling_4_0_image_to_video` |
| [Kling 4.0 · reference-to-video](https://popnow.ai/docs/models/kling-4-0) | `kling/4.0/reference-to-video` | $0.1128 / second | `PopNow_kling_4_0_reference_to_video` |
| [Kling 4.0 · text-to-video](https://popnow.ai/docs/models/kling-4-0) | `kling/4.0/text-to-video` | $0.1884 / second | `PopNow_kling_4_0_text_to_video` |
| [Kling 4.0 · video-edit](https://popnow.ai/docs/models/kling-4-0) | `kling/4.0/video-edit` | $0.1128 / second | `PopNow_kling_4_0_video_edit` |
| [Kling 4.0 · video-extend](https://popnow.ai/docs/models/kling-4-0) | `kling/4.0/video-extend` | $0.1884 / second | `PopNow_kling_4_0_video_extend` |
| [Kling Avatar 2.0 · talking-avatar](https://popnow.ai/docs/models/kling-avatar-2-0) | `kling/avatar-2.0/talking-avatar` | $0.0512 / second | `PopNow_kling_avatar_2_0_talking_avatar` |
| [Kling O3 · image-to-video](https://popnow.ai/docs/models/kling-o3) | `kling/o3/image-to-video` | $0.0672 / second | `PopNow_kling_o3_image_to_video` |
| [Kling O3 · reference-to-video](https://popnow.ai/docs/models/kling-o3) | `kling/o3/reference-to-video` | $0.0672 / second | `PopNow_kling_o3_reference_to_video` |
| [Kling O3 · text-to-video](https://popnow.ai/docs/models/kling-o3) | `kling/o3/text-to-video` | $0.0672 / second | `PopNow_kling_o3_text_to_video` |
| [Kling O3 · video-edit](https://popnow.ai/docs/models/kling-o3) | `kling/o3/video-edit` | $0.126452 / second | `PopNow_kling_o3_video_edit` |
| [LTX 2.5 · image-to-video](https://popnow.ai/docs/models/ltx-2-5) | `lightricks/ltx-2.5/image-to-video` | $0.0936 / second | `PopNow_lightricks_ltx_2_5_image_to_video` |
| [LTX 2.5 · text-to-video](https://popnow.ai/docs/models/ltx-2-5) | `lightricks/ltx-2.5/text-to-video` | $0.0945 / second | `PopNow_lightricks_ltx_2_5_text_to_video` |
| [LTX-2 19B LoRA · image-to-video](https://popnow.ai/docs/models/ltx-2-19b-lora) | `lightricks/ltx-2-19b-lora/image-to-video` | $0.018 / second | `PopNow_lightricks_ltx_2_19b_lora_image_to_video` |
| [LTX-2 19B LoRA · text-to-video](https://popnow.ai/docs/models/ltx-2-19b-lora) | `lightricks/ltx-2-19b-lora/text-to-video` | $0.018 / second | `PopNow_lightricks_ltx_2_19b_lora_text_to_video` |
| [LTX-2 19B · image-to-video](https://popnow.ai/docs/models/ltx-2-19b) | `lightricks/ltx-2-19b/image-to-video` | $0.0144 / second | `PopNow_lightricks_ltx_2_19b_image_to_video` |
| [LTX-2 19B · text-to-video](https://popnow.ai/docs/models/ltx-2-19b) | `lightricks/ltx-2-19b/text-to-video` | $0.0144 / second | `PopNow_lightricks_ltx_2_19b_text_to_video` |
| [LTX-2 19B · video-extend](https://popnow.ai/docs/models/ltx-2-19b) | `lightricks/ltx-2-19b/video-extend` | $0.0144 / second | `PopNow_lightricks_ltx_2_19b_video_extend` |
| [LTX-2.3 LoRA · image-to-video](https://popnow.ai/docs/models/ltx-2-3-lora) | `lightricks/ltx-2.3-lora/image-to-video` | $0.024 / second | `PopNow_lightricks_ltx_2_3_lora_image_to_video` |
| [LTX-2.3 LoRA · text-to-video](https://popnow.ai/docs/models/ltx-2-3-lora) | `lightricks/ltx-2.3-lora/text-to-video` | $0.024 / second | `PopNow_lightricks_ltx_2_3_lora_text_to_video` |
| [MiniMax H3 360 Orbit · image-to-video](https://popnow.ai/docs/models/minimax-h3-360-orbit) | `minimax/h3-360-orbit/image-to-video` | $0.05 / second | `PopNow_minimax_h3_360_orbit_image_to_video` |
| [MiniMax H3 Character Swap · video-edit](https://popnow.ai/docs/models/minimax-h3-character-swap) | `minimax/h3-character-swap/video-edit` | $0.06 / second | `PopNow_minimax_h3_character_swap_video_edit` |
| [MiniMax H3 Edit · video-edit](https://popnow.ai/docs/models/minimax-h3-edit) | `minimax/h3-edit/video-edit` | $0.03 / second | `PopNow_minimax_h3_edit_video_edit` |
| [MiniMax H3 HighSpeed · image-to-video](https://popnow.ai/docs/models/minimax-h3-highspeed) | `minimax/h3-highspeed/image-to-video` | $0.06 / second | `PopNow_minimax_h3_highspeed_image_to_video` |
| [MiniMax H3 HighSpeed · reference-to-video](https://popnow.ai/docs/models/minimax-h3-highspeed) | `minimax/h3-highspeed/reference-to-video` | $0.06 / second | `PopNow_minimax_h3_highspeed_reference_to_video` |
| [MiniMax H3 HighSpeed · text-to-video](https://popnow.ai/docs/models/minimax-h3-highspeed) | `minimax/h3-highspeed/text-to-video` | $0.06 / second | `PopNow_minimax_h3_highspeed_text_to_video` |
| [MiniMax H3 Lite · image-to-video](https://popnow.ai/docs/models/minimax-h3-lite) | `minimax/h3-lite/image-to-video` | $0.025 / second | `PopNow_minimax_h3_lite_image_to_video` |
| [MiniMax H3 Lite · reference-to-video](https://popnow.ai/docs/models/minimax-h3-lite) | `minimax/h3-lite/reference-to-video` | $0.025 / second | `PopNow_minimax_h3_lite_reference_to_video` |
| [MiniMax H3 Lite · text-to-video](https://popnow.ai/docs/models/minimax-h3-lite) | `minimax/h3-lite/text-to-video` | $0.025 / second | `PopNow_minimax_h3_lite_text_to_video` |
| [MiniMax H3 LoRA · image-to-video](https://popnow.ai/docs/models/minimax-h3-lora) | `minimax/h3-lora/image-to-video` | $0.05 / second | `PopNow_minimax_h3_lora_image_to_video` |
| [MiniMax H3 LoRA · reference-to-video](https://popnow.ai/docs/models/minimax-h3-lora) | `minimax/h3-lora/reference-to-video` | $0.06 / second | `PopNow_minimax_h3_lora_reference_to_video` |
| [MiniMax H3 LoRA · text-to-video](https://popnow.ai/docs/models/minimax-h3-lora) | `minimax/h3-lora/text-to-video` | $0.05 / second | `PopNow_minimax_h3_lora_text_to_video` |
| [MiniMax H3 LoRA · video-extend](https://popnow.ai/docs/models/minimax-h3-lora) | `minimax/h3-lora/video-extend` | $0.05 / second | `PopNow_minimax_h3_lora_video_extend` |
| [MiniMax H3 Max · image-to-video](https://popnow.ai/docs/models/minimax-h3-max) | `minimax/h3-max/image-to-video` | $0.0565 / second | `PopNow_minimax_h3_max_image_to_video` |
| [MiniMax H3 Max · text-to-video](https://popnow.ai/docs/models/minimax-h3-max) | `minimax/h3-max/text-to-video` | $0.0565 / second | `PopNow_minimax_h3_max_text_to_video` |
| [MiniMax H3 Max · video-extend](https://popnow.ai/docs/models/minimax-h3-max) | `minimax/h3-max/video-extend` | $0.056 / second | `PopNow_minimax_h3_max_video_extend` |
| [MiniMax H3 Singularity LoRA · image-to-video](https://popnow.ai/docs/models/minimax-h3-singularity-lora) | `minimax/h3-singularity-lora/image-to-video` | $0.0625 / second | `PopNow_minimax_h3_singularity_lora_image_to_video` |
| [MiniMax H3 Singularity LoRA · reference-to-video](https://popnow.ai/docs/models/minimax-h3-singularity-lora) | `minimax/h3-singularity-lora/reference-to-video` | $0.06 / second | `PopNow_minimax_h3_singularity_lora_reference_to_video` |
| [MiniMax H3 Singularity LoRA · video-extend](https://popnow.ai/docs/models/minimax-h3-singularity-lora) | `minimax/h3-singularity-lora/video-extend` | $0.0625 / second | `PopNow_minimax_h3_singularity_lora_video_extend` |
| [MiniMax H3 X Turbo · image-to-video](https://popnow.ai/docs/models/minimax-h3-x-turbo) | `minimax/h3-x-turbo/image-to-video` | $0.015 / second | `PopNow_minimax_h3_x_turbo_image_to_video` |
| [MiniMax H3 X Turbo · reference-to-video](https://popnow.ai/docs/models/minimax-h3-x-turbo) | `minimax/h3-x-turbo/reference-to-video` | $0.015 / second | `PopNow_minimax_h3_x_turbo_reference_to_video` |
| [MiniMax H3 X Turbo · text-to-video](https://popnow.ai/docs/models/minimax-h3-x-turbo) | `minimax/h3-x-turbo/text-to-video` | $0.015 / second | `PopNow_minimax_h3_x_turbo_text_to_video` |
| [MiniMax H3 X · image-to-video](https://popnow.ai/docs/models/minimax-h3-x) | `minimax/h3-x/image-to-video` | $0.022 / second | `PopNow_minimax_h3_x_image_to_video` |
| [MiniMax H3 X · reference-to-video](https://popnow.ai/docs/models/minimax-h3-x) | `minimax/h3-x/reference-to-video` | $0.022 / second | `PopNow_minimax_h3_x_reference_to_video` |
| [MiniMax H3 X · text-to-video](https://popnow.ai/docs/models/minimax-h3-x) | `minimax/h3-x/text-to-video` | $0.022 / second | `PopNow_minimax_h3_x_text_to_video` |
| [MiniMax H3 · image-to-video](https://popnow.ai/docs/models/minimax-h3) | `minimax/h3/image-to-video` | $0.025 / second | `PopNow_minimax_h3_image_to_video` |
| [MiniMax H3 · reference-to-video](https://popnow.ai/docs/models/minimax-h3) | `minimax/h3/reference-to-video` | $0.025 / second | `PopNow_minimax_h3_reference_to_video` |
| [MiniMax H3 · text-to-video](https://popnow.ai/docs/models/minimax-h3) | `minimax/h3/text-to-video` | $0.025 / second | `PopNow_minimax_h3_text_to_video` |
| [MiniMax H3 · video-extend](https://popnow.ai/docs/models/minimax-h3) | `minimax/h3/video-extend` | $0.025 / second | `PopNow_minimax_h3_video_extend` |
| [PixVerse V6 Effects · image-to-video](https://popnow.ai/docs/models/pixverse-v6-effects) | `pixverse/v6-effects/image-to-video` | $0.02331 / second | `PopNow_pixverse_v6_effects_image_to_video` |
| [PixVerse V6 Max · image-to-video](https://popnow.ai/docs/models/pixverse-v6-max) | `pixverse/v6-max/image-to-video` | $0.028196 / second | `PopNow_pixverse_v6_max_image_to_video` |
| [PixVerse V6 Max · text-to-video](https://popnow.ai/docs/models/pixverse-v6-max) | `pixverse/v6-max/text-to-video` | $0.028196 / second | `PopNow_pixverse_v6_max_text_to_video` |
| [PixVerse V6 · image-to-video](https://popnow.ai/docs/models/pixverse-v6) | `pixverse/v6/image-to-video` | $0.023532 / second | `PopNow_pixverse_v6_image_to_video` |
| [PixVerse V6 · reference-to-video](https://popnow.ai/docs/models/pixverse-v6) | `pixverse/v6/reference-to-video` | $0.023532 / second | `PopNow_pixverse_v6_reference_to_video` |
| [PixVerse V6 · text-to-video](https://popnow.ai/docs/models/pixverse-v6) | `pixverse/v6/text-to-video` | $0.023532 / second | `PopNow_pixverse_v6_text_to_video` |
| [PixVerse V6 · video-extend](https://popnow.ai/docs/models/pixverse-v6) | `pixverse/v6/video-extend` | $0.023532 / second | `PopNow_pixverse_v6_video_extend` |
| [Lip Sync · lip-sync](https://popnow.ai/docs/models/lip-sync-v1) | `popnow/lip-sync-v1/lip-sync` | $0.012 / second | `PopNow_popnow_lip_sync_v1_lip_sync` |
| [Talking Avatar · talking-avatar](https://popnow.ai/docs/models/talking-avatar-v1) | `popnow/talking-avatar-v1/talking-avatar` | $0.018 / second | `PopNow_popnow_talking_avatar_v1_talking_avatar` |
| [Video Background Remover · video-edit](https://popnow.ai/docs/models/background-remover-video-v1) | `popnow/background-remover-video-v1/video-edit` | $0.06 / second | `PopNow_popnow_background_remover_video_v1_video_edit` |
| [Video Eraser · video-edit](https://popnow.ai/docs/models/video-eraser-v1) | `popnow/video-eraser-v1/video-edit` | $0.024 / second | `PopNow_popnow_video_eraser_v1_video_edit` |
| [Video Face Enhancer · video-edit](https://popnow.ai/docs/models/face-enhancer-video-v1) | `popnow/face-enhancer-video-v1/video-edit` | $0.012 / second | `PopNow_popnow_face_enhancer_video_v1_video_edit` |
| [Video Face Swap · video-edit](https://popnow.ai/docs/models/face-swap-video-v1) | `popnow/face-swap-video-v1/video-edit` | $0.026 / second | `PopNow_popnow_face_swap_video_v1_video_edit` |
| [Video Music Remover · video-edit](https://popnow.ai/docs/models/music-remover-v1) | `popnow/music-remover-v1/video-edit` | $0.0024 / second | `PopNow_popnow_music_remover_v1_video_edit` |
| [Video Restorer · video-edit](https://popnow.ai/docs/models/video-restorer-v1) | `popnow/video-restorer-v1/video-edit` | $0.024 / second | `PopNow_popnow_video_restorer_v1_video_edit` |
| [Video Translator · video-translate](https://popnow.ai/docs/models/video-translator-v1) | `popnow/video-translator-v1/video-translate` | $0.005 / second | `PopNow_popnow_video_translator_v1_video_translate` |
| [Video Upscaler · upscale](https://popnow.ai/docs/models/video-upscaler-v1) | `popnow/video-upscaler-v1/upscale` | $0.006 / second | `PopNow_popnow_video_upscaler_v1_upscale` |
| [daVinci-MagiHuman · image-to-video](https://popnow.ai/docs/models/davinci-magihuman) | `sand-ai/davinci-magihuman/image-to-video` | $0.024 / second | `PopNow_sand_ai_davinci_magihuman_image_to_video` |
| [daVinci-MagiHuman · text-to-video](https://popnow.ai/docs/models/davinci-magihuman) | `sand-ai/davinci-magihuman/text-to-video` | $0.024 / second | `PopNow_sand_ai_davinci_magihuman_text_to_video` |
| [HunyuanVideo 1.5 · image-to-video](https://popnow.ai/docs/models/hunyuan-video-1-5) | `tencent/hunyuan-video-1.5/image-to-video` | $0.024 / second | `PopNow_tencent_hunyuan_video_1_5_image_to_video` |
| [HunyuanVideo 1.5 · text-to-video](https://popnow.ai/docs/models/hunyuan-video-1-5) | `tencent/hunyuan-video-1.5/text-to-video` | $0.024 / second | `PopNow_tencent_hunyuan_video_1_5_text_to_video` |
| [Topaz Astra · upscale](https://popnow.ai/docs/models/topaz-astra) | `topaz/astra/upscale` | $0.36 / second | `PopNow_topaz_astra_upscale` |
| [Topaz Starlight · upscale](https://popnow.ai/docs/models/topaz-starlight) | `topaz/starlight/upscale` | $0.07 / second | `PopNow_topaz_starlight_upscale` |
| [Topaz Video AI · frame-interpolation](https://popnow.ai/docs/models/topaz-video-ai) | `topaz/video-ai/frame-interpolation` | $0.002 / second | `PopNow_topaz_video_ai_frame_interpolation` |
| [Topaz Video AI · upscale](https://popnow.ai/docs/models/topaz-video-ai) | `topaz/video-ai/upscale` | $0.007058824 / second | `PopNow_topaz_video_ai_upscale` |
| [Topaz Video AI · video-edit](https://popnow.ai/docs/models/topaz-video-ai) | `topaz/video-ai/video-edit` | $0.004 / second | `PopNow_topaz_video_ai_video_edit` |
| [VEED Dubbing Pro · video-translate](https://popnow.ai/docs/models/veed-dubbing-pro) | `veed/dubbing-pro/video-translate` | $0.24 / second | `PopNow_veed_dubbing_pro_video_translate` |
| [VEED Dubbing · video-translate](https://popnow.ai/docs/models/veed-dubbing) | `veed/dubbing/video-translate` | $0.144 / second | `PopNow_veed_dubbing_video_translate` |
| [Vidu Q3 Pro · image-to-video](https://popnow.ai/docs/models/vidu-q3-pro) | `vidu/q3-pro/image-to-video` | $0.054 / second | `PopNow_vidu_q3_pro_image_to_video` |
| [Vidu Q3 Turbo · image-to-video](https://popnow.ai/docs/models/vidu-q3-turbo) | `vidu/q3-turbo/image-to-video` | $0.042 / second | `PopNow_vidu_q3_turbo_image_to_video` |
| [Vidu Q3 Turbo · video-extend](https://popnow.ai/docs/models/vidu-q3-turbo) | `vidu/q3-turbo/video-extend` | $0.042 / second | `PopNow_vidu_q3_turbo_video_extend` |
| [Vidu Q3 · image-to-video](https://popnow.ai/docs/models/vidu-q3) | `vidu/q3/image-to-video` | $0.07 / second | `PopNow_vidu_q3_image_to_video` |
| [Vidu Q4 Preview · image-to-video](https://popnow.ai/docs/models/vidu-q4-preview) | `vidu/q4-preview/image-to-video` | $0.045 / second | `PopNow_vidu_q4_preview_image_to_video` |
| [Vidu Q4 Preview · reference-to-video](https://popnow.ai/docs/models/vidu-q4-preview) | `vidu/q4-preview/reference-to-video` | $0.045 / second | `PopNow_vidu_q4_preview_reference_to_video` |
| [Vidu Q4 Preview · video-extend](https://popnow.ai/docs/models/vidu-q4-preview) | `vidu/q4-preview/video-extend` | $0.045 / second | `PopNow_vidu_q4_preview_video_extend` |

## Image

| Node | Call name | From | Node type |
| --- | --- | --- | --- |
| [Qwen Image 1.0 LoRA · image-to-image](https://popnow.ai/docs/models/qwen-image-1-0-lora) | `alibaba/qwen-image-1.0-lora/edit` | $0.03 / image | `PopNow_alibaba_qwen_image_1_0_lora_edit` |
| [Qwen Image 1.0 LoRA · text-to-image](https://popnow.ai/docs/models/qwen-image-1-0-lora) | `alibaba/qwen-image-1.0-lora/text-to-image` | $0.03 / image | `PopNow_alibaba_qwen_image_1_0_lora_text_to_image` |
| [Qwen Image 2 · image-to-image](https://popnow.ai/docs/models/alibaba-qwen-image-2) | `alibaba/qwen-image-2/edit` | $0.035 / image | `PopNow_alibaba_qwen_image_2_edit` |
| [Qwen Image 2 · text-to-image](https://popnow.ai/docs/models/alibaba-qwen-image-2) | `alibaba/qwen-image-2/text-to-image` | $0.035 / image | `PopNow_alibaba_qwen_image_2_text_to_image` |
| [Qwen Image 2.1 LoRA · image-to-image](https://popnow.ai/docs/models/qwen-image-2-1-lora) | `alibaba/qwen-image-2.1-lora/edit` | $0.042 / image | `PopNow_alibaba_qwen_image_2_1_lora_edit` |
| [Qwen Image 2.1 LoRA · text-to-image](https://popnow.ai/docs/models/qwen-image-2-1-lora) | `alibaba/qwen-image-2.1-lora/text-to-image` | $0.03 / image | `PopNow_alibaba_qwen_image_2_1_lora_text_to_image` |
| [Qwen Image 2.1 Pro · image-to-image](https://popnow.ai/docs/models/qwen-image-2-1-pro) | `alibaba/qwen-image-2.1-pro/edit` | $0.036 / image | `PopNow_alibaba_qwen_image_2_1_pro_edit` |
| [Qwen Image 2.1 Pro · text-to-image](https://popnow.ai/docs/models/qwen-image-2-1-pro) | `alibaba/qwen-image-2.1-pro/text-to-image` | $0.036 / image | `PopNow_alibaba_qwen_image_2_1_pro_text_to_image` |
| [Qwen Image 2.1 Turbo · image-to-image](https://popnow.ai/docs/models/qwen-image-2-1-turbo) | `alibaba/qwen-image-2.1-turbo/edit` | $0.0144 / image | `PopNow_alibaba_qwen_image_2_1_turbo_edit` |
| [Qwen Image 2.1 Turbo · text-to-image](https://popnow.ai/docs/models/qwen-image-2-1-turbo) | `alibaba/qwen-image-2.1-turbo/text-to-image` | $0.0144 / image | `PopNow_alibaba_qwen_image_2_1_turbo_text_to_image` |
| [Qwen Image 2.1 · image-to-image](https://popnow.ai/docs/models/qwen-image-2-1) | `alibaba/qwen-image-2.1/edit` | $0.036 / image | `PopNow_alibaba_qwen_image_2_1_edit` |
| [Qwen Image 2.1 · text-to-image](https://popnow.ai/docs/models/qwen-image-2-1) | `alibaba/qwen-image-2.1/text-to-image` | $0.024 / image | `PopNow_alibaba_qwen_image_2_1_text_to_image` |
| [Qwen Image 2512 LoRA · image-to-image](https://popnow.ai/docs/models/qwen-image-2512-lora) | `alibaba/qwen-image-2512-lora/edit` | $0.03 / image | `PopNow_alibaba_qwen_image_2512_lora_edit` |
| [Qwen Image 2512 LoRA · text-to-image](https://popnow.ai/docs/models/qwen-image-2512-lora) | `alibaba/qwen-image-2512-lora/text-to-image` | $0.03 / image | `PopNow_alibaba_qwen_image_2512_lora_text_to_image` |
| [Qwen Image 3.0 Pro · image-to-image](https://popnow.ai/docs/models/qwen-image-3-0-pro) | `alibaba/qwen-image-3.0-pro/edit` | $0.04 / image | `PopNow_alibaba_qwen_image_3_0_pro_edit` |
| [Qwen Image 3.0 Pro · text-to-image](https://popnow.ai/docs/models/qwen-image-3-0-pro) | `alibaba/qwen-image-3.0-pro/text-to-image` | $0.04 / image | `PopNow_alibaba_qwen_image_3_0_pro_text_to_image` |
| [Qwen Image 3.0 · image-to-image](https://popnow.ai/docs/models/qwen-image-3-0) | `alibaba/qwen-image-3.0/edit` | $0.03 / image | `PopNow_alibaba_qwen_image_3_0_edit` |
| [Qwen Image 3.0 · text-to-image](https://popnow.ai/docs/models/qwen-image-3-0) | `alibaba/qwen-image-3.0/text-to-image` | $0.03 / image | `PopNow_alibaba_qwen_image_3_0_text_to_image` |
| [Qwen Image Edit 2509 LoRA · image-to-image](https://popnow.ai/docs/models/qwen-image-edit-2509-lora) | `alibaba/qwen-image-edit-2509-lora/edit` | $0.03 / image | `PopNow_alibaba_qwen_image_edit_2509_lora_edit` |
| [Wan 2.1 Image LoRA · image-to-image](https://popnow.ai/docs/models/wan-2-1-image-lora) | `alibaba/wan-2.1-image-lora/edit` | $0.03 / image | `PopNow_alibaba_wan_2_1_image_lora_edit` |
| [Wan 2.1 Image LoRA · text-to-image](https://popnow.ai/docs/models/wan-2-1-image-lora) | `alibaba/wan-2.1-image-lora/text-to-image` | $0.03 / image | `PopNow_alibaba_wan_2_1_image_lora_text_to_image` |
| [Wan 2.2 Image LoRA · text-to-image](https://popnow.ai/docs/models/wan-2-2-image-lora) | `alibaba/wan-2.2-image-lora/text-to-image` | $0.03 / image | `PopNow_alibaba_wan_2_2_image_lora_text_to_image` |
| [Wan 2.7 Pro · image-to-image](https://popnow.ai/docs/models/wan-2-7-pro) | `alibaba/wan-2.7-pro/edit` | $0.075 / image | `PopNow_alibaba_wan_2_7_pro_edit` |
| [Wan 2.7 Pro · text-to-image](https://popnow.ai/docs/models/wan-2-7-pro) | `alibaba/wan-2.7-pro/text-to-image` | $0.075 / image | `PopNow_alibaba_wan_2_7_pro_text_to_image` |
| [Wan 2.7 · image-to-image](https://popnow.ai/docs/models/wan-2-7) | `alibaba/wan-2.7/edit` | $0.03 / image | `PopNow_alibaba_wan_2_7_edit` |
| [Wan 2.7 · text-to-image](https://popnow.ai/docs/models/wan-2-7) | `alibaba/wan-2.7/text-to-image` | $0.03 / image | `PopNow_alibaba_wan_2_7_text_to_image` |
| [Z-Image Base LoRA · image-to-image](https://popnow.ai/docs/models/z-image-base-lora) | `alibaba/z-image-base-lora/edit` | $0.0144 / image | `PopNow_alibaba_z_image_base_lora_edit` |
| [Z-Image Base LoRA · text-to-image](https://popnow.ai/docs/models/z-image-base-lora) | `alibaba/z-image-base-lora/text-to-image` | $0.0144 / image | `PopNow_alibaba_z_image_base_lora_text_to_image` |
| [Z-Image Turbo LoRA · image-to-image](https://popnow.ai/docs/models/z-image-turbo-lora) | `alibaba/z-image-turbo-lora/edit` | $0.012 / image | `PopNow_alibaba_z_image_turbo_lora_edit` |
| [Z-Image Turbo LoRA · text-to-image](https://popnow.ai/docs/models/z-image-turbo-lora) | `alibaba/z-image-turbo-lora/text-to-image` | $0.012 / image | `PopNow_alibaba_z_image_turbo_lora_text_to_image` |
| [Z-Image · text-to-image](https://popnow.ai/docs/models/z-image) | `alibaba/z-image-turbo/text-to-image` | $0.01 / image | `PopNow_alibaba_z_image_turbo_text_to_image` |
| [FLUX 3 Klein Base LoRA · image-to-image](https://popnow.ai/docs/models/flux-3-klein-base-lora) | `black-forest-labs/flux-3-klein-base-lora/edit` | $0.06 / image | `PopNow_black_forest_labs_flux_3_klein_base_lora_edit` |
| [FLUX 3 Klein Base LoRA · text-to-image](https://popnow.ai/docs/models/flux-3-klein-base-lora) | `black-forest-labs/flux-3-klein-base-lora/text-to-image` | $0.042 / image | `PopNow_black_forest_labs_flux_3_klein_base_lora_text_to_image` |
| [FLUX 3 Klein Base · image-to-image](https://popnow.ai/docs/models/flux-3-klein-base) | `black-forest-labs/flux-3-klein-base/edit` | $0.054 / image | `PopNow_black_forest_labs_flux_3_klein_base_edit` |
| [FLUX 3 Klein Base · text-to-image](https://popnow.ai/docs/models/flux-3-klein-base) | `black-forest-labs/flux-3-klein-base/text-to-image` | $0.036 / image | `PopNow_black_forest_labs_flux_3_klein_base_text_to_image` |
| [FLUX.1 Dev ControlNet LoRA · text-to-image](https://popnow.ai/docs/models/flux-1-dev-controlnet-lora) | `black-forest-labs/flux-1-dev-controlnet-lora/text-to-image` | $0.036 / image | `PopNow_black_forest_labs_flux_1_dev_controlnet_lora_text_to_image` |
| [FLUX.1 Dev LoRA · image-to-image](https://popnow.ai/docs/models/flux-1-dev-lora) | `black-forest-labs/flux-1-dev-lora/edit` | $0.018 / image | `PopNow_black_forest_labs_flux_1_dev_lora_edit` |
| [FLUX.1 Dev LoRA · text-to-image](https://popnow.ai/docs/models/flux-1-dev-lora) | `black-forest-labs/flux-1-dev-lora/text-to-image` | $0.018 / image | `PopNow_black_forest_labs_flux_1_dev_lora_text_to_image` |
| [FLUX.1 Fill Dev LoRA · image-to-image](https://popnow.ai/docs/models/flux-1-fill-dev-lora) | `black-forest-labs/flux-1-fill-dev-lora/edit` | $0.042 / image | `PopNow_black_forest_labs_flux_1_fill_dev_lora_edit` |
| [FLUX.1 Krea Dev LoRA · image-to-image](https://popnow.ai/docs/models/flux-1-krea-dev-lora) | `black-forest-labs/flux-1-krea-dev-lora/edit` | $0.024 / image | `PopNow_black_forest_labs_flux_1_krea_dev_lora_edit` |
| [FLUX.1 Krea Dev LoRA · text-to-image](https://popnow.ai/docs/models/flux-1-krea-dev-lora) | `black-forest-labs/flux-1-krea-dev-lora/text-to-image` | $0.024 / image | `PopNow_black_forest_labs_flux_1_krea_dev_lora_text_to_image` |
| [FLUX.1 Schnell LoRA · image-to-image](https://popnow.ai/docs/models/flux-1-schnell-lora) | `black-forest-labs/flux-1-schnell-lora/edit` | $0.006 / image | `PopNow_black_forest_labs_flux_1_schnell_lora_edit` |
| [FLUX.1 Schnell LoRA · text-to-image](https://popnow.ai/docs/models/flux-1-schnell-lora) | `black-forest-labs/flux-1-schnell-lora/text-to-image` | $0.006 / image | `PopNow_black_forest_labs_flux_1_schnell_lora_text_to_image` |
| [FLUX.2 Dev LoRA · image-to-image](https://popnow.ai/docs/models/flux-2-dev-lora) | `black-forest-labs/flux-2-dev-lora/edit` | $0.036 / image | `PopNow_black_forest_labs_flux_2_dev_lora_edit` |
| [FLUX.2 Dev LoRA · text-to-image](https://popnow.ai/docs/models/flux-2-dev-lora) | `black-forest-labs/flux-2-dev-lora/text-to-image` | $0.0216 / image | `PopNow_black_forest_labs_flux_2_dev_lora_text_to_image` |
| [FLUX.2 Dev · image-to-image](https://popnow.ai/docs/models/flux-2-dev) | `black-forest-labs/flux-2-dev/edit` | $0.0231 / image | `PopNow_black_forest_labs_flux_2_dev_edit` |
| [FLUX.2 Dev · text-to-image](https://popnow.ai/docs/models/flux-2-dev) | `black-forest-labs/flux-2-dev/text-to-image` | $0.0116 / image | `PopNow_black_forest_labs_flux_2_dev_text_to_image` |
| [FLUX.2 Flex · image-to-image](https://popnow.ai/docs/models/flux-2-flex) | `black-forest-labs/flux-2-flex/edit` | $0.1154 / image | `PopNow_black_forest_labs_flux_2_flex_edit` |
| [FLUX.2 Flex · text-to-image](https://popnow.ai/docs/models/flux-2-flex) | `black-forest-labs/flux-2-flex/text-to-image` | $0.0578 / image | `PopNow_black_forest_labs_flux_2_flex_text_to_image` |
| [FLUX.2 Klein 4B LoRA · image-to-image](https://popnow.ai/docs/models/flux-2-klein-4b-lora) | `black-forest-labs/flux-2-klein-4b-lora/edit` | $0.0204 / image | `PopNow_black_forest_labs_flux_2_klein_4b_lora_edit` |
| [FLUX.2 Klein 4B LoRA · text-to-image](https://popnow.ai/docs/models/flux-2-klein-4b-lora) | `black-forest-labs/flux-2-klein-4b-lora/text-to-image` | $0.0156 / image | `PopNow_black_forest_labs_flux_2_klein_4b_lora_text_to_image` |
| [FLUX.2 Klein 4B · image-to-image](https://popnow.ai/docs/models/flux-2-klein-4b) | `black-forest-labs/flux-2-klein-4b/edit` | $0.0126 / image | `PopNow_black_forest_labs_flux_2_klein_4b_edit` |
| [FLUX.2 Klein 4B · text-to-image](https://popnow.ai/docs/models/flux-2-klein-4b) | `black-forest-labs/flux-2-klein-4b/text-to-image` | $0.0093 / image | `PopNow_black_forest_labs_flux_2_klein_4b_text_to_image` |
| [FLUX.2 Klein 9B LoRA · image-to-image](https://popnow.ai/docs/models/flux-2-klein-9b-lora) | `black-forest-labs/flux-2-klein-9b-lora/edit` | $0.0252 / image | `PopNow_black_forest_labs_flux_2_klein_9b_lora_edit` |
| [FLUX.2 Klein 9B LoRA · text-to-image](https://popnow.ai/docs/models/flux-2-klein-9b-lora) | `black-forest-labs/flux-2-klein-9b-lora/text-to-image` | $0.018 / image | `PopNow_black_forest_labs_flux_2_klein_9b_lora_text_to_image` |
| [FLUX.2 Klein 9B · image-to-image](https://popnow.ai/docs/models/flux-2-klein-9b) | `black-forest-labs/flux-2-klein-9b/edit` | $0.0163 / image | `PopNow_black_forest_labs_flux_2_klein_9b_edit` |
| [FLUX.2 Klein 9B · text-to-image](https://popnow.ai/docs/models/flux-2-klein-9b) | `black-forest-labs/flux-2-klein-9b/text-to-image` | $0.011 / image | `PopNow_black_forest_labs_flux_2_klein_9b_text_to_image` |
| [FLUX.2 Klein Base 4B LoRA · image-to-image](https://popnow.ai/docs/models/flux-2-klein-base-4b-lora) | `black-forest-labs/flux-2-klein-base-4b-lora/edit` | $0.024 / image | `PopNow_black_forest_labs_flux_2_klein_base_4b_lora_edit` |
| [FLUX.2 Klein Base 4B LoRA · text-to-image](https://popnow.ai/docs/models/flux-2-klein-base-4b-lora) | `black-forest-labs/flux-2-klein-base-4b-lora/text-to-image` | $0.018 / image | `PopNow_black_forest_labs_flux_2_klein_base_4b_lora_text_to_image` |
| [FLUX.2 Klein Base 9B LoRA · image-to-image](https://popnow.ai/docs/models/flux-2-klein-base-9b-lora) | `black-forest-labs/flux-2-klein-base-9b-lora/edit` | $0.0312 / image | `PopNow_black_forest_labs_flux_2_klein_base_9b_lora_edit` |
| [FLUX.2 Klein Base 9B LoRA · text-to-image](https://popnow.ai/docs/models/flux-2-klein-base-9b-lora) | `black-forest-labs/flux-2-klein-base-9b-lora/text-to-image` | $0.024 / image | `PopNow_black_forest_labs_flux_2_klein_base_9b_lora_text_to_image` |
| [FLUX.2 Max · image-to-image](https://popnow.ai/docs/models/flux-2-max) | `black-forest-labs/flux-2-max/edit` | $0.0761 / image | `PopNow_black_forest_labs_flux_2_max_edit` |
| [FLUX.2 Max · text-to-image](https://popnow.ai/docs/models/flux-2-max) | `black-forest-labs/flux-2-max/text-to-image` | $0.07 / image | `PopNow_black_forest_labs_flux_2_max_text_to_image` |
| [FLUX.2 Pro · image-to-image](https://popnow.ai/docs/models/flux-2-pro) | `black-forest-labs/flux-2-pro/edit` | $0.0578 / image | `PopNow_black_forest_labs_flux_2_pro_edit` |
| [FLUX.2 Pro · text-to-image](https://popnow.ai/docs/models/flux-2-pro) | `black-forest-labs/flux-2-pro/text-to-image` | $0.03 / image | `PopNow_black_forest_labs_flux_2_pro_text_to_image` |
| [Seed3D 2.0 · image-to-3d](https://popnow.ai/docs/models/seed3d-2-0) | `bytedance/seed3d-2.0/image-to-3d` | $0.48 / run | `PopNow_bytedance_seed3d_2_0_image_to_3d` |
| [Seedream 4.0 · image-to-image](https://popnow.ai/docs/models/seedream-4-0) | `bytedance/seedream-4.0/edit` | $0.0318 / image | `PopNow_bytedance_seedream_4_0_edit` |
| [Seedream 4.0 · text-to-image](https://popnow.ai/docs/models/seedream-4-0) | `bytedance/seedream-4.0/text-to-image` | $0.0318 / image | `PopNow_bytedance_seedream_4_0_text_to_image` |
| [Seedream 4.5 · image-to-image](https://popnow.ai/docs/models/seedream-4-5) | `bytedance/seedream-4.5/edit` | $0.04 / image | `PopNow_bytedance_seedream_4_5_edit` |
| [Seedream 4.5 · text-to-image](https://popnow.ai/docs/models/seedream-4-5) | `bytedance/seedream-4.5/text-to-image` | $0.04 / image | `PopNow_bytedance_seedream_4_5_text_to_image` |
| [Seedream 5.0 Flash · image-to-image](https://popnow.ai/docs/models/seedream-5-0-flash) | `bytedance/seedream-5.0-flash/edit` | $0.029 / image | `PopNow_bytedance_seedream_5_0_flash_edit` |
| [Seedream 5.0 Flash · layer-decomposition](https://popnow.ai/docs/models/seedream-5-0-flash) | `bytedance/seedream-5.0-flash/layer-decomposition` | $0.026 / image | `PopNow_bytedance_seedream_5_0_flash_layer_decomposition` |
| [Seedream 5.0 Flash · text-to-image](https://popnow.ai/docs/models/seedream-5-0-flash) | `bytedance/seedream-5.0-flash/text-to-image` | $0.029 / image | `PopNow_bytedance_seedream_5_0_flash_text_to_image` |
| [Seedream 5.0 Lite · image-to-image](https://popnow.ai/docs/models/seedream-5-0-lite) | `bytedance/seedream-5.0-lite/edit` | $0.0345 / image | `PopNow_bytedance_seedream_5_0_lite_edit` |
| [Seedream 5.0 Lite · text-to-image](https://popnow.ai/docs/models/seedream-5-0-lite) | `bytedance/seedream-5.0-lite/text-to-image` | $0.0345 / image | `PopNow_bytedance_seedream_5_0_lite_text_to_image` |
| [Seedream 5.0 Pro · image-to-image](https://popnow.ai/docs/models/seedream-5-0-pro) | `bytedance/seedream-5.0-pro/edit` | $0.036 / image | `PopNow_bytedance_seedream_5_0_pro_edit` |
| [Seedream 5.0 Pro · layer-decomposition](https://popnow.ai/docs/models/seedream-5-0-pro) | `bytedance/seedream-5.0-pro/layer-decomposition` | $0.042 / image | `PopNow_bytedance_seedream_5_0_pro_layer_decomposition` |
| [Seedream 5.0 Pro · text-to-image](https://popnow.ai/docs/models/seedream-5-0-pro) | `bytedance/seedream-5.0-pro/text-to-image` | $0.036 / image | `PopNow_bytedance_seedream_5_0_pro_text_to_image` |
| [Anima Turbo LoRA · image-to-image](https://popnow.ai/docs/models/anima-turbo-lora) | `circlestone-labs/anima-turbo-lora/edit` | $0.018 / image | `PopNow_circlestone_labs_anima_turbo_lora_edit` |
| [Anima Turbo LoRA · text-to-image](https://popnow.ai/docs/models/anima-turbo-lora) | `circlestone-labs/anima-turbo-lora/text-to-image` | $0.018 / image | `PopNow_circlestone_labs_anima_turbo_lora_text_to_image` |
| [Anima Turbo · image-to-image](https://popnow.ai/docs/models/anima-turbo) | `circlestone-labs/anima-turbo/edit` | $0.012 / image | `PopNow_circlestone_labs_anima_turbo_edit` |
| [Anima Turbo · text-to-image](https://popnow.ai/docs/models/anima-turbo) | `circlestone-labs/anima-turbo/text-to-image` | $0.012 / image | `PopNow_circlestone_labs_anima_turbo_text_to_image` |
| [Nano Banana 2 · image-to-image](https://popnow.ai/docs/models/nano-banana-2) | `google/nano-banana-2/edit` | $0.036 / image | `PopNow_google_nano_banana_2_edit` |
| [Nano Banana 2 · text-to-image](https://popnow.ai/docs/models/nano-banana-2) | `google/nano-banana-2/text-to-image` | $0.036 / image | `PopNow_google_nano_banana_2_text_to_image` |
| [Nano Banana 2.1 · image-to-image](https://popnow.ai/docs/models/nano-banana-2-1) | `google/nano-banana-2.1/edit` | $0.048 / image | `PopNow_google_nano_banana_2_1_edit` |
| [Nano Banana 2.1 · text-to-image](https://popnow.ai/docs/models/nano-banana-2-1) | `google/nano-banana-2.1/text-to-image` | $0.048 / image | `PopNow_google_nano_banana_2_1_text_to_image` |
| [Nano Banana Pro · image-to-image](https://popnow.ai/docs/models/nano-banana-pro) | `google/nano-banana-pro/edit` | $0.1072 / image | `PopNow_google_nano_banana_pro_edit` |
| [Nano Banana Pro · text-to-image](https://popnow.ai/docs/models/nano-banana-pro) | `google/nano-banana-pro/text-to-image` | $0.1072 / image | `PopNow_google_nano_banana_pro_text_to_image` |
| [Ideogram Vector 1.0 · image-edit](https://popnow.ai/docs/models/ideogram-vector-1) | `ideogram/vector-1/edit` | $0.132 / image | `PopNow_ideogram_vector_1_edit` |
| [Ideogram Vector 1.0 · text-to-image](https://popnow.ai/docs/models/ideogram-vector-1) | `ideogram/vector-1/text-to-image` | $0.174 / image | `PopNow_ideogram_vector_1_text_to_image` |
| [Jib Mix Qwen LoRA · text-to-image](https://popnow.ai/docs/models/jib-mix-qwen-image-lora) | `j1b/jib-mix-qwen-image-lora/text-to-image` | $0.03 / image | `PopNow_j1b_jib_mix_qwen_image_lora_text_to_image` |
| [Jib Mix Qwen · text-to-image](https://popnow.ai/docs/models/jib-mix-qwen-image) | `j1b/jib-mix-qwen-image/text-to-image` | $0.024 / image | `PopNow_j1b_jib_mix_qwen_image_text_to_image` |
| [Krea 2 Large · text-to-image](https://popnow.ai/docs/models/krea-2-large) | `krea/2-large/text-to-image` | $0.06 / image | `PopNow_krea_2_large_text_to_image` |
| [Krea 2 Medium Turbo · text-to-image](https://popnow.ai/docs/models/krea-2-medium-turbo) | `krea/2-medium-turbo/text-to-image` | $0.015 / image | `PopNow_krea_2_medium_turbo_text_to_image` |
| [Krea 2 Medium · text-to-image](https://popnow.ai/docs/models/krea-2-medium) | `krea/2-medium/text-to-image` | $0.03 / image | `PopNow_krea_2_medium_text_to_image` |
| [Krea 2 Turbo LoRA · image-to-image](https://popnow.ai/docs/models/krea-2-turbo-lora) | `krea/2-turbo-lora/edit` | $0.0216 / image | `PopNow_krea_2_turbo_lora_edit` |
| [Krea 2 Turbo LoRA · text-to-image](https://popnow.ai/docs/models/krea-2-turbo-lora) | `krea/2-turbo-lora/text-to-image` | $0.0216 / image | `PopNow_krea_2_turbo_lora_text_to_image` |
| [Krea 3 · image-to-image](https://popnow.ai/docs/models/krea-3) | `krea/3/edit` | $0.072 / image | `PopNow_krea_3_edit` |
| [Krea 3 · text-to-image](https://popnow.ai/docs/models/krea-3) | `krea/3/text-to-image` | $0.036 / image | `PopNow_krea_3_text_to_image` |
| [MiniMax H3 Image LoRA · image-to-image](https://popnow.ai/docs/models/minimax-h3-image-lora) | `minimax/h3-image-lora/edit` | $0.054 / image | `PopNow_minimax_h3_image_lora_edit` |
| [MiniMax H3 Image LoRA · text-to-image](https://popnow.ai/docs/models/minimax-h3-image-lora) | `minimax/h3-image-lora/text-to-image` | $0.042 / image | `PopNow_minimax_h3_image_lora_text_to_image` |
| [Neta Lumina · text-to-image](https://popnow.ai/docs/models/neta-lumina) | `neta-art/neta-lumina/text-to-image` | $0.012 / image | `PopNow_neta_art_neta_lumina_text_to_image` |
| [GPT Image 2 · image-to-image](https://popnow.ai/docs/models/gpt-image-2) | `openai/gpt-image-2/edit` | $0.001816 / image | `PopNow_openai_gpt_image_2_edit` |
| [GPT Image 2 · text-to-image](https://popnow.ai/docs/models/gpt-image-2) | `openai/gpt-image-2/text-to-image` | $0.001816 / image | `PopNow_openai_gpt_image_2_text_to_image` |
| [GPT Image 2.5 Flare · image-to-image](https://popnow.ai/docs/models/gpt-image-2-5-flare) | `openai/gpt-image-2.5-flare/edit` | $0.001816 / image | `PopNow_openai_gpt_image_2_5_flare_edit` |
| [GPT Image 2.5 Flare · text-to-image](https://popnow.ai/docs/models/gpt-image-2-5-flare) | `openai/gpt-image-2.5-flare/text-to-image` | $0.001816 / image | `PopNow_openai_gpt_image_2_5_flare_text_to_image` |
| [GPT Image 2.5 Sunburst · image-to-image](https://popnow.ai/docs/models/gpt-image-2-5-sunburst) | `openai/gpt-image-2.5-sunburst/edit` | $0.001816 / image | `PopNow_openai_gpt_image_2_5_sunburst_edit` |
| [GPT Image 2.5 Sunburst · text-to-image](https://popnow.ai/docs/models/gpt-image-2-5-sunburst) | `openai/gpt-image-2.5-sunburst/text-to-image` | $0.001816 / image | `PopNow_openai_gpt_image_2_5_sunburst_text_to_image` |
| [Anime to Real · image-edit](https://popnow.ai/docs/models/anime-to-real-v1) | `popnow/anime-to-real-v1/edit` | $0.03 / image | `PopNow_popnow_anime_to_real_v1_edit` |
| [Background Remover · image-edit](https://popnow.ai/docs/models/background-remover-v1) | `popnow/background-remover-v1/edit` | $0.0048 / image | `PopNow_popnow_background_remover_v1_edit` |
| [Camera Angle Changer · image-edit](https://popnow.ai/docs/models/camera-angle-changer-v1) | `popnow/camera-angle-changer-v1/edit` | $0.03 / image | `PopNow_popnow_camera_angle_changer_v1_edit` |
| [Celebrity Look-Alike · image-to-image](https://popnow.ai/docs/models/look-alike-v1) | `popnow/look-alike-v1/edit` | $0.05 / image | `PopNow_popnow_look_alike_v1_edit` |
| [Face Enhancer · image-edit](https://popnow.ai/docs/models/face-enhancer-v1) | `popnow/face-enhancer-v1/edit` | $0.012 / image | `PopNow_popnow_face_enhancer_v1_edit` |
| [Face Swap Plus · image-to-image](https://popnow.ai/docs/models/face-swap-v1-plus) | `popnow/face-swap-v1-plus/edit` | $0.16 / image | `PopNow_popnow_face_swap_v1_plus_edit` |
| [Face Swap Pro · image-to-image](https://popnow.ai/docs/models/face-swap-pro-v1) | `popnow/face-swap-pro-v1/edit` | $0.16 / image | `PopNow_popnow_face_swap_pro_v1_edit` |
| [Face Swap · image-to-image](https://popnow.ai/docs/models/face-swap-v1) | `popnow/face-swap-v1/edit` | $0.013 / image | `PopNow_popnow_face_swap_v1_edit` |
| [Head Swap · image-to-image](https://popnow.ai/docs/models/head-swap-v1) | `popnow/head-swap-v1/edit` | $0.013 / image | `PopNow_popnow_head_swap_v1_edit` |
| [Image Expander · image-edit](https://popnow.ai/docs/models/image-expander-v1) | `popnow/image-expander-v1/edit` | $0.024 / image | `PopNow_popnow_image_expander_v1_edit` |
| [Image Upscaler · upscale](https://popnow.ai/docs/models/image-upscaler-v1) | `popnow/image-upscaler-v1/upscale` | $0.012 / image | `PopNow_popnow_image_upscaler_v1_upscale` |
| [Object Eraser · image-edit](https://popnow.ai/docs/models/object-eraser-v1) | `popnow/object-eraser-v1/edit` | $0.03 / image | `PopNow_popnow_object_eraser_v1_edit` |
| [Object Extractor · image-edit](https://popnow.ai/docs/models/object-extractor-v1) | `popnow/object-extractor-v1/edit` | $0.024 / image | `PopNow_popnow_object_extractor_v1_edit` |
| [Old Photo Restorer · image-edit](https://popnow.ai/docs/models/photo-restorer-v1) | `popnow/photo-restorer-v1/edit` | $0.048 / image | `PopNow_popnow_photo_restorer_v1_edit` |
| [Photo Colorizer · image-edit](https://popnow.ai/docs/models/photo-colorizer-v1) | `popnow/photo-colorizer-v1/edit` | $0.06 / image | `PopNow_popnow_photo_colorizer_v1_edit` |
| [Photo to Anime · image-edit](https://popnow.ai/docs/models/photo-to-anime-v1) | `popnow/photo-to-anime-v1/edit` | $0.05 / image | `PopNow_popnow_photo_to_anime_v1_edit` |
| [Pose Changer · image-edit](https://popnow.ai/docs/models/pose-changer-v1) | `popnow/pose-changer-v1/edit` | $0.03 / image | `PopNow_popnow_pose_changer_v1_edit` |
| [Relight · image-edit](https://popnow.ai/docs/models/relight-v1) | `popnow/relight-v1/edit` | $0.03 / image | `PopNow_popnow_relight_v1_edit` |
| [Shadow Remover · image-edit](https://popnow.ai/docs/models/shadow-remover-v1) | `popnow/shadow-remover-v1/edit` | $0.03 / image | `PopNow_popnow_shadow_remover_v1_edit` |
| [Prefect Pony XL LoRA · text-to-image](https://popnow.ai/docs/models/prefect-pony-xl-lora) | `prefect/pony-xl-lora/text-to-image` | $0.024 / image | `PopNow_prefect_pony_xl_lora_text_to_image` |
| [Prefect Pony XL · text-to-image](https://popnow.ai/docs/models/prefect-pony-xl) | `prefect/pony-xl/text-to-image` | $0.015 / image | `PopNow_prefect_pony_xl_text_to_image` |
| [P-Image LoRA · image-to-image](https://popnow.ai/docs/models/p-image-lora) | `pruna-ai/p-image-lora/edit` | $0.012 / image | `PopNow_pruna_ai_p_image_lora_edit` |
| [P-Image LoRA · text-to-image](https://popnow.ai/docs/models/p-image-lora) | `pruna-ai/p-image-lora/text-to-image` | $0.006 / image | `PopNow_pruna_ai_p_image_lora_text_to_image` |
| [Recraft 20B SVG · text-to-image](https://popnow.ai/docs/models/recraft-20b-svg) | `recraft/20b-svg/text-to-image` | $0.0528 / image | `PopNow_recraft_20b_svg_text_to_image` |
| [Recraft V4 Vector · text-to-image](https://popnow.ai/docs/models/recraft-v4-vector) | `recraft/v4-vector/text-to-image` | $0.096 / image | `PopNow_recraft_v4_vector_text_to_image` |
| [Topaz Bloom · upscale](https://popnow.ai/docs/models/topaz-bloom) | `topaz/bloom/upscale` | $0.36 / image | `PopNow_topaz_bloom_upscale` |
| [Topaz Denoise & Sharpen · image-edit](https://popnow.ai/docs/models/topaz-denoise-sharpen) | `topaz/denoise-sharpen/edit` | $0.12 / image | `PopNow_topaz_denoise_sharpen_edit` |
| [Topaz Gigapixel · upscale](https://popnow.ai/docs/models/topaz-gigapixel) | `topaz/gigapixel/upscale` | $0.12 / image | `PopNow_topaz_gigapixel_upscale` |
| [Tripo H3.1 · image-to-3d](https://popnow.ai/docs/models/tripo-h3-1) | `tripo/h3.1/image-to-3d` | $0.432 / run | `PopNow_tripo_h3_1_image_to_3d` |
| [Tripo H3.1 · text-to-3d](https://popnow.ai/docs/models/tripo-h3-1) | `tripo/h3.1/text-to-3d` | $0.288 / run | `PopNow_tripo_h3_1_text_to_3d` |
| [Tripo P1 · image-to-3d](https://popnow.ai/docs/models/tripo-p1) | `tripo/p1/image-to-3d` | $0.72 / run | `PopNow_tripo_p1_image_to_3d` |

## Audio

| Node | Call name | From | Node type |
| --- | --- | --- | --- |
| [Qwen3 TTS · text-to-speech](https://popnow.ai/docs/models/qwen-3-tts) | `alibaba/qwen-3-tts/text-to-speech` | $0.068 / 1k characters | `PopNow_alibaba_qwen_3_tts_text_to_speech` |
| [Seed Audio 1.0 · text-to-audio](https://popnow.ai/docs/models/seed-audio-1-0) | `bytedance/seed-audio-1.0/text-to-audio` | $0.36 / run | `PopNow_bytedance_seed_audio_1_0_text_to_audio` |
| [Seed Speech 2.0 · text-to-speech](https://popnow.ai/docs/models/seed-speech-2-0) | `bytedance/seed-speech-2.0/text-to-speech` | $0.072 / 1k characters | `PopNow_bytedance_seed_speech_2_0_text_to_speech` |
| [Gemini 2.5 Pro TTS · text-to-speech](https://popnow.ai/docs/models/gemini-2-5-pro-tts) | `google/gemini-2.5-pro-tts/text-to-speech` | $0.00045 / second | `PopNow_google_gemini_2_5_pro_tts_text_to_speech` |
| [Gemini 3.8 Flash TTS · text-to-speech](https://popnow.ai/docs/models/gemini-3-8-flash-tts) | `google/gemini-3.8-flash-tts/text-to-speech` | $0.00032 / second | `PopNow_google_gemini_3_8_flash_tts_text_to_speech` |
| [Gemini 3.8 Flash-Lite TTS · text-to-speech](https://popnow.ai/docs/models/gemini-3-8-flash-lite-tts) | `google/gemini-3.8-flash-lite-tts/text-to-speech` | $0.00021 / second | `PopNow_google_gemini_3_8_flash_lite_tts_text_to_speech` |
| [HeartMuLa Transcribe · speech-to-text](https://popnow.ai/docs/models/heartmula-transcribe) | `heartmula/transcribe/speech-to-text` | $0.05 / run | `PopNow_heartmula_transcribe_speech_to_text` |
| [MiniMax Music 3.0 · text-to-audio](https://popnow.ai/docs/models/minimax-music-3-0) | `minimax/music-3.0/text-to-audio` | $0.18 / run | `PopNow_minimax_music_3_0_text_to_audio` |
| [MiniMax Speech 2.8 HD · text-to-speech](https://popnow.ai/docs/models/minimax-speech-2-8-hd) | `minimax/speech-2.8-hd/text-to-speech` | $0.12 / 1k characters | `PopNow_minimax_speech_2_8_hd_text_to_speech` |
| [MiniMax Speech 2.8 Turbo · text-to-speech](https://popnow.ai/docs/models/minimax-speech-2-8-turbo) | `minimax/speech-2.8-turbo/text-to-speech` | $0.072 / 1k characters | `PopNow_minimax_speech_2_8_turbo_text_to_speech` |
| [GPT Live Transcribe · realtime-transcription](https://popnow.ai/docs/models/gpt-live-transcribe) | `openai/gpt-live-transcribe/realtime-transcription` | $0.000056667 / second | `PopNow_openai_gpt_live_transcribe_realtime_transcription` |
| [GPT Transcribe · realtime-transcription](https://popnow.ai/docs/models/gpt-transcribe) | `openai/gpt-transcribe/realtime-transcription` | $0.000015 / second | `PopNow_openai_gpt_transcribe_realtime_transcription` |
| [GPT Transcribe · speech-to-text](https://popnow.ai/docs/models/gpt-transcribe) | `openai/gpt-transcribe/speech-to-text` | $0.000075 / second | `PopNow_openai_gpt_transcribe_speech_to_text` |
| [GPT-4o Mini Transcribe · speech-to-text](https://popnow.ai/docs/models/gpt-4o-mini-transcribe) | `openai/gpt-4o-mini-transcribe/speech-to-text` | $0.00005 / second | `PopNow_openai_gpt_4o_mini_transcribe_speech_to_text` |
| [GPT-4o Transcribe Diarize · speech-to-text](https://popnow.ai/docs/models/gpt-4o-transcribe-diarize) | `openai/gpt-4o-transcribe-diarize/speech-to-text` | $0.0001 / second | `PopNow_openai_gpt_4o_transcribe_diarize_speech_to_text` |
| [GPT-4o Transcribe · speech-to-text](https://popnow.ai/docs/models/gpt-4o-transcribe) | `openai/gpt-4o-transcribe/speech-to-text` | $0.0001 / second | `PopNow_openai_gpt_4o_transcribe_speech_to_text` |
| [GPT-Realtime-2.1 Mini · realtime](https://popnow.ai/docs/models/gpt-realtime-2-1-mini) | `openai/gpt-realtime-2.1-mini/realtime` | $0.00048 / 1k tokens | `PopNow_openai_gpt_realtime_2_1_mini_realtime` |
| [GPT-Realtime-2.1 · realtime](https://popnow.ai/docs/models/gpt-realtime-2-1) | `openai/gpt-realtime-2.1/realtime` | $0.0048 / 1k tokens | `PopNow_openai_gpt_realtime_2_1_realtime` |
| [TTS-1 HD · text-to-speech](https://popnow.ai/docs/models/tts-1-hd) | `openai/tts-1-hd/text-to-speech` | $0.006 / 1k characters | `PopNow_openai_tts_1_hd_text_to_speech` |
| [TTS-1 · text-to-speech](https://popnow.ai/docs/models/tts-1) | `openai/tts-1/text-to-speech` | $0.003 / 1k characters | `PopNow_openai_tts_1_text_to_speech` |
| [Whisper 1 · speech-to-text](https://popnow.ai/docs/models/whisper-1) | `openai/whisper-1/speech-to-text` | $0.0001 / second | `PopNow_openai_whisper_1_speech_to_text` |
| [Video Sound Effects · video-to-audio](https://popnow.ai/docs/models/foley-v1) | `popnow/foley-v1/video-to-audio` | $0.0012 / second | `PopNow_popnow_foley_v1_video_to_audio` |
| [Vocal Isolator · audio-separation](https://popnow.ai/docs/models/vocal-isolator-v1) | `popnow/vocal-isolator-v1/audio-separation` | $0.0012 / second | `PopNow_popnow_vocal_isolator_v1_audio_separation` |
| [Voice Cleaner · audio-to-audio](https://popnow.ai/docs/models/voice-cleaner-v1) | `popnow/voice-cleaner-v1/audio-to-audio` | $0.00028 / second | `PopNow_popnow_voice_cleaner_v1_audio_to_audio` |
| [Chatterbox · text-to-speech](https://popnow.ai/docs/models/chatterbox-v1) | `resemble-ai/chatterbox-v1/text-to-speech` | $0.036 / run | `PopNow_resemble_ai_chatterbox_v1_text_to_speech` |
| [Suno v6 Mini · text-to-audio](https://popnow.ai/docs/models/suno-v6-mini) | `suno/v6-mini/text-to-audio` | $0.072 / run | `PopNow_suno_v6_mini_text_to_audio` |
| [Suno v6 Wild · text-to-audio](https://popnow.ai/docs/models/suno-v6-wild) | `suno/v6-wild/text-to-audio` | $0.072 / run | `PopNow_suno_v6_wild_text_to_audio` |
| [Suno v6 · text-to-audio](https://popnow.ai/docs/models/suno-v6) | `suno/v6/text-to-audio` | $0.072 / run | `PopNow_suno_v6_text_to_audio` |
| [Grok STT · speech-to-text](https://popnow.ai/docs/models/grok-stt) | `xai/grok-stt/speech-to-text` | $0.000033334 / second | `PopNow_xai_grok_stt_speech_to_text` |
| [Grok TTS · text-to-speech](https://popnow.ai/docs/models/grok-tts) | `xai/grok-tts/text-to-speech` | $0.018 / 1k characters | `PopNow_xai_grok_tts_text_to_speech` |

## Text and vectors

| Node | Call name | From | Node type |
| --- | --- | --- | --- |
| [text-embedding-3-large · embedding](https://popnow.ai/docs/models/text-embedding-3-large) | `openai/text-embedding-3-large/embedding` | $0.000026 / 1k tokens | `PopNow_openai_text_embedding_3_large_embedding` |
| [text-embedding-3-small · embedding](https://popnow.ai/docs/models/text-embedding-3-small) | `openai/text-embedding-3-small/embedding` | $0.000004 / 1k tokens | `PopNow_openai_text_embedding_3_small_embedding` |
| [text-embedding-ada-002 · embedding](https://popnow.ai/docs/models/text-embedding-ada-002) | `openai/text-embedding-ada-002/embedding` | $0.00002 / 1k tokens | `PopNow_openai_text_embedding_ada_002_embedding` |
