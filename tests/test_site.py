from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    REPO_ROOT / "index.html",
    REPO_ROOT / "about/arc/index.html",
    REPO_ROOT / "about/dues/index.html",
    REPO_ROOT / "about/gate/index.html",
    REPO_ROOT / "about/links/index.html",
    REPO_ROOT / "board/index.html",
    REPO_ROOT / "contact/index.html",
]


class StaticSiteTests(unittest.TestCase):
    def test_expected_pages_exist(self) -> None:
        for page in PAGES:
            self.assertTrue(page.exists(), f"Missing page: {page}")

    def test_removed_documents_and_events_navigation(self) -> None:
        for page in PAGES:
            content = page.read_text(encoding="utf-8")
            self.assertNotIn(">Documents<", content)
            self.assertNotIn(">Events<", content)
            self.assertNotIn("HOA Updates/Reminders", content)
            self.assertNotIn("January 31st 2024", content)

    def test_homepage_links_to_current_resources(self) -> None:
        content = (REPO_ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("/assets/files/ccrs.pdf", content)
        self.assertIn("/assets/files/arc-guidelines.pdf", content)
        self.assertIn("/assets/files/arc-request-form.pdf", content)
        self.assertIn("/assets/files/pavilion-use-form.pdf", content)

    def test_required_assets_exist(self) -> None:
        assets = [
            REPO_ROOT / "assets/site.css",
            REPO_ROOT / "assets/images/logo-small.jpg",
            REPO_ROOT / "assets/images/hero.jpg",
            REPO_ROOT / "assets/files/ccrs.pdf",
        ]
        for asset in assets:
            self.assertTrue(asset.exists(), f"Missing asset: {asset}")


if __name__ == "__main__":
    unittest.main()
