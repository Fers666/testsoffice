from playwright.sync_api import sync_playwright
from ..steps import search_page
class TestClass:
    def test_sync_2(self):
        with sync_playwright() as playwright:
            page = search_page(playwright)
            page.navigate()
            page.search("ggwp")
            page.close()





