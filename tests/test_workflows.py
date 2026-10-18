"""The example workflows in example_workflows/ load against the nodes this package builds."""

import json
import unittest
from pathlib import Path

from . import comfy_stub

try:
    import aiohttp  # noqa: F401
except ImportError:  # pragma: no cover - only when run outside a ComfyUI environment
    aiohttp = None

if aiohttp is not None:
    comfy_stub.install()
    from popnow_nodes import nodes

ROOT = Path(__file__).resolve().parent.parent
CORE_NODES = {"LoadImage", "SaveImage", "PreviewImage", "SaveVideo", "SaveAudio"}
WIDGETS = {"STRING", "INT", "FLOAT", "BOOLEAN", "COMBO"}


@unittest.skipIf(aiohttp is None, "aiohttp is not installed")
class WorkflowTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        items = json.loads((ROOT / "data" / "catalog-snapshot.json").read_text(encoding="utf-8"))["items"]
        built, _ = nodes.build_all(items)
        cls.schemas = {n.GET_SCHEMA().node_id: n.GET_SCHEMA() for n in built}

    def test_examples_exist(self):
        self.assertGreaterEqual(len(list((ROOT / "example_workflows").glob("*.json"))), 5)

    def test_every_node_and_widget_is_known(self):
        for path in sorted((ROOT / "example_workflows").glob("*.json")):
            graph = json.loads(path.read_text(encoding="utf-8"))
            for node in graph["nodes"]:
                with self.subTest(workflow=path.name, node=node["type"]):
                    if node["type"] in CORE_NODES:
                        continue
                    self.assertIn(node["type"], self.schemas)
                    schema = self.schemas[node["type"]]
                    widgets = {i.name: i for i in schema.inputs if i.socket in WIDGETS}
                    named = {k: v for k, v in node["widgets_values_named"].items() if k != "control_after_generate"}
                    self.assertEqual(list(named), list(widgets))
                    for name, value in named.items():
                        if widgets[name].socket == "COMBO":
                            self.assertIn(value, widgets[name].options["options"])

    def test_links_point_at_real_slots(self):
        for path in sorted((ROOT / "example_workflows").glob("*.json")):
            graph = json.loads(path.read_text(encoding="utf-8"))
            by_id = {n["id"]: n for n in graph["nodes"]}
            for link_id, src, src_slot, dst, dst_slot, kind in graph["links"]:
                with self.subTest(workflow=path.name, link=link_id):
                    self.assertEqual(by_id[src]["outputs"][src_slot]["type"], kind)
                    self.assertIn(link_id, by_id[src]["outputs"][src_slot]["links"])
                    self.assertEqual(by_id[dst]["inputs"][dst_slot]["link"], link_id)


if __name__ == "__main__":
    unittest.main()
