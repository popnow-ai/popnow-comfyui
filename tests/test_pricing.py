import json
import unittest
from pathlib import Path

from popnow_nodes.pricing import (
    badge_for,
    credits_to_usd,
    decimal_text,
    describe_price,
    format_credits,
    format_usd,
    key_value,
    match_rule,
    usd_rates,
    usd_text,
)

SNAPSHOT = Path(__file__).resolve().parent.parent / "data" / "catalog-snapshot.json"


def widget_values(badge, properties, when):
    """What the widgets would hold for a rule: its values, typed the way the schema types them."""
    values, connected = {}, set()
    for name, raw in when.items():
        target = badge["presence"].get(name)
        if target is not None:
            if raw == "true":
                connected.add(target)
            continue
        kind = (properties.get(name) or {}).get("type")
        if kind == "boolean":
            values[name] = raw == "true"
        elif kind == "integer":
            values[name] = int(raw)
        elif kind == "number":
            values[name] = float(raw)
        else:
            values[name] = raw
    return values, connected


class RuleMatchTest(unittest.TestCase):
    def test_every_published_rule_is_found_again(self):
        """Setting a node's widgets to a rule's values must show that rule's price.

        The JavaScript badge follows the same matching; if it drifted from the published rules the
        badge would silently fall back to "from x" on every node.
        """
        checked = 0
        for model in json.loads(SNAPSHOT.read_text(encoding="utf-8"))["items"]:
            badge = badge_for(model)
            self.assertIsNotNone(badge, model["model"])
            properties = model["inputSchema"].get("properties", {})
            for rule in badge["rules"]:
                values, connected = widget_values(badge, properties, rule["when"])
                same = {r["usd"] for r in badge["rules"] if r["when"] == rule["when"]}
                with self.subTest(model=model["model"], when=rule["when"]):
                    self.assertIn(match_rule(badge, values, connected), same)
                checked += 1
        self.assertGreater(checked, 1000)

    def test_snapshot_carries_usd_rates_only(self):
        for model in json.loads(SNAPSHOT.read_text(encoding="utf-8"))["items"]:
            with self.subTest(model=model["model"]):
                self.assertEqual(model["usd"]["currency"], "USD")
                self.assertIsInstance(model["usd"]["perUnit"], str)
                self.assertNotIn("credits", model)

    def test_star_means_the_single_variant_field(self):
        model = {
            "usd": {
                "unit": "per_image",
                "perUnit": "0.003",
                "rules": [{"when": {"*": "1k"}, "perUnit": "0.003"}, {"when": {"*": "2k"}, "perUnit": "0.006"}],
                "currency": "USD",
            },
            "inputSchema": {
                "x-pricing": {"variantFields": ["resolution"]},
                "properties": {"resolution": {"type": "string", "enum": ["1k", "2k"], "default": "1k"}},
            },
        }
        badge = badge_for(model)
        self.assertEqual(badge["rules"][1]["when"], {"resolution": "2k"})
        self.assertEqual(match_rule(badge, {}, set()), "0.003")
        self.assertEqual(match_rule(badge, {"resolution": "2k"}, set()), "0.006")
        self.assertEqual(badge["unit"], "image")
        self.assertEqual(badge["currency"], "USD")

    def test_most_specific_rule_wins_over_the_fallback(self):
        model = {
            "usd": {
                "unit": "per_image",
                "perUnit": "0.0015",
                "rules": [{"when": {}, "perUnit": "0.0015"}, {"when": {"enable_prompt_expansion": "true"}, "perUnit": "0.0024"}],
            },
            "inputSchema": {
                "x-pricing": {"variantFields": ["enable_prompt_expansion"]},
                "properties": {"enable_prompt_expansion": {"type": "boolean", "default": False}},
            },
        }
        badge = badge_for(model)
        self.assertEqual(match_rule(badge, {"enable_prompt_expansion": False}, set()), "0.0015")
        self.assertEqual(match_rule(badge, {"enable_prompt_expansion": True}, set()), "0.0024")

    def test_presence_follows_connections(self):
        model = {
            "usd": {
                "unit": "per_second",
                "perUnit": "0.005",
                "rules": [
                    {"when": {"with_video": "false"}, "perUnit": "0.005"},
                    {"when": {"with_video": "true"}, "perUnit": "0.003"},
                ],
            },
            "inputSchema": {"x-pricing": {"variantFields": ["with_video"], "presenceFields": {"with_video": "clips"}}},
        }
        badge = badge_for(model)
        self.assertEqual(match_rule(badge, {}, set()), "0.005")
        self.assertEqual(match_rule(badge, {}, {"clips"}), "0.003")

    def test_flat_price_has_no_rules(self):
        rates = {"unit": "per_request", "perUnit": "0.0045", "rules": [], "currency": "USD"}
        badge = badge_for({"usd": rates, "inputSchema": {}})
        self.assertEqual(match_rule(badge, {}, set()), "0.0045")
        self.assertEqual(badge["unit"], "run")

    def test_usd_wins_over_the_deprecated_credits(self):
        model = {
            "usd": {"unit": "per_image", "perUnit": "0.05", "currency": "USD"},
            "credits": {"unit": "per_image", "perUnit": 48},
            "inputSchema": {},
        }
        self.assertEqual(badge_for(model)["from"], "0.05")

    def test_legacy_credit_catalog_is_converted(self):
        # A catalog cached by version 0.1 has only the credit table; the badge still reads in USD.
        model = {
            "credits": {
                "unit": "per_second",
                "perUnit": 37,
                "rules": [{"when": {"*": "768p"}, "perUnit": 37}, {"when": {"*": "1080p"}, "perUnit": 5.55}],
                "assets": [{"when": {"enable_web_search": "true"}, "perUnit": 16.8}],
                "blocks": {"seconds": 5},
            },
            "inputSchema": {"x-pricing": {"variantFields": ["resolution"]}},
        }
        rates = usd_rates(model)
        self.assertEqual(rates["perUnit"], "0.037")
        self.assertEqual([r["perUnit"] for r in rates["rules"]], ["0.037", "0.00555"])
        self.assertEqual(rates["assets"][0]["perUnit"], "0.0168")
        self.assertEqual(rates["blocks"], {"seconds": 5})
        self.assertEqual(rates["currency"], "USD")
        badge = badge_for(model)
        self.assertEqual(badge["from"], "0.00555")
        self.assertEqual(match_rule(badge, {"resolution": "768p"}, set()), "0.037")


class FormatTest(unittest.TestCase):
    def test_format(self):
        self.assertEqual(decimal_text("0.0480"), "0.048")
        self.assertEqual(decimal_text("1E+1"), "10")
        self.assertEqual(decimal_text("0.000000001"), "0.000000001")
        self.assertEqual(usd_text("0.00555"), "$0.00555")
        self.assertEqual(usd_text("0.048"), "$0.048")
        self.assertEqual(usd_text("0.1"), "$0.10")
        self.assertEqual(usd_text("1"), "$1.00")
        self.assertEqual(usd_text("-0.5"), "-$0.50")
        self.assertEqual(usd_text(None), "")
        self.assertEqual(credits_to_usd(48), "0.048")
        self.assertEqual(credits_to_usd(5.55), "0.00555")
        self.assertIsNone(credits_to_usd("lots"))
        self.assertEqual(key_value(True), "true")
        self.assertEqual(key_value(5.0), "5")

    def test_deprecated_credit_formatters(self):
        self.assertEqual(format_credits(5.55), "5.55")
        self.assertEqual(format_credits("8.0"), "8")
        self.assertEqual(format_usd(5.55), "$0.00555")
        self.assertEqual(format_usd(100), "$0.10")
        self.assertEqual(format_usd(1000), "$1.00")

    def test_describe(self):
        flat = {"rules": [], "from": "0.048", "unit": "image"}
        self.assertEqual(describe_price(flat), "$0.048 per image.")
        tiers = {"rules": [{"usd": "0.037"}, {"usd": "0.058"}], "from": "0.037", "unit": "second"}
        self.assertEqual(describe_price(tiers), "From $0.037 per second.")
        self.assertEqual(describe_price({**flat, "approximate": True}), "About $0.048 per image.")
        self.assertEqual(describe_price(None), "")


if __name__ == "__main__":
    unittest.main()
