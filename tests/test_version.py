import re
import unittest
from pathlib import Path

from popnow_nodes import VERSION

ROOT = Path(__file__).resolve().parent.parent


class VersionTest(unittest.TestCase):
    def test_pyproject_and_package_agree(self):
        # The registry metadata reads pyproject; the User-Agent reads the package. They must not drift.
        match = re.search(r'^version = "([^"]+)"', (ROOT / "pyproject.toml").read_text(encoding="utf-8"), re.M)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), VERSION)

    def test_changelog_mentions_the_version(self):
        self.assertIn(f"## {VERSION}", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
