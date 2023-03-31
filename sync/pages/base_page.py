from playwright.sync_api import Page, Browser, Playwright, sync_playwright

class BasePage:
    def __init__(self, playwright):
        self.browser: Browser = playwright.chromium.launch(headless=False)
        self.page: Page = self.browser.new_page()

    def get(self):
        return self.browser

    def get_page(self):
        return self.page

    def get_title(self):
        return self.page.title()

    def screenshot(self, path: str):
        self.page.screenshot(path=path)

    def close(self):
        self.browser.close()