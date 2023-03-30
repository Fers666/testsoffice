from playwright.async_api import Page, Browser, Playwright


class BasePage:
    def __init__(self, playwright: Playwright):
        # Мы не можем здесь открыть браузер, потому что инициализатор класса не может быть асинхронным
        self.playwright: Playwright = playwright
        self.browser: Browser | None = None
        self.page: Page | None = None

    async def create_browser(self):
        self.browser: Browser = await self.playwright.chromium.launch(headless=False)
        self.page: Page = await self.browser.new_page()

    def get(self):
        return self.browser

    def get_page(self):
        return self.page

    async def get_title(self):
        return await self.page.title()


    async def screenshot(self, path: str):
        await self.page.screenshot(path=path)

    async def close(self):
        await self.browser.close()