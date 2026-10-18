import json
import unittest
from pathlib import Path

from popnow_nodes.pricing import badge_for, describe_price, format_credits, format_usd, key_value, match_rule

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
                same = {r["credits"] for r in badge["rules"] if r["when"] == rule["when"]}
                with self.subTest(model=model["model"], when=rule["when"]):
                    self.assertIn(match_rule(badge, values, connected), same)
                checked += 1
        self.assertGreater(checked, 1000)

    def test_star_means_the_single_variant_field(self):
        model = {
            "credits": {
                "unit": "per_image",
                "perUnit": 3,
                "rules": [{"when": {"*": "1k"}, "perUnit": 3}, {"when": {"*": "2k"}, "perUnit": 6}],
            },
            "inputSchema": {
                "x-pricing": {"variantFields": ["resolution"]},
                "properties": {"resolution": {"type": "string", "enum": ["1k", "2k"], "default": "1k"}},
            },
        }
        badge = badge_for(model)
        self.assertEqual(badge["rules"][1]["when"], {"resolution": "2k"})
        self.assertEqual(match_rule(badge, {}, set()), "3")
        self.assertEqual(match_rule(badge, {"resolution": "2k"}, set()), "6")
        self.assertEqual(badge["unit"], "image")

    def test_most_specific_rule_wins_over_the_fallback(self):
        model = {
            "credits": {
                "unit": "per_image",
                "perUnit": 1.5,
                "rules": [{"when": {}, "perUnit": 1.5}, {"when": {"enable_prompt_expansion": "true"}, "perUnit": 2.4}],
            },
            "inputSchema": {
                "x-pricing": {"variantFields": ["enable_prompt_expansion"]},
                "properties": {"enable_prompt_expansion": {"type": "boolean", "default": False}},
            },
        }
        badge = badge_for(model)
        self.assertEqual(match_rule(badge, {"enable_prompt_expansion": False}, set()), "1.5")
        self.assertEqual(match_rule(badge, {"enable_prompt_expansion": True}, set()), "2.4")

    def test_presence_follows_connections(self):
        model = {
            "credits": {
                "unit": "per_second",
                "perUnit": 5,
                "rules": [{"when": {"with_video": "false"}, "perUnit": 5}, {"when": {"with_video": "true"}, "perUnit": 3}],
            },
            "inputSchema": {"x-pricing": {"variantFields": ["with_video"], "presenceFields": {"with_video": "clips"}}},
        }
        badge = badge_for(model)
        self.assertEqual(match_rule(badge, {}, set()), "5")
        self.assertEqual(match_rule(badge, {}, {"clips"}), "3")

    def test_flat_price_has_no_rules(self):
        badge = badge_for({"credits": {"unit": "per_request", "perUnit": 4.5, "rules": []}, "inputSchema": {}})
        self.assertEqual(match_rule(badge, {}, set()), "4.5")
        self.assertEqual(badge["unit"], "run")


class FormatTest(unittest.TestCase):
    def test_format(self):
        self.assertEqual(format_credits(5.55), "5.55")
        self.assertEqual(format_credits(8), "8")
        self.assertEqual(format_credits("8.0"), "8")
        self.assertEqual(format_usd(5.55), "$0.0555")
        self.assertEqual(format_usd(8), "$0.08")
        self.assertEqual(format_usd(100), "$1.00")
        self.assertEqual(key_value(True), "true")
        self.assertEqual(key_value(5.0), "5")

    def test_describe(self):
        flat = {"rules": [], "from": "8", "unit": "image"}
        self.assertEqual(describe_price(flat), "8 credits ($0.08) per image.")
        tiers = {"rules": [{"credits": "5.55"}, {"credits": "11.1"}], "from": "5.55", "unit": "second"}
        self.assertEqual(describe_price(tiers), "From 5.55 credits ($0.0555) per second.")
        self.assertEqual(describe_price({**flat, "approximate": True}), "About 8 credits ($0.08) per image.")
        self.assertEqual(describe_price(None), "")


if __name__ == "__main__":
    unittest.main()
