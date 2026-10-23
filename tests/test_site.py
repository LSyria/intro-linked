"""Checks for the standalone Intro Linked HTML prototype."""
import re
import unittest
from pathlib import Path

HTML = (Path(__file__).resolve().parents[1] / "index.html").read_text(encoding="utf-8")

class IntroLinkedTests(unittest.TestCase):
    def test_page_metadata(self):
        self.assertIn("Intro Linked", HTML)
        self.assertIn('name="viewport"', HTML)
        self.assertIn("Leonard Syriaque", HTML)

    def test_video_avatar(self):
        self.assertIn('id="introVideo"', HTML)
        self.assertIn('id="avatarButton"', HTML)
        self.assertIn('data:video/mp4;base64,', HTML)

    def test_controls(self):
        self.assertIn('id="uploadIntro"', HTML)
        self.assertIn('id="recordIntro"', HTML)
        self.assertIn('id="videoProgress"', HTML)
        self.assertIn('id="videoTimer"', HTML)
        self.assertIn("URL.createObjectURL", HTML)

    def test_no_server_side_secrets(self):
        self.assertNotIn("GITHUB_TOKEN=", HTML)
        self.assertNotIn("sk-proj-", HTML)

if __name__ == "__main__":
    unittest.main()
