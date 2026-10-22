"""Node classes built from the snapshot, with ComfyUI replaced by tests/comfy_stub.py."""

import json
import os
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

from . import comfy_stub

try:
    import aiohttp  # noqa: F401
except ImportError:  # pragma: no cover - only when run outside a ComfyUI environment
    aiohttp = None

if aiohttp is not None:
    comfy_stub.install()
    from popnow_nodes import config, nodes
    from popnow_nodes.fields import build_fields, plan_outputs

    from .fake_api import FakePopNow

ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT = ROOT / "data" / "catalog-snapshot.json"


def snapshot_items():
    return json.loads(SNAPSHOT.read_text(encoding="utf-8"))["items"]


@unittest.skipIf(aiohttp is None, "aiohttp is not installed")
class BuildTest(unittest.TestCase):
    def test_one_node_per_model_plus_two(self):
        items = snapshot_items()
        built, badges = nodes.build_all(items)
        self.assertEqual(len(built), len(items) + 2)
        ids = [node.GET_SCHEMA().node_id for node in built]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertIn("PopNowGenerate", ids)
        self.assertIn("PopNow_LoRA", ids)
        # Every model node carries a price badge, and every badge belongs to a node.
        self.assertEqual(set(badges), {i for i in ids if i.startswith("PopNow_") and i != "PopNow_LoRA"})
        for node in built:
            schema = node.GET_SCHEMA()
            self.assertTrue(schema.category.startswith("PopNow"), schema.node_id)

    def test_text_and_chat_models_are_not_nodes(self):
        built, _ = nodes.build_all(
            [
                {"model": "x/chat/chat", "modality": "text", "tasks": ["chat"], "inputSchema": {"properties": {}}},
                {"model": "x/off/text-to-image", "modality": "image", "enabled": False, "inputSchema": {"properties": {}}},
            ]
        )
        self.assertEqual([n.GET_SCHEMA().node_id for n in built], ["PopNowGenerate", "PopNow_LoRA"])

    def test_model_node_shape(self):
        model = next(i for i in snapshot_items() if i["model"] == "minimax/h3/image-to-video")
        schema = nodes.make_model_node(model).GET_SCHEMA()
        self.assertEqual(schema.node_id, "PopNow_minimax_h3_image_to_video")
        self.assertEqual(schema.category, "PopNow/Video/MiniMax")
        self.assertIn("minimax/h3/image-to-video", schema.description)
        self.assertIn("credits", schema.description)
        self.assertEqual([o.name for o in schema.outputs], ["video", "task_id"])
        image = next(i for i in schema.inputs if i.name == "image_url")
        self.assertEqual(image.socket, "IMAGE")


@unittest.skipIf(aiohttp is None, "aiohttp is not installed")
class GenerateCompatibilityTest(unittest.TestCase):
    """PopNow Generate must stay a drop-in for the single-file node published on popnow.ai."""

    def test_same_node_type_inputs_and_outputs(self):
        schema = nodes.PopNowGenerate.GET_SCHEMA()
        self.assertEqual(schema.node_id, "PopNowGenerate")
        self.assertEqual(schema.display_name, "PopNow Generate")
        self.assertEqual(schema.category, "PopNow")
        self.assertEqual([i.name for i in schema.inputs], ["model", "prompt", "options", "image", "image_field"])
        self.assertEqual([i.socket for i in schema.inputs], ["STRING", "STRING", "STRING", "IMAGE", "STRING"])
        self.assertEqual([i.optional for i in schema.inputs], [False, False, False, True, True])
        defaults = {i.name: i.options.get("default") for i in schema.inputs}
        self.assertEqual(defaults["model"], "google/nano-banana-2.1/text-to-image")
        self.assertEqual(json.loads(defaults["options"]), {"aspect_ratio": "16:9", "resolution": "1k"})
        self.assertEqual(defaults["image_field"], "image_url")
        self.assertEqual(
            [(o.socket, o.name) for o in schema.outputs], [("IMAGE", "image"), ("STRING", "url"), ("STRING", "path")]
        )

    def test_input_rules_match_the_single_file_node(self):
        build = nodes.build_generate_input
        self.assertEqual(build("a/b/c", "hi", '{"resolution": "2k"}', [], "image_url"), {"resolution": "2k", "prompt": "hi"})
        self.assertEqual(build("a/b/c", "hi", '{"prompt": "kept"}', [], "image_url"), {"prompt": "kept"})
        self.assertEqual(build("a/b/c", "  ", "", [], "image_url"), {})
        self.assertEqual(build("a/b/c", "", "{}", ["popnow://f/1"], "image_url"), {"image_url": "popnow://f/1"})
        self.assertEqual(
            build("a/b/c", "", "{}", ["popnow://f/1", "popnow://f/2"], "image_urls"),
            {"image_urls": ["popnow://f/1", "popnow://f/2"]},
        )
        with self.assertRaises(ValueError):
            build("a/b/c", "", "{bad", [], "image_url")
        with self.assertRaises(ValueError):
            build("a/b/c", "", "[1]", [], "image_url")

    def test_speech_models_get_the_prompt_as_text(self):
        nodes.build_all(snapshot_items())
        self.assertEqual(
            nodes.build_generate_input("xai/grok-tts/text-to-speech", "Hello", "{}", [], "image_url"), {"text": "Hello"}
        )


@unittest.skipIf(aiohttp is None, "aiohttp is not installed")
class LoraTest(unittest.IsolatedAsyncioTestCase):
    def test_source_kinds(self):
        kind = nodes.lora_source_kind
        self.assertEqual(kind("popnow://f/fil_1"), "uri")
        self.assertEqual(kind("https://example.com/w.safetensors"), "direct")
        self.assertEqual(kind("https://huggingface.co/owner/repo"), "import")
        self.assertEqual(kind("https://civitai.com/models/123"), "import")
        self.assertEqual(kind("owner/repo"), "import")
        self.assertEqual(kind("styles/pixel.safetensors"), "local")
        self.assertEqual(kind("pixel.safetensors"), "local")

    async def test_direct_links_need_no_key_and_chain(self):
        with mock.patch.dict(os.environ, {"POPNOW_API_KEY": ""}):
            first = await nodes.PopNowLoRA.execute("https://example.com/a.safetensors", 0.8)
            second = await nodes.PopNowLoRA.execute("https://example.com/b.safetensors", 1.0, loras=first[0])
        self.assertEqual(
            second[0],
            [
                {"path": "https://example.com/a.safetensors", "scale": 0.8},
                {"path": "https://example.com/b.safetensors", "scale": 1.0},
            ],
        )

    async def test_hugging_face_repo_is_imported_once(self):
        fake = FakePopNow()
        base = await fake.start()
        self.addAsyncCleanup(fake.close)
        home = tempfile.TemporaryDirectory()
        self.addCleanup(home.cleanup)
        env = {"POPNOW_API_KEY": "sk-popnow-lora", "POPNOW_BASE_URL": base, "POPNOW_COMFYUI_HOME": home.name, "HF_TOKEN": "hf_x"}
        with mock.patch.dict(os.environ, env):
            out = await nodes.PopNowLoRA.execute("owner/repo", 1.0)
            await nodes.PopNowLoRA.execute("owner/repo", 1.0)
        self.assertEqual(out[0], [{"path": "popnow://f/fil_lora", "scale": 1.0}])
        self.assertEqual(fake.calls["import"], 1)
        self.assertEqual(fake.bodies["import"][0], {"url": "owner/repo", "token": "hf_x"})


@unittest.skipIf(aiohttp is None, "aiohttp is not installed")
class RunTest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.fake = FakePopNow()
        base = await self.fake.start()
        self.home = tempfile.TemporaryDirectory()
        env = {"POPNOW_API_KEY": "sk-popnow-run", "POPNOW_BASE_URL": base, "POPNOW_COMFYUI_HOME": self.home.name}
        self.env = mock.patch.dict(os.environ, env)
        self.env.start()
        nodes._upload_cache.clear()

    async def asyncTearDown(self):
        self.env.stop()
        self.home.cleanup()
        await self.fake.close()

    def transcriber(self):
        return {
            "model": "test/stt/speech-to-text",
            "modality": "audio",
            "tasks": ["speech-to-text"],
            "inputSchema": {
                "required": ["audio_url"],
                "properties": {
                    "audio_url": {"type": "string", "x-ui": {"widget": "text", "order": 100}},
                    "language": {"type": "string", "enum": ["en", "de"], "x-ui": {"order": 50}},
                    "seed": {"type": "integer", "minimum": 0},
                },
            },
        }

    async def run_transcriber(self, **values):
        model = self.transcriber()
        specs = build_fields(model["inputSchema"])
        return await nodes.run_model(model, specs, plan_outputs(model), "7", values)

    async def test_quote_create_poll_collect(self):
        self.fake.behaviour["output"] = {"text": "hello world", "assets": []}
        result = await self.run_transcriber(audio_url="https://example.com/a.mp3", language="model default", seed=3)
        self.assertEqual(result, ["hello world", "job_1"])
        sent = self.fake.bodies["create"][0]
        self.assertEqual(sent["model"], "test/stt/speech-to-text")
        self.assertEqual(sent["input"], {"audio_url": "https://example.com/a.mp3", "seed": 3})
        self.assertEqual(sent["quoteId"], "q_1")
        self.assertEqual(sent["expectedCredits"], 48)
        self.assertEqual(self.fake.bodies["quote"][0]["input"], sent["input"])

    async def test_price_change_requotes_under_the_same_key(self):
        self.fake.behaviour["output"] = {"text": "ok", "assets": []}
        self.fake.behaviour["create_40901_first"] = True
        await self.run_transcriber(audio_url="https://example.com/a.mp3", language="en", seed=0)
        self.assertEqual(self.fake.calls["quote"], 2)
        keys = [h.get("Idempotency-Key") for h in self.fake.headers["create"]]
        self.assertEqual(len(keys), 2)
        self.assertEqual(keys[0], keys[1])
        self.assertEqual(self.fake.bodies["create"][1]["quoteId"], "q_2")

    async def test_credit_limit_stops_before_anything_is_held(self):
        config.save_max_credits_per_run(5)
        with self.assertRaises(ValueError) as caught:
            await self.run_transcriber(audio_url="https://example.com/a.mp3", language="en", seed=0)
        self.assertIn("5 credits", str(caught.exception))
        self.assertNotIn("create", self.fake.calls)

    async def test_failed_task_raises(self):
        self.fake.behaviour["state"] = "failed"
        self.fake.behaviour["output"] = {"assets": []}
        with self.assertRaises(nodes.PopNowTaskFailed):
            await self.run_transcriber(audio_url="https://example.com/a.mp3", language="en", seed=0)

    async def test_no_key_is_a_clear_error(self):
        with mock.patch.dict(os.environ, {"POPNOW_API_KEY": ""}), self.assertRaises(ValueError) as caught:
            await self.run_transcriber(audio_url="x", language="en", seed=0)
        self.assertIn("POPNOW_API_KEY", str(caught.exception))

    async def test_generate_saves_audio_to_the_output_folder(self):
        self.fake.behaviour["output"] = {"assets": [{"mime": "audio/mpeg", "url": f"{self.fake.base}/files/result.bin"}]}
        fake_media = types.SimpleNamespace(empty_image=lambda: "BLANK")
        with mock.patch.object(nodes, "_media", lambda: fake_media):
            image, url, path = await nodes.PopNowGenerate.execute("xai/grok-tts/text-to-speech", "Hello", "{}")
        self.assertEqual(image, "BLANK")
        self.assertTrue(url.endswith("/files/result.bin"))
        self.assertTrue(path.endswith("popnow_job_1.mp3"))
        with open(path, "rb") as handle:
            self.assertEqual(handle.read(), b"RESULT-BYTES")
        os.unlink(path)


if __name__ == "__main__":
    unittest.main()
