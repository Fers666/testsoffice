from playwright.async_api import Page, Browser, Playwright


class BasePage:
    def __init__(self, playwright: Playwright):
        # Мы не можем здесь открыть браузер, потому что инициализатор класса не может быть асинхронным
        self.playwright: Playwright = playwright
        self.browser: Browser | None = None
        self.page: Page | None = None

    def create_browser(self):
        self.browser: Browser = self.playwright.chromium.launch(headless=False)
        self.page: Page = self.browser.new_page()

    def get(self):
        return self.browser

    def get_page(self):
        return self.page

    def get_title(self):
        return self.page.title()


    def screenshot(self, path: str):
        self.page.screenshot(path=path)

    async def close(self):
        self.browser.close()