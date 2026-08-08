"""Tests for the profile README validator."""

import tempfile
import unittest
from pathlib import Path

from scripts.validate_readme import validate_readme


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class ValidateReadmeTests(unittest.TestCase):
    def validate_text(self, text: str) -> list[str]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(text, encoding="utf-8")
            (root / "LICENSE").write_text("MIT\n", encoding="utf-8")
            return validate_readme(root / "README.md")

    def test_repository_readme_is_valid(self):
        self.assertEqual(validate_readme(REPOSITORY_ROOT / "README.md"), [])

    def test_duplicate_links_are_rejected(self):
        text = (REPOSITORY_ROOT / "README.md").read_text(encoding="utf-8")
        text += "\n[Duplicate](https://jovanipink.com)\n"

        errors = self.validate_text(text)

        self.assertTrue(any("Duplicate link targets" in error for error in errors))

    def test_insecure_external_links_are_rejected(self):
        text = (REPOSITORY_ROOT / "README.md").read_text(encoding="utf-8")
        text = text.replace("https://jovanipink.com", "http://jovanipink.com")

        errors = self.validate_text(text)

        self.assertTrue(any("must use HTTPS" in error for error in errors))

    def test_missing_relative_links_are_rejected(self):
        text = (REPOSITORY_ROOT / "README.md").read_text(encoding="utf-8")
        text = text.replace("[MIT License](LICENSE)", "[MIT License](MISSING.md)")

        errors = self.validate_text(text)

        self.assertTrue(any("does not exist" in error for error in errors))

    def test_section_contract_is_enforced(self):
        text = (REPOSITORY_ROOT / "README.md").read_text(encoding="utf-8")
        text = text.replace("## Core capabilities", "## Skills")

        errors = self.validate_text(text)

        self.assertTrue(any("Level-two sections" in error for error in errors))

    def test_legacy_bullets_are_rejected(self):
        text = (REPOSITORY_ROOT / "README.md").read_text(encoding="utf-8")
        text += "\n● Placeholder\n"

        errors = self.validate_text(text)

        self.assertTrue(any("decorative bullet" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
