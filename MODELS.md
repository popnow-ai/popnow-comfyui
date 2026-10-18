# PopNow models available as ComfyUI nodes

248 PopNow models, one ComfyUI node each: 115 video, 116 image and 17 audio. Any of them can also be called by name from the **PopNow Generate** node.

The list is generated from the model catalog bundled with this release. ComfyUI loads the live catalog at startup once an API key is set, so models added since then appear after a restart.
Prices are starting prices in credits (1 credit = $0.01); the badge on each node shows the rate for the options you pick.

## Video

| Node | Call name | From | Node type |
| --- | --- | --- | --- |
| [HappyHorse 1.1 · Image to Video](https://popnow.ai/docs/models/happyhorse-1-1) | `alibaba/happyhorse-1.1/image-to-video` | 21 credits / second | `PopNow_alibaba_happyhorse_1_1_image_to_video` |
| [HappyHorse 1.1 · Reference to Video](https://popnow.ai/docs/models/happyhorse-1-1) | `alibaba/happyhorse-1.1/reference-to-video` | 21 credits / second | `PopNow_alibaba_happyhorse_1_1_reference_to_video` |
| [HappyHorse 1.1 · Text to Video](https://popnow.ai/docs/models/happyhorse-1-1) | `alibaba/happyhorse-1.1/text-to-video` | 21 credits / second | `PopNow_alibaba_happyhorse_1_1_text_to_video` |
| [Wan 2.1 LoRA · Image to Video](https://popnow.ai/docs/models/wan-2-1-lora) | `alibaba/wan-2.1-lora/image-to-video` | 36 credits / run | `PopNow_alibaba_wan_2_1_lora_image_to_video` |
| [Wan 2.1 LoRA · Text to Video](https://popnow.ai/docs/models/wan-2-1-lora) | `alibaba/wan-2.1-lora/text-to-video` | 36 credits / run | `PopNow_alibaba_wan_2_1_lora_text_to_video` |
| [Wan 2.1 LoRA · Video Edit](https://popnow.ai/docs/models/wan-2-1-lora) | `alibaba/wan-2.1-lora/video-edit` | 36 credits / run | `PopNow_alibaba_wan_2_1_lora_video_edit` |
| [Wan 2.2 5B LoRA · Image to Video](https://popnow.ai/docs/models/wan-2-2-5b-lora) | `alibaba/wan-2.2-5b-lora/image-to-video` | 18 credits / run | `PopNow_alibaba_wan_2_2_5b_lora_image_to_video` |
| [Wan 2.2 5B LoRA · Text to Video](https://popnow.ai/docs/models/wan-2-2-5b-lora) | `alibaba/wan-2.2-5b-lora/text-to-video` | 18 credits / run | `PopNow_alibaba_wan_2_2_5b_lora_text_to_video` |
| [Wan 2.2 Animate · Character Animation](https://popnow.ai/docs/models/wan-2-2-animate) | `alibaba/wan-2.2-animate/character-animation` | 7.95 credits / second | `PopNow_alibaba_wan_2_2_animate_character_animation` |
| [Wan 2.2 LoRA · Image to Video](https://popnow.ai/docs/models/wan-2-2-lora) | `alibaba/wan-2.2-lora/image-to-video` | 3.6 credits / second | `PopNow_alibaba_wan_2_2_lora_image_to_video` |
| [Wan 2.2 LoRA · Text to Video](https://popnow.ai/docs/models/wan-2-2-lora) | `alibaba/wan-2.2-lora/text-to-video` | 7.2 credits / second | `PopNow_alibaba_wan_2_2_lora_text_to_video` |
| [Wan 2.2 LoRA · Video Extend](https://popnow.ai/docs/models/wan-2-2-lora) | `alibaba/wan-2.2-lora/video-extend` | 3.6 credits / second | `PopNow_alibaba_wan_2_2_lora_video_extend` |
| [Wan 2.2 · Image to Video](https://popnow.ai/docs/models/wan-2-2) | `alibaba/wan-2.2/image-to-video` | 36 credits / run | `PopNow_alibaba_wan_2_2_image_to_video` |
| [Wan 2.2 · Text to Video](https://popnow.ai/docs/models/wan-2-2) | `alibaba/wan-2.2/text-to-video` | 36 credits / run | `PopNow_alibaba_wan_2_2_text_to_video` |
| [Wan 2.5 · Image to Video](https://popnow.ai/docs/models/wan-2-5) | `alibaba/wan-2.5/image-to-video` | 6.75 credits / second | `PopNow_alibaba_wan_2_5_image_to_video` |
| [Wan 2.5 · Text to Video](https://popnow.ai/docs/models/wan-2-5) | `alibaba/wan-2.5/text-to-video` | 6.75 credits / second | `PopNow_alibaba_wan_2_5_text_to_video` |
| [Wan 2.5 · Video Extend](https://popnow.ai/docs/models/wan-2-5) | `alibaba/wan-2.5/video-extend` | 6.75 credits / second | `PopNow_alibaba_wan_2_5_video_extend` |
| [Wan 2.6 Flash · Image to Video](https://popnow.ai/docs/models/wan-2-6-flash) | `alibaba/wan-2.6-flash/image-to-video` | 3.38 credits / second | `PopNow_alibaba_wan_2_6_flash_image_to_video` |
| [Wan 2.6 Flash · Reference to Video](https://popnow.ai/docs/models/wan-2-6-flash) | `alibaba/wan-2.6-flash/reference-to-video` | 3.38 credits / second | `PopNow_alibaba_wan_2_6_flash_reference_to_video` |
| [Wan 2.6 · Image to Video](https://popnow.ai/docs/models/wan-2-6) | `alibaba/wan-2.6/image-to-video` | 13.5 credits / second | `PopNow_alibaba_wan_2_6_image_to_video` |
| [Wan 2.6 · Reference to Video](https://popnow.ai/docs/models/wan-2-6) | `alibaba/wan-2.6/reference-to-video` | 9.75 credits / second | `PopNow_alibaba_wan_2_6_reference_to_video` |
| [Wan 2.6 · Text to Video](https://popnow.ai/docs/models/wan-2-6) | `alibaba/wan-2.6/text-to-video` | 13.5 credits / second | `PopNow_alibaba_wan_2_6_text_to_video` |
| [Wan 3.0 Prime · Image to Video](https://popnow.ai/docs/models/wan-3-0-prime) | `alibaba/wan-3.0-prime/image-to-video` | 9.18 credits / second | `PopNow_alibaba_wan_3_0_prime_image_to_video` |
| [Wan 3.0 Prime · Reference to Video](https://popnow.ai/docs/models/wan-3-0-prime) | `alibaba/wan-3.0-prime/reference-to-video` | 9.18 credits / second | `PopNow_alibaba_wan_3_0_prime_reference_to_video` |
| [Wan 3.0 Prime · Text to Video](https://popnow.ai/docs/models/wan-3-0-prime) | `alibaba/wan-3.0-prime/text-to-video` | 9.18 credits / second | `PopNow_alibaba_wan_3_0_prime_text_to_video` |
| [Wan 3.0 Prime · Video Extend](https://popnow.ai/docs/models/wan-3-0-prime) | `alibaba/wan-3.0-prime/video-extend` | 9.18 credits / second | `PopNow_alibaba_wan_3_0_prime_video_extend` |
| [Wan 3.0 Pro Prime · Image to Video](https://popnow.ai/docs/models/wan-3-0-pro-prime) | `alibaba/wan-3.0-pro-prime/image-to-video` | 35.1 credits / second | `PopNow_alibaba_wan_3_0_pro_prime_image_to_video` |
| [Wan 3.0 Pro Prime · Reference to Video](https://popnow.ai/docs/models/wan-3-0-pro-prime) | `alibaba/wan-3.0-pro-prime/reference-to-video` | 35.1 credits / second | `PopNow_alibaba_wan_3_0_pro_prime_reference_to_video` |
| [Wan 3.0 Pro Prime · Text to Video](https://popnow.ai/docs/models/wan-3-0-pro-prime) | `alibaba/wan-3.0-pro-prime/text-to-video` | 35.1 credits / second | `PopNow_alibaba_wan_3_0_pro_prime_text_to_video` |
| [Wan 3.0 Pro Prime · Video Extend](https://popnow.ai/docs/models/wan-3-0-pro-prime) | `alibaba/wan-3.0-pro-prime/video-extend` | 35.1 credits / second | `PopNow_alibaba_wan_3_0_pro_prime_video_extend` |
| [Wan 3.0 Pro · Image to Video](https://popnow.ai/docs/models/wan-3-0-pro) | `alibaba/wan-3.0-pro/image-to-video` | 21.6 credits / second | `PopNow_alibaba_wan_3_0_pro_image_to_video` |
| [Wan 3.0 Pro · Reference to Video](https://popnow.ai/docs/models/wan-3-0-pro) | `alibaba/wan-3.0-pro/reference-to-video` | 21.6 credits / second | `PopNow_alibaba_wan_3_0_pro_reference_to_video` |
| [Wan 3.0 Pro · Text to Video](https://popnow.ai/docs/models/wan-3-0-pro) | `alibaba/wan-3.0-pro/text-to-video` | 21.6 credits / second | `PopNow_alibaba_wan_3_0_pro_text_to_video` |
| [Wan 3.0 Pro · Video Extend](https://popnow.ai/docs/models/wan-3-0-pro) | `alibaba/wan-3.0-pro/video-extend` | 21.6 credits / second | `PopNow_alibaba_wan_3_0_pro_video_extend` |
| [Wan 3.0 · Image to Video](https://popnow.ai/docs/models/wan-3-0) | `alibaba/wan-3.0/image-to-video` | 6.75 credits / second | `PopNow_alibaba_wan_3_0_image_to_video` |
| [Wan 3.0 · Reference to Video](https://popnow.ai/docs/models/wan-3-0) | `alibaba/wan-3.0/reference-to-video` | 6.75 credits / second | `PopNow_alibaba_wan_3_0_reference_to_video` |
| [Wan 3.0 · Text to Video](https://popnow.ai/docs/models/wan-3-0) | `alibaba/wan-3.0/text-to-video` | 6.75 credits / second | `PopNow_alibaba_wan_3_0_text_to_video` |
| [Wan 3.0 · Video Extend](https://popnow.ai/docs/models/wan-3-0) | `alibaba/wan-3.0/video-extend` | 6.75 credits / second | `PopNow_alibaba_wan_3_0_video_extend` |
| [FLUX 3 · Image to Video](https://popnow.ai/docs/models/flux-3) | `black-forest-labs/flux-3/image-to-video` | 9 credits / second | `PopNow_black_forest_labs_flux_3_image_to_video` |
| [FLUX 3 · Text to Video](https://popnow.ai/docs/models/flux-3) | `black-forest-labs/flux-3/text-to-video` | 9 credits / second | `PopNow_black_forest_labs_flux_3_text_to_video` |
| [FLUX 3 · Upscale](https://popnow.ai/docs/models/flux-3) | `black-forest-labs/flux-3/upscale` | 79.2 credits / second | `PopNow_black_forest_labs_flux_3_upscale` |
| [FLUX 3 · Video Extend](https://popnow.ai/docs/models/flux-3) | `black-forest-labs/flux-3/video-extend` | 18 credits / second | `PopNow_black_forest_labs_flux_3_video_extend` |
| [Seedance 1.5 Pro · Image to Video](https://popnow.ai/docs/models/seedance-1-5-pro) | `bytedance/seedance-1.5-pro/image-to-video` | 1.68 credits / second | `PopNow_bytedance_seedance_1_5_pro_image_to_video` |
| [Seedance 1.5 Pro · Text to Video](https://popnow.ai/docs/models/seedance-1-5-pro) | `bytedance/seedance-1.5-pro/text-to-video` | 1.68 credits / second | `PopNow_bytedance_seedance_1_5_pro_text_to_video` |
| [Seedance 1.5 Pro · Video Extend](https://popnow.ai/docs/models/seedance-1-5-pro) | `bytedance/seedance-1.5-pro/video-extend` | 1.68 credits / second | `PopNow_bytedance_seedance_1_5_pro_video_extend` |
| [Seedance 2.0 Fast · Image to Video](https://popnow.ai/docs/models/seedance-2-0-fast) | `bytedance/seedance-2.0-fast/image-to-video` | 6.75 credits / second | `PopNow_bytedance_seedance_2_0_fast_image_to_video` |
| [Seedance 2.0 Fast · Reference to Video](https://popnow.ai/docs/models/seedance-2-0-fast) | `bytedance/seedance-2.0-fast/reference-to-video` | 3.38 credits / second | `PopNow_bytedance_seedance_2_0_fast_reference_to_video` |
| [Seedance 2.0 Fast · Text to Video](https://popnow.ai/docs/models/seedance-2-0-fast) | `bytedance/seedance-2.0-fast/text-to-video` | 6.75 credits / second | `PopNow_bytedance_seedance_2_0_fast_text_to_video` |
| [Seedance 2.0 Fast · Video Extend](https://popnow.ai/docs/models/seedance-2-0-fast) | `bytedance/seedance-2.0-fast/video-extend` | 6.75 credits / second | `PopNow_bytedance_seedance_2_0_fast_video_extend` |
| [Seedance 2.0 Mini · Image to Video](https://popnow.ai/docs/models/seedance-2-0-mini) | `bytedance/seedance-2.0-mini/image-to-video` | 3.69 credits / second | `PopNow_bytedance_seedance_2_0_mini_image_to_video` |
| [Seedance 2.0 Mini · Reference to Video](https://popnow.ai/docs/models/seedance-2-0-mini) | `bytedance/seedance-2.0-mini/reference-to-video` | 1.65 credits / second | `PopNow_bytedance_seedance_2_0_mini_reference_to_video` |
| [Seedance 2.0 Mini · Text to Video](https://popnow.ai/docs/models/seedance-2-0-mini) | `bytedance/seedance-2.0-mini/text-to-video` | 3.69 credits / second | `PopNow_bytedance_seedance_2_0_mini_text_to_video` |
| [Seedance 2.0 Mini · Video Extend](https://popnow.ai/docs/models/seedance-2-0-mini) | `bytedance/seedance-2.0-mini/video-extend` | 3.69 credits / second | `PopNow_bytedance_seedance_2_0_mini_video_extend` |
| [Seedance 2.0 · Image to Video](https://popnow.ai/docs/models/seedance-2-0) | `bytedance/seedance-2.0/image-to-video` | 10.5 credits / second | `PopNow_bytedance_seedance_2_0_image_to_video` |
| [Seedance 2.0 · Reference to Video](https://popnow.ai/docs/models/seedance-2-0) | `bytedance/seedance-2.0/reference-to-video` | 6.47 credits / second | `PopNow_bytedance_seedance_2_0_reference_to_video` |
| [Seedance 2.0 · Text to Video](https://popnow.ai/docs/models/seedance-2-0) | `bytedance/seedance-2.0/text-to-video` | 10.5 credits / second | `PopNow_bytedance_seedance_2_0_text_to_video` |
| [Seedance 2.0 · Video Extend](https://popnow.ai/docs/models/seedance-2-0) | `bytedance/seedance-2.0/video-extend` | 10.5 credits / second | `PopNow_bytedance_seedance_2_0_video_extend` |
| [Seedance 2.5 · Image to Video](https://popnow.ai/docs/models/seedance-2-5) | `bytedance/seedance-2.5/image-to-video` | 18.51 credits / second | `PopNow_bytedance_seedance_2_5_image_to_video` |
| [Seedance 2.5 · Reference to Video](https://popnow.ai/docs/models/seedance-2-5) | `bytedance/seedance-2.5/reference-to-video` | 11.07 credits / second | `PopNow_bytedance_seedance_2_5_reference_to_video` |
| [Seedance 2.5 · Text to Video](https://popnow.ai/docs/models/seedance-2-5) | `bytedance/seedance-2.5/text-to-video` | 18.51 credits / second | `PopNow_bytedance_seedance_2_5_text_to_video` |
| [Seedance 2.5 · Video Extend](https://popnow.ai/docs/models/seedance-2-5) | `bytedance/seedance-2.5/video-extend` | 11.07 credits / second | `PopNow_bytedance_seedance_2_5_video_extend` |
| [Kling 2.1 Master · Image to Video](https://popnow.ai/docs/models/kling-2-1-master) | `kling/2.1-master/image-to-video` | 32.4 credits / second | `PopNow_kling_2_1_master_image_to_video` |
| [Kling 2.1 Master · Text to Video](https://popnow.ai/docs/models/kling-2-1-master) | `kling/2.1-master/text-to-video` | 32.4 credits / second | `PopNow_kling_2_1_master_text_to_video` |
| [Kling 2.1 · Image to Video](https://popnow.ai/docs/models/kling-2-1) | `kling/2.1/image-to-video` | 5.25 credits / second | `PopNow_kling_2_1_image_to_video` |
| [Kling 2.5 Turbo · Image to Video](https://popnow.ai/docs/models/kling-2-5-turbo) | `kling/2.5-turbo/image-to-video` | 8.4 credits / second | `PopNow_kling_2_5_turbo_image_to_video` |
| [Kling 2.5 Turbo · Text to Video](https://popnow.ai/docs/models/kling-2-5-turbo) | `kling/2.5-turbo/text-to-video` | 8.4 credits / second | `PopNow_kling_2_5_turbo_text_to_video` |
| [Kling 2.6 · Character Animation](https://popnow.ai/docs/models/kling-2-6) | `kling/2.6/character-animation` | 10.35 credits / second | `PopNow_kling_2_6_character_animation` |
| [Kling 2.6 · Image to Video](https://popnow.ai/docs/models/kling-2-6) | `kling/2.6/image-to-video` | 10.35 credits / second | `PopNow_kling_2_6_image_to_video` |
| [Kling 2.6 · Text to Video](https://popnow.ai/docs/models/kling-2-6) | `kling/2.6/text-to-video` | 10.35 credits / second | `PopNow_kling_2_6_text_to_video` |
| [Kling 3.0 Turbo · Image to Video](https://popnow.ai/docs/models/kling-3-0-turbo) | `kling/3.0-turbo/image-to-video` | 16.8 credits / second | `PopNow_kling_3_0_turbo_image_to_video` |
| [Kling 3.0 Turbo · Text to Video](https://popnow.ai/docs/models/kling-3-0-turbo) | `kling/3.0-turbo/text-to-video` | 16.8 credits / second | `PopNow_kling_3_0_turbo_text_to_video` |
| [Kling 3.0 · Character Animation](https://popnow.ai/docs/models/kling-3-0) | `kling/3.0/character-animation` | 15.12 credits / second | `PopNow_kling_3_0_character_animation` |
| [Kling 3.0 · Image to Video](https://popnow.ai/docs/models/kling-3-0) | `kling/3.0/image-to-video` | 10.08 credits / second | `PopNow_kling_3_0_image_to_video` |
| [Kling 3.0 · Text to Video](https://popnow.ai/docs/models/kling-3-0) | `kling/3.0/text-to-video` | 10.08 credits / second | `PopNow_kling_3_0_text_to_video` |
| [Kling 4.0 · Image to Video](https://popnow.ai/docs/models/kling-4-0) | `kling/4.0/image-to-video` | 32.4 credits / second | `PopNow_kling_4_0_image_to_video` |
| [Kling 4.0 · Reference to Video](https://popnow.ai/docs/models/kling-4-0) | `kling/4.0/reference-to-video` | 32.4 credits / second | `PopNow_kling_4_0_reference_to_video` |
| [Kling 4.0 · Text to Video](https://popnow.ai/docs/models/kling-4-0) | `kling/4.0/text-to-video` | 32.4 credits / second | `PopNow_kling_4_0_text_to_video` |
| [Kling O3 · Image to Video](https://popnow.ai/docs/models/kling-o3) | `kling/o3/image-to-video` | 10.08 credits / second | `PopNow_kling_o3_image_to_video` |
| [Kling O3 · Reference to Video](https://popnow.ai/docs/models/kling-o3) | `kling/o3/reference-to-video` | 10.08 credits / second | `PopNow_kling_o3_reference_to_video` |
| [Kling O3 · Text to Video](https://popnow.ai/docs/models/kling-o3) | `kling/o3/text-to-video` | 10.08 credits / second | `PopNow_kling_o3_text_to_video` |
| [Kling O3 · Video Edit](https://popnow.ai/docs/models/kling-o3) | `kling/o3/video-edit` | 18.78 credits / second | `PopNow_kling_o3_video_edit` |
| [LTX 2.5 · Image to Video](https://popnow.ai/docs/models/ltx-2-5) | `lightricks/ltx-2.5/image-to-video` | 13.5 credits / second | `PopNow_lightricks_ltx_2_5_image_to_video` |
| [LTX 2.5 · Text to Video](https://popnow.ai/docs/models/ltx-2-5) | `lightricks/ltx-2.5/text-to-video` | 13.5 credits / second | `PopNow_lightricks_ltx_2_5_text_to_video` |
| [LTX-2 19B LoRA · Image to Video](https://popnow.ai/docs/models/ltx-2-19b-lora) | `lightricks/ltx-2-19b-lora/image-to-video` | 2.7 credits / second | `PopNow_lightricks_ltx_2_19b_lora_image_to_video` |
| [LTX-2 19B LoRA · Text to Video](https://popnow.ai/docs/models/ltx-2-19b-lora) | `lightricks/ltx-2-19b-lora/text-to-video` | 2.7 credits / second | `PopNow_lightricks_ltx_2_19b_lora_text_to_video` |
| [LTX-2 19B · Image to Video](https://popnow.ai/docs/models/ltx-2-19b) | `lightricks/ltx-2-19b/image-to-video` | 2.16 credits / second | `PopNow_lightricks_ltx_2_19b_image_to_video` |
| [LTX-2 19B · Text to Video](https://popnow.ai/docs/models/ltx-2-19b) | `lightricks/ltx-2-19b/text-to-video` | 2.16 credits / second | `PopNow_lightricks_ltx_2_19b_text_to_video` |
| [LTX-2 19B · Video Extend](https://popnow.ai/docs/models/ltx-2-19b) | `lightricks/ltx-2-19b/video-extend` | 2.16 credits / second | `PopNow_lightricks_ltx_2_19b_video_extend` |
| [LTX-2.3 LoRA · Image to Video](https://popnow.ai/docs/models/ltx-2-3-lora) | `lightricks/ltx-2.3-lora/image-to-video` | 3.6 credits / second | `PopNow_lightricks_ltx_2_3_lora_image_to_video` |
| [LTX-2.3 LoRA · Text to Video](https://popnow.ai/docs/models/ltx-2-3-lora) | `lightricks/ltx-2.3-lora/text-to-video` | 3.6 credits / second | `PopNow_lightricks_ltx_2_3_lora_text_to_video` |
| [MiniMax H3 360 Orbit · Image to Video](https://popnow.ai/docs/models/minimax-h3-360-orbit) | `minimax/h3-360-orbit/image-to-video` | 7.5 credits / second | `PopNow_minimax_h3_360_orbit_image_to_video` |
| [MiniMax H3 LoRA · Image to Video](https://popnow.ai/docs/models/minimax-h3-lora) | `minimax/h3-lora/image-to-video` | 7.5 credits / second | `PopNow_minimax_h3_lora_image_to_video` |
| [MiniMax H3 LoRA · Reference to Video](https://popnow.ai/docs/models/minimax-h3-lora) | `minimax/h3-lora/reference-to-video` | 9 credits / second | `PopNow_minimax_h3_lora_reference_to_video` |
| [MiniMax H3 LoRA · Text to Video](https://popnow.ai/docs/models/minimax-h3-lora) | `minimax/h3-lora/text-to-video` | 7.5 credits / second | `PopNow_minimax_h3_lora_text_to_video` |
| [MiniMax H3 LoRA · Video Extend](https://popnow.ai/docs/models/minimax-h3-lora) | `minimax/h3-lora/video-extend` | 7.5 credits / second | `PopNow_minimax_h3_lora_video_extend` |
| [MiniMax H3 Max · Image to Video](https://popnow.ai/docs/models/minimax-h3-max) | `minimax/h3-max/image-to-video` | 7.5 credits / second | `PopNow_minimax_h3_max_image_to_video` |
| [MiniMax H3 Max · Text to Video](https://popnow.ai/docs/models/minimax-h3-max) | `minimax/h3-max/text-to-video` | 7.5 credits / second | `PopNow_minimax_h3_max_text_to_video` |
| [MiniMax H3 Max · Video Extend](https://popnow.ai/docs/models/minimax-h3-max) | `minimax/h3-max/video-extend` | 7.5 credits / second | `PopNow_minimax_h3_max_video_extend` |
| [MiniMax H3 Singularity LoRA · Image to Video](https://popnow.ai/docs/models/minimax-h3-singularity-lora) | `minimax/h3-singularity-lora/image-to-video` | 9.38 credits / second | `PopNow_minimax_h3_singularity_lora_image_to_video` |
| [MiniMax H3 Singularity LoRA · Reference to Video](https://popnow.ai/docs/models/minimax-h3-singularity-lora) | `minimax/h3-singularity-lora/reference-to-video` | 9 credits / second | `PopNow_minimax_h3_singularity_lora_reference_to_video` |
| [MiniMax H3 Singularity LoRA · Video Extend](https://popnow.ai/docs/models/minimax-h3-singularity-lora) | `minimax/h3-singularity-lora/video-extend` | 9.38 credits / second | `PopNow_minimax_h3_singularity_lora_video_extend` |
| [MiniMax H3 · Image to Video](https://popnow.ai/docs/models/minimax-h3) | `minimax/h3/image-to-video` | 5.55 credits / second | `PopNow_minimax_h3_image_to_video` |
| [MiniMax H3 · Reference to Video](https://popnow.ai/docs/models/minimax-h3) | `minimax/h3/reference-to-video` | 5.55 credits / second | `PopNow_minimax_h3_reference_to_video` |
| [MiniMax H3 · Text to Video](https://popnow.ai/docs/models/minimax-h3) | `minimax/h3/text-to-video` | 5.55 credits / second | `PopNow_minimax_h3_text_to_video` |
| [MiniMax H3 · Video Extend](https://popnow.ai/docs/models/minimax-h3) | `minimax/h3/video-extend` | 5.55 credits / second | `PopNow_minimax_h3_video_extend` |
| [Video Upscaler · Upscale](https://popnow.ai/docs/models/video-upscaler-v1) | `popnow/video-upscaler-v1/upscale` | 0.9 credits / second | `PopNow_popnow_video_upscaler_v1_upscale` |
| [HunyuanVideo 1.5 · Image to Video](https://popnow.ai/docs/models/hunyuan-video-1-5) | `tencent/hunyuan-video-1.5/image-to-video` | 3.6 credits / second | `PopNow_tencent_hunyuan_video_1_5_image_to_video` |
| [HunyuanVideo 1.5 · Text to Video](https://popnow.ai/docs/models/hunyuan-video-1-5) | `tencent/hunyuan-video-1.5/text-to-video` | 3.6 credits / second | `PopNow_tencent_hunyuan_video_1_5_text_to_video` |
| [Vidu Q3 Pro · Image to Video](https://popnow.ai/docs/models/vidu-q3-pro) | `vidu/q3-pro/image-to-video` | 8.1 credits / second | `PopNow_vidu_q3_pro_image_to_video` |
| [Vidu Q3 Turbo · Image to Video](https://popnow.ai/docs/models/vidu-q3-turbo) | `vidu/q3-turbo/image-to-video` | 6.3 credits / second | `PopNow_vidu_q3_turbo_image_to_video` |
| [Vidu Q3 Turbo · Video Extend](https://popnow.ai/docs/models/vidu-q3-turbo) | `vidu/q3-turbo/video-extend` | 6.3 credits / second | `PopNow_vidu_q3_turbo_video_extend` |
| [Vidu Q3 · Image to Video](https://popnow.ai/docs/models/vidu-q3) | `vidu/q3/image-to-video` | 10.5 credits / second | `PopNow_vidu_q3_image_to_video` |
| [Vidu Q4 Preview · Image to Video](https://popnow.ai/docs/models/vidu-q4-preview) | `vidu/q4-preview/image-to-video` | 6.75 credits / second | `PopNow_vidu_q4_preview_image_to_video` |
| [Vidu Q4 Preview · Reference to Video](https://popnow.ai/docs/models/vidu-q4-preview) | `vidu/q4-preview/reference-to-video` | 6.75 credits / second | `PopNow_vidu_q4_preview_reference_to_video` |
| [Vidu Q4 Preview · Video Extend](https://popnow.ai/docs/models/vidu-q4-preview) | `vidu/q4-preview/video-extend` | 6.75 credits / second | `PopNow_vidu_q4_preview_video_extend` |

## Image

| Node | Call name | From | Node type |
| --- | --- | --- | --- |
| [Qwen Image 1.0 LoRA · Edit](https://popnow.ai/docs/models/qwen-image-1-0-lora) | `alibaba/qwen-image-1.0-lora/edit` | 4.5 credits / image | `PopNow_alibaba_qwen_image_1_0_lora_edit` |
| [Qwen Image 1.0 LoRA · Text to Image](https://popnow.ai/docs/models/qwen-image-1-0-lora) | `alibaba/qwen-image-1.0-lora/text-to-image` | 4.5 credits / image | `PopNow_alibaba_qwen_image_1_0_lora_text_to_image` |
| [Qwen Image 2 · Edit](https://popnow.ai/docs/models/alibaba-qwen-image-2) | `alibaba/qwen-image-2/edit` | 5.25 credits / image | `PopNow_alibaba_qwen_image_2_edit` |
| [Qwen Image 2 · Text to Image](https://popnow.ai/docs/models/alibaba-qwen-image-2) | `alibaba/qwen-image-2/text-to-image` | 5.25 credits / image | `PopNow_alibaba_qwen_image_2_text_to_image` |
| [Qwen Image 2.1 LoRA · Edit](https://popnow.ai/docs/models/qwen-image-2-1-lora) | `alibaba/qwen-image-2.1-lora/edit` | 6.3 credits / image | `PopNow_alibaba_qwen_image_2_1_lora_edit` |
| [Qwen Image 2.1 LoRA · Text to Image](https://popnow.ai/docs/models/qwen-image-2-1-lora) | `alibaba/qwen-image-2.1-lora/text-to-image` | 4.5 credits / image | `PopNow_alibaba_qwen_image_2_1_lora_text_to_image` |
| [Qwen Image 2.1 Pro · Edit](https://popnow.ai/docs/models/qwen-image-2-1-pro) | `alibaba/qwen-image-2.1-pro/edit` | 5.4 credits / image | `PopNow_alibaba_qwen_image_2_1_pro_edit` |
| [Qwen Image 2.1 Pro · Text to Image](https://popnow.ai/docs/models/qwen-image-2-1-pro) | `alibaba/qwen-image-2.1-pro/text-to-image` | 5.4 credits / image | `PopNow_alibaba_qwen_image_2_1_pro_text_to_image` |
| [Qwen Image 2.1 Turbo · Edit](https://popnow.ai/docs/models/qwen-image-2-1-turbo) | `alibaba/qwen-image-2.1-turbo/edit` | 2.16 credits / image | `PopNow_alibaba_qwen_image_2_1_turbo_edit` |
| [Qwen Image 2.1 Turbo · Text to Image](https://popnow.ai/docs/models/qwen-image-2-1-turbo) | `alibaba/qwen-image-2.1-turbo/text-to-image` | 2.16 credits / image | `PopNow_alibaba_qwen_image_2_1_turbo_text_to_image` |
| [Qwen Image 2.1 · Edit](https://popnow.ai/docs/models/qwen-image-2-1) | `alibaba/qwen-image-2.1/edit` | 5.4 credits / image | `PopNow_alibaba_qwen_image_2_1_edit` |
| [Qwen Image 2.1 · Text to Image](https://popnow.ai/docs/models/qwen-image-2-1) | `alibaba/qwen-image-2.1/text-to-image` | 3.6 credits / image | `PopNow_alibaba_qwen_image_2_1_text_to_image` |
| [Qwen Image 2512 LoRA · Edit](https://popnow.ai/docs/models/qwen-image-2512-lora) | `alibaba/qwen-image-2512-lora/edit` | 4.5 credits / image | `PopNow_alibaba_qwen_image_2512_lora_edit` |
| [Qwen Image 2512 LoRA · Text to Image](https://popnow.ai/docs/models/qwen-image-2512-lora) | `alibaba/qwen-image-2512-lora/text-to-image` | 4.5 credits / image | `PopNow_alibaba_qwen_image_2512_lora_text_to_image` |
| [Qwen Image 3.0 Pro · Edit](https://popnow.ai/docs/models/qwen-image-3-0-pro) | `alibaba/qwen-image-3.0-pro/edit` | 6 credits / image | `PopNow_alibaba_qwen_image_3_0_pro_edit` |
| [Qwen Image 3.0 Pro · Text to Image](https://popnow.ai/docs/models/qwen-image-3-0-pro) | `alibaba/qwen-image-3.0-pro/text-to-image` | 6 credits / image | `PopNow_alibaba_qwen_image_3_0_pro_text_to_image` |
| [Qwen Image 3.0 · Edit](https://popnow.ai/docs/models/qwen-image-3-0) | `alibaba/qwen-image-3.0/edit` | 4.5 credits / image | `PopNow_alibaba_qwen_image_3_0_edit` |
| [Qwen Image 3.0 · Text to Image](https://popnow.ai/docs/models/qwen-image-3-0) | `alibaba/qwen-image-3.0/text-to-image` | 4.5 credits / image | `PopNow_alibaba_qwen_image_3_0_text_to_image` |
| [Qwen Image Edit 2509 LoRA · Edit](https://popnow.ai/docs/models/qwen-image-edit-2509-lora) | `alibaba/qwen-image-edit-2509-lora/edit` | 4.5 credits / image | `PopNow_alibaba_qwen_image_edit_2509_lora_edit` |
| [Wan 2.1 Image LoRA · Edit](https://popnow.ai/docs/models/wan-2-1-image-lora) | `alibaba/wan-2.1-image-lora/edit` | 4.5 credits / image | `PopNow_alibaba_wan_2_1_image_lora_edit` |
| [Wan 2.1 Image LoRA · Text to Image](https://popnow.ai/docs/models/wan-2-1-image-lora) | `alibaba/wan-2.1-image-lora/text-to-image` | 4.5 credits / image | `PopNow_alibaba_wan_2_1_image_lora_text_to_image` |
| [Wan 2.2 Image LoRA · Text to Image](https://popnow.ai/docs/models/wan-2-2-image-lora) | `alibaba/wan-2.2-image-lora/text-to-image` | 4.5 credits / image | `PopNow_alibaba_wan_2_2_image_lora_text_to_image` |
| [Wan 2.7 Pro · Edit](https://popnow.ai/docs/models/wan-2-7-pro) | `alibaba/wan-2.7-pro/edit` | 11.25 credits / image | `PopNow_alibaba_wan_2_7_pro_edit` |
| [Wan 2.7 Pro · Text to Image](https://popnow.ai/docs/models/wan-2-7-pro) | `alibaba/wan-2.7-pro/text-to-image` | 11.25 credits / image | `PopNow_alibaba_wan_2_7_pro_text_to_image` |
| [Wan 2.7 · Edit](https://popnow.ai/docs/models/wan-2-7) | `alibaba/wan-2.7/edit` | 4.5 credits / image | `PopNow_alibaba_wan_2_7_edit` |
| [Wan 2.7 · Text to Image](https://popnow.ai/docs/models/wan-2-7) | `alibaba/wan-2.7/text-to-image` | 4.5 credits / image | `PopNow_alibaba_wan_2_7_text_to_image` |
| [Z-Image Base LoRA · Edit](https://popnow.ai/docs/models/z-image-base-lora) | `alibaba/z-image-base-lora/edit` | 2.16 credits / image | `PopNow_alibaba_z_image_base_lora_edit` |
| [Z-Image Base LoRA · Text to Image](https://popnow.ai/docs/models/z-image-base-lora) | `alibaba/z-image-base-lora/text-to-image` | 2.16 credits / image | `PopNow_alibaba_z_image_base_lora_text_to_image` |
| [Z-Image Turbo LoRA · Edit](https://popnow.ai/docs/models/z-image-turbo-lora) | `alibaba/z-image-turbo-lora/edit` | 1.8 credits / image | `PopNow_alibaba_z_image_turbo_lora_edit` |
| [Z-Image Turbo LoRA · Text to Image](https://popnow.ai/docs/models/z-image-turbo-lora) | `alibaba/z-image-turbo-lora/text-to-image` | 1.8 credits / image | `PopNow_alibaba_z_image_turbo_lora_text_to_image` |
| [Z-Image · Text to Image](https://popnow.ai/docs/models/z-image) | `alibaba/z-image-turbo/text-to-image` | 1.5 credits / image | `PopNow_alibaba_z_image_turbo_text_to_image` |
| [FLUX 3 Klein Base LoRA · Edit](https://popnow.ai/docs/models/flux-3-klein-base-lora) | `black-forest-labs/flux-3-klein-base-lora/edit` | 9 credits / image | `PopNow_black_forest_labs_flux_3_klein_base_lora_edit` |
| [FLUX 3 Klein Base LoRA · Text to Image](https://popnow.ai/docs/models/flux-3-klein-base-lora) | `black-forest-labs/flux-3-klein-base-lora/text-to-image` | 6.3 credits / image | `PopNow_black_forest_labs_flux_3_klein_base_lora_text_to_image` |
| [FLUX 3 Klein Base · Edit](https://popnow.ai/docs/models/flux-3-klein-base) | `black-forest-labs/flux-3-klein-base/edit` | 8.1 credits / image | `PopNow_black_forest_labs_flux_3_klein_base_edit` |
| [FLUX 3 Klein Base · Text to Image](https://popnow.ai/docs/models/flux-3-klein-base) | `black-forest-labs/flux-3-klein-base/text-to-image` | 5.4 credits / image | `PopNow_black_forest_labs_flux_3_klein_base_text_to_image` |
| [FLUX.1 Dev ControlNet LoRA · Text to Image](https://popnow.ai/docs/models/flux-1-dev-controlnet-lora) | `black-forest-labs/flux-1-dev-controlnet-lora/text-to-image` | 5.4 credits / image | `PopNow_black_forest_labs_flux_1_dev_controlnet_lora_text_to_image` |
| [FLUX.1 Dev LoRA · Edit](https://popnow.ai/docs/models/flux-1-dev-lora) | `black-forest-labs/flux-1-dev-lora/edit` | 2.7 credits / image | `PopNow_black_forest_labs_flux_1_dev_lora_edit` |
| [FLUX.1 Dev LoRA · Text to Image](https://popnow.ai/docs/models/flux-1-dev-lora) | `black-forest-labs/flux-1-dev-lora/text-to-image` | 2.7 credits / image | `PopNow_black_forest_labs_flux_1_dev_lora_text_to_image` |
| [FLUX.1 Fill Dev LoRA · Edit](https://popnow.ai/docs/models/flux-1-fill-dev-lora) | `black-forest-labs/flux-1-fill-dev-lora/edit` | 6.3 credits / image | `PopNow_black_forest_labs_flux_1_fill_dev_lora_edit` |
| [FLUX.1 Krea Dev LoRA · Edit](https://popnow.ai/docs/models/flux-1-krea-dev-lora) | `black-forest-labs/flux-1-krea-dev-lora/edit` | 3.6 credits / image | `PopNow_black_forest_labs_flux_1_krea_dev_lora_edit` |
| [FLUX.1 Krea Dev LoRA · Text to Image](https://popnow.ai/docs/models/flux-1-krea-dev-lora) | `black-forest-labs/flux-1-krea-dev-lora/text-to-image` | 3.6 credits / image | `PopNow_black_forest_labs_flux_1_krea_dev_lora_text_to_image` |
| [FLUX.1 Schnell LoRA · Edit](https://popnow.ai/docs/models/flux-1-schnell-lora) | `black-forest-labs/flux-1-schnell-lora/edit` | 0.9 credits / image | `PopNow_black_forest_labs_flux_1_schnell_lora_edit` |
| [FLUX.1 Schnell LoRA · Text to Image](https://popnow.ai/docs/models/flux-1-schnell-lora) | `black-forest-labs/flux-1-schnell-lora/text-to-image` | 0.9 credits / image | `PopNow_black_forest_labs_flux_1_schnell_lora_text_to_image` |
| [FLUX.2 Dev LoRA · Edit](https://popnow.ai/docs/models/flux-2-dev-lora) | `black-forest-labs/flux-2-dev-lora/edit` | 5.4 credits / image | `PopNow_black_forest_labs_flux_2_dev_lora_edit` |
| [FLUX.2 Dev LoRA · Text to Image](https://popnow.ai/docs/models/flux-2-dev-lora) | `black-forest-labs/flux-2-dev-lora/text-to-image` | 3.24 credits / image | `PopNow_black_forest_labs_flux_2_dev_lora_text_to_image` |
| [FLUX.2 Dev · Edit](https://popnow.ai/docs/models/flux-2-dev) | `black-forest-labs/flux-2-dev/edit` | 3.47 credits / image | `PopNow_black_forest_labs_flux_2_dev_edit` |
| [FLUX.2 Dev · Text to Image](https://popnow.ai/docs/models/flux-2-dev) | `black-forest-labs/flux-2-dev/text-to-image` | 1.74 credits / image | `PopNow_black_forest_labs_flux_2_dev_text_to_image` |
| [FLUX.2 Flex · Edit](https://popnow.ai/docs/models/flux-2-flex) | `black-forest-labs/flux-2-flex/edit` | 17.31 credits / image | `PopNow_black_forest_labs_flux_2_flex_edit` |
| [FLUX.2 Flex · Text to Image](https://popnow.ai/docs/models/flux-2-flex) | `black-forest-labs/flux-2-flex/text-to-image` | 8.67 credits / image | `PopNow_black_forest_labs_flux_2_flex_text_to_image` |
| [FLUX.2 Klein 4B LoRA · Edit](https://popnow.ai/docs/models/flux-2-klein-4b-lora) | `black-forest-labs/flux-2-klein-4b-lora/edit` | 3.06 credits / image | `PopNow_black_forest_labs_flux_2_klein_4b_lora_edit` |
| [FLUX.2 Klein 4B LoRA · Text to Image](https://popnow.ai/docs/models/flux-2-klein-4b-lora) | `black-forest-labs/flux-2-klein-4b-lora/text-to-image` | 2.34 credits / image | `PopNow_black_forest_labs_flux_2_klein_4b_lora_text_to_image` |
| [FLUX.2 Klein 4B · Edit](https://popnow.ai/docs/models/flux-2-klein-4b) | `black-forest-labs/flux-2-klein-4b/edit` | 1.89 credits / image | `PopNow_black_forest_labs_flux_2_klein_4b_edit` |
| [FLUX.2 Klein 4B · Text to Image](https://popnow.ai/docs/models/flux-2-klein-4b) | `black-forest-labs/flux-2-klein-4b/text-to-image` | 1.39 credits / image | `PopNow_black_forest_labs_flux_2_klein_4b_text_to_image` |
| [FLUX.2 Klein 9B LoRA · Edit](https://popnow.ai/docs/models/flux-2-klein-9b-lora) | `black-forest-labs/flux-2-klein-9b-lora/edit` | 3.78 credits / image | `PopNow_black_forest_labs_flux_2_klein_9b_lora_edit` |
| [FLUX.2 Klein 9B LoRA · Text to Image](https://popnow.ai/docs/models/flux-2-klein-9b-lora) | `black-forest-labs/flux-2-klein-9b-lora/text-to-image` | 2.7 credits / image | `PopNow_black_forest_labs_flux_2_klein_9b_lora_text_to_image` |
| [FLUX.2 Klein 9B · Edit](https://popnow.ai/docs/models/flux-2-klein-9b) | `black-forest-labs/flux-2-klein-9b/edit` | 2.44 credits / image | `PopNow_black_forest_labs_flux_2_klein_9b_edit` |
| [FLUX.2 Klein 9B · Text to Image](https://popnow.ai/docs/models/flux-2-klein-9b) | `black-forest-labs/flux-2-klein-9b/text-to-image` | 1.65 credits / image | `PopNow_black_forest_labs_flux_2_klein_9b_text_to_image` |
| [FLUX.2 Klein Base 4B LoRA · Edit](https://popnow.ai/docs/models/flux-2-klein-base-4b-lora) | `black-forest-labs/flux-2-klein-base-4b-lora/edit` | 3.6 credits / image | `PopNow_black_forest_labs_flux_2_klein_base_4b_lora_edit` |
| [FLUX.2 Klein Base 4B LoRA · Text to Image](https://popnow.ai/docs/models/flux-2-klein-base-4b-lora) | `black-forest-labs/flux-2-klein-base-4b-lora/text-to-image` | 2.7 credits / image | `PopNow_black_forest_labs_flux_2_klein_base_4b_lora_text_to_image` |
| [FLUX.2 Klein Base 9B LoRA · Edit](https://popnow.ai/docs/models/flux-2-klein-base-9b-lora) | `black-forest-labs/flux-2-klein-base-9b-lora/edit` | 4.68 credits / image | `PopNow_black_forest_labs_flux_2_klein_base_9b_lora_edit` |
| [FLUX.2 Klein Base 9B LoRA · Text to Image](https://popnow.ai/docs/models/flux-2-klein-base-9b-lora) | `black-forest-labs/flux-2-klein-base-9b-lora/text-to-image` | 3.6 credits / image | `PopNow_black_forest_labs_flux_2_klein_base_9b_lora_text_to_image` |
| [FLUX.2 Max · Edit](https://popnow.ai/docs/models/flux-2-max) | `black-forest-labs/flux-2-max/edit` | 11.42 credits / image | `PopNow_black_forest_labs_flux_2_max_edit` |
| [FLUX.2 Max · Text to Image](https://popnow.ai/docs/models/flux-2-max) | `black-forest-labs/flux-2-max/text-to-image` | 10.5 credits / image | `PopNow_black_forest_labs_flux_2_max_text_to_image` |
| [FLUX.2 Pro · Edit](https://popnow.ai/docs/models/flux-2-pro) | `black-forest-labs/flux-2-pro/edit` | 8.67 credits / image | `PopNow_black_forest_labs_flux_2_pro_edit` |
| [FLUX.2 Pro · Text to Image](https://popnow.ai/docs/models/flux-2-pro) | `black-forest-labs/flux-2-pro/text-to-image` | 4.5 credits / image | `PopNow_black_forest_labs_flux_2_pro_text_to_image` |
| [Seedream 4.0 · Edit](https://popnow.ai/docs/models/seedream-4-0) | `bytedance/seedream-4.0/edit` | 4.5 credits / image | `PopNow_bytedance_seedream_4_0_edit` |
| [Seedream 4.0 · Text to Image](https://popnow.ai/docs/models/seedream-4-0) | `bytedance/seedream-4.0/text-to-image` | 4.5 credits / image | `PopNow_bytedance_seedream_4_0_text_to_image` |
| [Seedream 5.0 Flash · Edit](https://popnow.ai/docs/models/seedream-5-0-flash) | `bytedance/seedream-5.0-flash/edit` | 4.35 credits / image | `PopNow_bytedance_seedream_5_0_flash_edit` |
| [Seedream 5.0 Flash · Layer Decomposition](https://popnow.ai/docs/models/seedream-5-0-flash) | `bytedance/seedream-5.0-flash/layer-decomposition` | 3.9 credits / image | `PopNow_bytedance_seedream_5_0_flash_layer_decomposition` |
| [Seedream 5.0 Flash · Text to Image](https://popnow.ai/docs/models/seedream-5-0-flash) | `bytedance/seedream-5.0-flash/text-to-image` | 4.35 credits / image | `PopNow_bytedance_seedream_5_0_flash_text_to_image` |
| [Seedream 5.0 Lite · Edit](https://popnow.ai/docs/models/seedream-5-0-lite) | `bytedance/seedream-5.0-lite/edit` | 5.18 credits / image | `PopNow_bytedance_seedream_5_0_lite_edit` |
| [Seedream 5.0 Lite · Text to Image](https://popnow.ai/docs/models/seedream-5-0-lite) | `bytedance/seedream-5.0-lite/text-to-image` | 5.18 credits / image | `PopNow_bytedance_seedream_5_0_lite_text_to_image` |
| [Seedream 5.0 Pro · Edit](https://popnow.ai/docs/models/seedream-5-0-pro) | `bytedance/seedream-5.0-pro/edit` | 5.4 credits / image | `PopNow_bytedance_seedream_5_0_pro_edit` |
| [Seedream 5.0 Pro · Layer Decomposition](https://popnow.ai/docs/models/seedream-5-0-pro) | `bytedance/seedream-5.0-pro/layer-decomposition` | 6.3 credits / image | `PopNow_bytedance_seedream_5_0_pro_layer_decomposition` |
| [Seedream 5.0 Pro · Text to Image](https://popnow.ai/docs/models/seedream-5-0-pro) | `bytedance/seedream-5.0-pro/text-to-image` | 5.4 credits / image | `PopNow_bytedance_seedream_5_0_pro_text_to_image` |
| [Anima Turbo LoRA · Edit](https://popnow.ai/docs/models/anima-turbo-lora) | `circlestone-labs/anima-turbo-lora/edit` | 2.7 credits / image | `PopNow_circlestone_labs_anima_turbo_lora_edit` |
| [Anima Turbo LoRA · Text to Image](https://popnow.ai/docs/models/anima-turbo-lora) | `circlestone-labs/anima-turbo-lora/text-to-image` | 2.7 credits / image | `PopNow_circlestone_labs_anima_turbo_lora_text_to_image` |
| [Anima Turbo · Edit](https://popnow.ai/docs/models/anima-turbo) | `circlestone-labs/anima-turbo/edit` | 1.8 credits / image | `PopNow_circlestone_labs_anima_turbo_edit` |
| [Anima Turbo · Text to Image](https://popnow.ai/docs/models/anima-turbo) | `circlestone-labs/anima-turbo/text-to-image` | 1.8 credits / image | `PopNow_circlestone_labs_anima_turbo_text_to_image` |
| [Nano Banana 2 · Edit](https://popnow.ai/docs/models/nano-banana-2) | `google/nano-banana-2/edit` | 5.4 credits / image | `PopNow_google_nano_banana_2_edit` |
| [Nano Banana 2 · Text to Image](https://popnow.ai/docs/models/nano-banana-2) | `google/nano-banana-2/text-to-image` | 5.4 credits / image | `PopNow_google_nano_banana_2_text_to_image` |
| [Nano Banana 2.1 · Edit](https://popnow.ai/docs/models/nano-banana-2-1) | `google/nano-banana-2.1/edit` | 7.2 credits / image | `PopNow_google_nano_banana_2_1_edit` |
| [Nano Banana 2.1 · Text to Image](https://popnow.ai/docs/models/nano-banana-2-1) | `google/nano-banana-2.1/text-to-image` | 7.2 credits / image | `PopNow_google_nano_banana_2_1_text_to_image` |
| [Nano Banana Pro · Edit](https://popnow.ai/docs/models/nano-banana-pro) | `google/nano-banana-pro/edit` | 16.08 credits / image | `PopNow_google_nano_banana_pro_edit` |
| [Nano Banana Pro · Text to Image](https://popnow.ai/docs/models/nano-banana-pro) | `google/nano-banana-pro/text-to-image` | 16.08 credits / image | `PopNow_google_nano_banana_pro_text_to_image` |
| [Jib Mix Qwen LoRA · Text to Image](https://popnow.ai/docs/models/jib-mix-qwen-image-lora) | `j1b/jib-mix-qwen-image-lora/text-to-image` | 4.5 credits / image | `PopNow_j1b_jib_mix_qwen_image_lora_text_to_image` |
| [Jib Mix Qwen · Text to Image](https://popnow.ai/docs/models/jib-mix-qwen-image) | `j1b/jib-mix-qwen-image/text-to-image` | 3.6 credits / image | `PopNow_j1b_jib_mix_qwen_image_text_to_image` |
| [Krea 2 Large · Text to Image](https://popnow.ai/docs/models/krea-2-large) | `krea/2-large/text-to-image` | 9 credits / image | `PopNow_krea_2_large_text_to_image` |
| [Krea 2 Medium Turbo · Text to Image](https://popnow.ai/docs/models/krea-2-medium-turbo) | `krea/2-medium-turbo/text-to-image` | 2.25 credits / image | `PopNow_krea_2_medium_turbo_text_to_image` |
| [Krea 2 Medium · Text to Image](https://popnow.ai/docs/models/krea-2-medium) | `krea/2-medium/text-to-image` | 4.5 credits / image | `PopNow_krea_2_medium_text_to_image` |
| [Krea 2 Turbo LoRA · Edit](https://popnow.ai/docs/models/krea-2-turbo-lora) | `krea/2-turbo-lora/edit` | 3.24 credits / image | `PopNow_krea_2_turbo_lora_edit` |
| [Krea 2 Turbo LoRA · Text to Image](https://popnow.ai/docs/models/krea-2-turbo-lora) | `krea/2-turbo-lora/text-to-image` | 3.24 credits / image | `PopNow_krea_2_turbo_lora_text_to_image` |
| [Krea 3 · Edit](https://popnow.ai/docs/models/krea-3) | `krea/3/edit` | 10.8 credits / image | `PopNow_krea_3_edit` |
| [Krea 3 · Text to Image](https://popnow.ai/docs/models/krea-3) | `krea/3/text-to-image` | 5.4 credits / image | `PopNow_krea_3_text_to_image` |
| [MiniMax H3 Image LoRA · Edit](https://popnow.ai/docs/models/minimax-h3-image-lora) | `minimax/h3-image-lora/edit` | 8.1 credits / image | `PopNow_minimax_h3_image_lora_edit` |
| [MiniMax H3 Image LoRA · Text to Image](https://popnow.ai/docs/models/minimax-h3-image-lora) | `minimax/h3-image-lora/text-to-image` | 6.3 credits / image | `PopNow_minimax_h3_image_lora_text_to_image` |
| [Neta Lumina · Text to Image](https://popnow.ai/docs/models/neta-lumina) | `neta-art/neta-lumina/text-to-image` | 1.8 credits / image | `PopNow_neta_art_neta_lumina_text_to_image` |
| [GPT Image 2 · Edit](https://popnow.ai/docs/models/gpt-image-2) | `openai/gpt-image-2/edit` | 0.27 credits / image | `PopNow_openai_gpt_image_2_edit` |
| [GPT Image 2 · Text to Image](https://popnow.ai/docs/models/gpt-image-2) | `openai/gpt-image-2/text-to-image` | 0.27 credits / image | `PopNow_openai_gpt_image_2_text_to_image` |
| [GPT Image 2.5 Flare · Edit](https://popnow.ai/docs/models/gpt-image-2-5-flare) | `openai/gpt-image-2.5-flare/edit` | 0.27 credits / image | `PopNow_openai_gpt_image_2_5_flare_edit` |
| [GPT Image 2.5 Flare · Text to Image](https://popnow.ai/docs/models/gpt-image-2-5-flare) | `openai/gpt-image-2.5-flare/text-to-image` | 0.27 credits / image | `PopNow_openai_gpt_image_2_5_flare_text_to_image` |
| [GPT Image 2.5 Sunburst · Edit](https://popnow.ai/docs/models/gpt-image-2-5-sunburst) | `openai/gpt-image-2.5-sunburst/edit` | 0.27 credits / image | `PopNow_openai_gpt_image_2_5_sunburst_edit` |
| [GPT Image 2.5 Sunburst · Text to Image](https://popnow.ai/docs/models/gpt-image-2-5-sunburst) | `openai/gpt-image-2.5-sunburst/text-to-image` | 0.27 credits / image | `PopNow_openai_gpt_image_2_5_sunburst_text_to_image` |
| [Anime to Real · Edit](https://popnow.ai/docs/models/anime-to-real-v1) | `popnow/anime-to-real-v1/edit` | 4.5 credits / image | `PopNow_popnow_anime_to_real_v1_edit` |
| [Background Remover · Edit](https://popnow.ai/docs/models/background-remover-v1) | `popnow/background-remover-v1/edit` | 0.72 credits / image | `PopNow_popnow_background_remover_v1_edit` |
| [Camera Angle Changer · Edit](https://popnow.ai/docs/models/camera-angle-changer-v1) | `popnow/camera-angle-changer-v1/edit` | 4.5 credits / image | `PopNow_popnow_camera_angle_changer_v1_edit` |
| [Image Expander · Edit](https://popnow.ai/docs/models/image-expander-v1) | `popnow/image-expander-v1/edit` | 3.6 credits / image | `PopNow_popnow_image_expander_v1_edit` |
| [Image Upscaler · Upscale](https://popnow.ai/docs/models/image-upscaler-v1) | `popnow/image-upscaler-v1/upscale` | 1.8 credits / image | `PopNow_popnow_image_upscaler_v1_upscale` |
| [Object Eraser · Edit](https://popnow.ai/docs/models/object-eraser-v1) | `popnow/object-eraser-v1/edit` | 4.5 credits / image | `PopNow_popnow_object_eraser_v1_edit` |
| [Pose Changer · Edit](https://popnow.ai/docs/models/pose-changer-v1) | `popnow/pose-changer-v1/edit` | 4.5 credits / image | `PopNow_popnow_pose_changer_v1_edit` |
| [Relight · Edit](https://popnow.ai/docs/models/relight-v1) | `popnow/relight-v1/edit` | 4.5 credits / image | `PopNow_popnow_relight_v1_edit` |
| [Shadow Remover · Edit](https://popnow.ai/docs/models/shadow-remover-v1) | `popnow/shadow-remover-v1/edit` | 4.5 credits / image | `PopNow_popnow_shadow_remover_v1_edit` |
| [Prefect Pony XL LoRA · Text to Image](https://popnow.ai/docs/models/prefect-pony-xl-lora) | `prefect/pony-xl-lora/text-to-image` | 3.6 credits / image | `PopNow_prefect_pony_xl_lora_text_to_image` |
| [Prefect Pony XL · Text to Image](https://popnow.ai/docs/models/prefect-pony-xl) | `prefect/pony-xl/text-to-image` | 2.25 credits / image | `PopNow_prefect_pony_xl_text_to_image` |
| [P-Image LoRA · Edit](https://popnow.ai/docs/models/p-image-lora) | `pruna-ai/p-image-lora/edit` | 1.8 credits / image | `PopNow_pruna_ai_p_image_lora_edit` |
| [P-Image LoRA · Text to Image](https://popnow.ai/docs/models/p-image-lora) | `pruna-ai/p-image-lora/text-to-image` | 0.9 credits / image | `PopNow_pruna_ai_p_image_lora_text_to_image` |

## Audio

| Node | Call name | From | Node type |
| --- | --- | --- | --- |
| [Qwen3 TTS · Text to Speech](https://popnow.ai/docs/models/qwen-3-tts) | `alibaba/qwen-3-tts/text-to-speech` | 10.2 credits / 1k characters | `PopNow_alibaba_qwen_3_tts_text_to_speech` |
| [Seed Audio 1.0 · Text to Audio](https://popnow.ai/docs/models/seed-audio-1-0) | `bytedance/seed-audio-1.0/text-to-audio` | 54 credits / run | `PopNow_bytedance_seed_audio_1_0_text_to_audio` |
| [Seed Speech 2.0 · Text to Speech](https://popnow.ai/docs/models/seed-speech-2-0) | `bytedance/seed-speech-2.0/text-to-speech` | 10.8 credits / 1k characters | `PopNow_bytedance_seed_speech_2_0_text_to_speech` |
| [Gemini 2.5 Pro TTS · Text to Speech](https://popnow.ai/docs/models/gemini-2-5-pro-tts) | `google/gemini-2.5-pro-tts/text-to-speech` | 0.07 credits / second | `PopNow_google_gemini_2_5_pro_tts_text_to_speech` |
| [Gemini 3.8 Flash TTS · Text to Speech](https://popnow.ai/docs/models/gemini-3-8-flash-tts) | `google/gemini-3.8-flash-tts/text-to-speech` | 0.05 credits / second | `PopNow_google_gemini_3_8_flash_tts_text_to_speech` |
| [Gemini 3.8 Flash-Lite TTS · Text to Speech](https://popnow.ai/docs/models/gemini-3-8-flash-lite-tts) | `google/gemini-3.8-flash-lite-tts/text-to-speech` | 0.03 credits / second | `PopNow_google_gemini_3_8_flash_lite_tts_text_to_speech` |
| [HeartMuLa Transcribe · Speech to Text](https://popnow.ai/docs/models/heartmula-transcribe) | `heartmula/transcribe/speech-to-text` | 7.5 credits / run | `PopNow_heartmula_transcribe_speech_to_text` |
| [MiniMax Music 3.0 · Text to Audio](https://popnow.ai/docs/models/minimax-music-3-0) | `minimax/music-3.0/text-to-audio` | 27 credits / run | `PopNow_minimax_music_3_0_text_to_audio` |
| [MiniMax Speech 2.8 HD · Text to Speech](https://popnow.ai/docs/models/minimax-speech-2-8-hd) | `minimax/speech-2.8-hd/text-to-speech` | 18 credits / 1k characters | `PopNow_minimax_speech_2_8_hd_text_to_speech` |
| [MiniMax Speech 2.8 Turbo · Text to Speech](https://popnow.ai/docs/models/minimax-speech-2-8-turbo) | `minimax/speech-2.8-turbo/text-to-speech` | 10.8 credits / 1k characters | `PopNow_minimax_speech_2_8_turbo_text_to_speech` |
| [Video Sound Effects · Video to Audio](https://popnow.ai/docs/models/foley-v1) | `popnow/foley-v1/video-to-audio` | 0.18 credits / second | `PopNow_popnow_foley_v1_video_to_audio` |
| [Chatterbox · Text to Speech](https://popnow.ai/docs/models/chatterbox-v1) | `resemble-ai/chatterbox-v1/text-to-speech` | 5.4 credits / run | `PopNow_resemble_ai_chatterbox_v1_text_to_speech` |
| [Suno v6 Mini · Text to Audio](https://popnow.ai/docs/models/suno-v6-mini) | `suno/v6-mini/text-to-audio` | 10.8 credits / run | `PopNow_suno_v6_mini_text_to_audio` |
| [Suno v6 Wild · Text to Audio](https://popnow.ai/docs/models/suno-v6-wild) | `suno/v6-wild/text-to-audio` | 10.8 credits / run | `PopNow_suno_v6_wild_text_to_audio` |
| [Suno v6 · Text to Audio](https://popnow.ai/docs/models/suno-v6) | `suno/v6/text-to-audio` | 10.8 credits / run | `PopNow_suno_v6_text_to_audio` |
| [Grok STT · Speech to Text](https://popnow.ai/docs/models/grok-stt) | `xai/grok-stt/speech-to-text` | 0.01 credits / second | `PopNow_xai_grok_stt_speech_to_text` |
| [Grok TTS · Text to Speech](https://popnow.ai/docs/models/grok-tts) | `xai/grok-tts/text-to-speech` | 2.7 credits / 1k characters | `PopNow_xai_grok_tts_text_to_speech` |
