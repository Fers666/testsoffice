from playwright.sync_api import Playwright, sync_playwright, expect

class CustomBrowser:
    @pytest.fixture
    def browser(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            yield page
            page.close()
            browser.close()