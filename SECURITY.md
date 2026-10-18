# Security policy

## Reporting a vulnerability

Please do **not** open a public issue for security problems.

- Open a [private security advisory](https://github.com/popnow-ai/popnow-comfyui/security/advisories/new) on
  GitHub, or
- email **support@popnow.ai** with "Security" in the subject.

Include the affected version, a description, and steps to reproduce. Never include a live API key; if you
think a key was exposed, revoke it in the [API console](https://popnow.ai/api/console/keys) first.

## Supported versions

Security fixes are released for the latest version of `popnow-comfyui`.

## How the nodes handle secrets

- The API key is read from `POPNOW_API_KEY` or from `user/popnow/config.json` (written with owner-only
  permissions). It is never a widget value, so it never ends up in workflow files or image metadata, and
  the settings routes only ever return its last four characters.
- Hugging Face and Civitai tokens for LoRA imports are read from the environment for one request and never
  stored.
- File names typed into nodes are resolved inside ComfyUI's input or loras folder only, so a shared
  workflow cannot upload files from elsewhere on your machine.
- Output URLs are short-lived signed links; the key is never attached when downloading them.
