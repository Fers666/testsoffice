from playwright.sync_api import sync_playwright


class BrowserInit:
    def browser_fixture(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            yield page
            page.close()
            browser.close()