import json
import os
import stat
import tempfile
import unittest
from decimal import Decimal
from unittest import mock

from popnow_nodes import config


class ConfigTest(unittest.TestCase):
    def setUp(self):
        self.home = tempfile.TemporaryDirectory()
        patcher = mock.patch.dict(os.environ, {config.ENV_CONFIG_DIR: self.home.name}, clear=False)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.addCleanup(self.home.cleanup)
        os.environ.pop(config.ENV_API_KEY, None)
        os.environ.pop(config.ENV_BASE_URL, None)

    def test_no_key(self):
        self.assertEqual(config.get_api_key(), ("", "none"))

    def test_saved_key_is_owner_only(self):
        config.save_api_key("  sk-popnow-test-efgh1234  ")
        self.assertEqual(config.get_api_key(), ("sk-popnow-test-efgh1234", "file"))
        if os.name == "posix":
            mode = stat.S_IMODE(os.stat(os.path.join(self.home.name, "config.json")).st_mode)
            self.assertEqual(mode, 0o600)

    def test_environment_wins(self):
        config.save_api_key("sk-popnow-from-file-0000")
        with mock.patch.dict(os.environ, {config.ENV_API_KEY: "sk-popnow-from-env-1111"}):
            self.assertEqual(config.get_api_key(), ("sk-popnow-from-env-1111", "env"))

    def test_clear_keeps_other_settings(self):
        config.save_api_key("sk-popnow-test-efgh1234")
        config.save_max_usd_per_run("0.25")
        config.clear_api_key()
        self.assertEqual(config.get_api_key(), ("", "none"))
        self.assertEqual(config.get_max_usd_per_run(), Decimal("0.25"))

    def test_hint_never_shows_more_than_four_characters(self):
        self.assertEqual(config.key_hint("sk-popnow-test-efgh1234"), "...1234")
        self.assertEqual(config.key_hint("short"), "...")
        self.assertEqual(config.key_hint(""), "")

    def test_usd_limit(self):
        self.assertIsNone(config.get_max_usd_per_run())
        self.assertIsNone(config.save_max_usd_per_run(0))
        self.assertIsNone(config.get_max_usd_per_run())
        self.assertEqual(config.save_max_usd_per_run("1.50"), Decimal("1.5"))
        self.assertEqual(config.get_max_usd_per_run(), Decimal("1.5"))
        # Stored as an exact decimal string, never a float.
        with open(os.path.join(self.home.name, "config.json"), encoding="utf-8") as handle:
            self.assertEqual(json.load(handle)["maxUsdPerRun"], "1.5")
        # A number widget can hand over binary-float noise; it is rounded to nine decimals.
        self.assertEqual(config.save_max_usd_per_run(0.15000000000000002), Decimal("0.15"))
        self.assertEqual(config.save_max_usd_per_run("0.0000000004"), None)
        for bad in ("-1", "lots", "nan", "inf", True):
            with self.subTest(value=bad), self.assertRaises(ValueError):
                config.save_max_usd_per_run(bad)

    def test_limit_saved_in_credits_still_applies(self):
        # Version 0.1 saved the limit as maxCreditsPerRun; it keeps working at 1 credit = $0.001.
        with open(os.path.join(self.home.name, "config.json"), "w", encoding="utf-8") as handle:
            json.dump({"maxCreditsPerRun": 250}, handle)
        self.assertEqual(config.get_max_usd_per_run(), Decimal("0.25"))
        self.assertEqual(config.get_max_credits_per_run(), 250)
        # Saving a USD limit replaces the legacy one.
        config.save_max_usd_per_run("2")
        with open(os.path.join(self.home.name, "config.json"), encoding="utf-8") as handle:
            saved = json.load(handle)
        self.assertEqual(saved, {"maxUsdPerRun": "2"})

    def test_deprecated_credit_limit(self):
        self.assertIsNone(config.get_max_credits_per_run())
        self.assertIsNone(config.save_max_credits_per_run(0))
        self.assertIsNone(config.get_max_credits_per_run())
        self.assertEqual(config.save_max_credits_per_run("120"), 120)
        self.assertEqual(config.save_max_credits_per_run(30.9), 30)
        with self.assertRaises(ValueError):
            config.save_max_credits_per_run("-1")
        with self.assertRaises(ValueError):
            config.save_max_credits_per_run("lots")

    def test_base_url(self):
        self.assertEqual(config.get_base_url(), "https://api.popnow.ai")
        with mock.patch.dict(os.environ, {config.ENV_BASE_URL: "http://127.0.0.1:9000/"}):
            self.assertEqual(config.get_base_url(), "http://127.0.0.1:9000")
        with mock.patch.dict(os.environ, {config.ENV_BASE_URL: "https://api.popnow.ai/api/v1"}):
            self.assertEqual(config.get_base_url(), "https://api.popnow.ai")


if __name__ == "__main__":
    unittest.main()
