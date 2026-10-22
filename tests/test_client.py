"""The HTTP client against a local fake of the API. Needs aiohttp, which ComfyUI ships."""

import os
import tempfile
import unittest

try:
    import aiohttp  # noqa: F401
except ImportError:  # pragma: no cover - only when run outside a ComfyUI environment
    aiohttp = None

if aiohttp is not None:
    from popnow_nodes.client import USER_AGENT, PopNowApiError, PopNowClient, PopNowTaskFailed

    from .fake_api import FakePopNow


@unittest.skipIf(aiohttp is None, "aiohttp is not installed")
class ClientTest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.fake = FakePopNow()
        base = await self.fake.start()
        self.client = PopNowClient("sk-popnow-test", base)

    async def asyncTearDown(self):
        await self.client.close()
        await self.fake.close()

    async def test_sends_key_and_an_explicit_user_agent(self):
        await self.client.list_models()
        headers = self.fake.headers["models"][0]
        self.assertEqual(headers["Authorization"], "Bearer sk-popnow-test")
        self.assertEqual(headers["User-Agent"], USER_AGENT)
        self.assertTrue(USER_AGENT.startswith("popnow-comfyui/"))

    async def test_retries_a_503_then_succeeds(self):
        self.fake.behaviour["models_503_first"] = True
        items = await self.client.list_models()
        self.assertEqual(items[0]["model"], "a/b/c")
        self.assertEqual(self.fake.calls["models"], 2)

    async def test_resend_keeps_the_idempotency_key(self):
        self.fake.behaviour["create_503_first"] = True
        task = await self.client.create_task(
            "m/x/y", {"prompt": "p"}, idempotency_key="key-1", quote_id="q_1", expected_credits=48
        )
        self.assertEqual(task["taskId"], "job_1")
        keys = [h.get("Idempotency-Key") for h in self.fake.headers["create"]]
        self.assertEqual(keys, ["key-1", "key-1"])
        self.assertEqual(self.fake.bodies["create"][0]["expectedCredits"], 48)
        self.assertEqual(self.fake.bodies["create"][0]["quoteId"], "q_1")

    async def test_refunded_failure_is_not_replayed(self):
        with self.assertRaises(PopNowApiError) as caught:
            await self.client.create_task("always/refunded/x", {}, idempotency_key="key-2")
        self.assertEqual(caught.exception.code, 50302)
        self.assertEqual(self.fake.calls["create"], 1)
        self.assertIn("refunded", caught.exception.recovery)
        self.assertIn("req_test", str(caught.exception))

    async def test_upload_sends_ticket_headers_and_no_key(self):
        uri = await self.client.upload(b"\x89PNG-bytes", "image/png")
        self.assertEqual(uri, "popnow://f/fil_1")
        self.assertEqual(self.fake.calls["put"], 1)
        self.assertEqual(self.fake.bodies["put"][0], b"\x89PNG-bytes")
        self.assertEqual(self.fake.bodies["ticket"][0], {"contentType": "image/png", "bytes": 10})

    async def test_upload_refuses_oversized_bytes(self):
        with self.assertRaises(PopNowApiError):
            await self.client.upload(b"x" * 2048, "image/png")
        self.assertNotIn("put", self.fake.calls)

    async def test_upload_file_streams_from_disk(self):
        self.fake.behaviour["max_bytes"] = 1 << 20
        with tempfile.NamedTemporaryFile(suffix=".safetensors", delete=False) as handle:
            handle.write(b"S" * 4096)
        self.addCleanup(os.unlink, handle.name)
        uri = await self.client.upload_file(handle.name, "application/octet-stream")
        self.assertEqual(uri, "popnow://f/fil_1")
        self.assertEqual(self.fake.bodies["put"][0], b"S" * 4096)

    async def test_import_lora(self):
        uri = await self.client.import_lora("owner/repo", "hf_token")
        self.assertEqual(uri, "popnow://f/fil_lora")
        self.assertEqual(self.fake.bodies["import"][0], {"url": "owner/repo", "token": "hf_token"})
        await self.client.import_lora("https://example.com/x.safetensors")
        self.assertEqual(self.fake.bodies["import"][1], {"url": "https://example.com/x.safetensors"})

    async def test_wait_skips_pending_assets(self):
        task = await self.client.wait_for_task("job_1", timeout_seconds=30)
        self.assertEqual(task["output"]["assets"][0]["url"], "https://x/y.png")
        self.assertEqual(self.fake.calls["record"], 2)

    async def test_balance(self):
        balance = await self.client.balance()
        self.assertEqual(balance["availableCredits"], 1000)

    async def test_failed_task_message(self):
        error = PopNowTaskFailed({"taskId": "job_9", "state": "failed", "errorCode": "generation_failed", "errorMessage": "boom"})
        self.assertIn("generation_failed", str(error))
        self.assertIn("job_9", str(error))


if __name__ == "__main__":
    unittest.main()
