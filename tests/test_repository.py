"""Repository hygiene: this is a public package, written in English, about PopNow only."""

import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# CJK ideographs, kana, hangul and full-width forms, written as code points to keep this file ASCII.
RANGES = ((0x3040, 0x30FF), (0x3400, 0x4DBF), (0x4E00, 0x9FFF), (0xAC00, 0xD7AF), (0xFF00, 0xFFEF))
FOREIGN_SCRIPT = re.compile("[" + "".join(f"{chr(a)}-{chr(b)}" for a, b in RANGES) + "]")
# Names that do not belong in this repository: other platforms and model hosts. Assembled from
# pieces so this file does not match itself.
VENDOR_WORDS = [
    "sp" + "icy",
    "wave" + "speed",
    "atlas" + "cloud",
    "k" + "ie" + r"\.ai",
    r"\bk" + r"ie\b",
    "fal" + r"\.ai",
    "repli" + "cate",
]
VENDORS = re.compile("|".join(VENDOR_WORDS), re.I)


def tracked_files():
    """Tracked files plus new ones not yet added, so a file is checked before its first commit."""
    try:
        output = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        names = [line for line in output.splitlines() if line]
    except (OSError, subprocess.CalledProcessError):
        names = []
    if not names:  # not a git checkout (an installed copy): scan the files on disk instead
        names = [
            str(p.relative_to(ROOT))
            for p in ROOT.rglob("*")
            if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts
        ]
    return [ROOT / name for name in names if (ROOT / name).is_file()]


def text_files():
    texts = {}
    for path in tracked_files():
        try:
            texts[path] = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
    return texts


class RepositoryTest(unittest.TestCase):
    def test_scanners_detect_samples(self):
        # Guards the guards: a broken pattern would make the next tests pass on anything.
        self.assertTrue(FOREIGN_SCRIPT.search(chr(0x4E2D)))
        self.assertTrue(FOREIGN_SCRIPT.search(chr(0x30AB)))
        self.assertTrue(FOREIGN_SCRIPT.search(chr(0xAC00)))
        self.assertFalse(FOREIGN_SCRIPT.search("caf" + chr(0xE9) + " " + chr(0xB7) + " " + chr(0x2014)))
        self.assertTrue(VENDORS.search("Sp" + "icyAPI"))
        self.assertTrue(VENDORS.search("api." + "k" + "ie.ai"))
        self.assertFalse(VENDORS.search("stokie_en cookie kiev"))

    def test_no_foreign_script_in_tracked_files(self):
        texts = text_files()
        self.assertGreater(len(texts), 20, "too few files were read; the scan would prove nothing")
        offenders = [
            f"{path.relative_to(ROOT)}:{number}"
            for path, text in texts.items()
            for number, line in enumerate(text.splitlines(), 1)
            if FOREIGN_SCRIPT.search(line)
        ]
        self.assertEqual(offenders, [])

    def test_no_other_platform_names(self):
        texts = text_files()
        scanned = 0
        offenders = []
        for path, text in texts.items():
            relative = str(path.relative_to(ROOT))
            scanned += 1
            offenders += [f"{relative}:{n}" for n, line in enumerate(text.splitlines(), 1) if VENDORS.search(line)]
        self.assertGreater(scanned, 20)
        self.assertEqual(offenders, [])

    def test_snapshot_is_ascii(self):
        self.assertTrue((ROOT / "data" / "catalog-snapshot.json").read_text(encoding="utf-8").isascii())

    def test_no_secrets(self):
        key = re.compile(r"sk-popnow-[A-Za-z0-9]{12,}")
        offenders = [str(p.relative_to(ROOT)) for p, text in text_files().items() if key.search(text)]
        self.assertEqual(offenders, [])


if __name__ == "__main__":
    unittest.main()
