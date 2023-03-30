from playwright.sync_api import sync_playwright
import pytest
from pages.search_page import SearchPage
from core.browser import BrowserInit

# async def get_browser():
#     browser = BrowserInit()
#     page = await browser.browser_fixture()
#     return page

def browser_fixture():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        browser.close()

def test_1():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        # page = browser_fixture()
        search_page = SearchPage(page)
        search_page.navigate()
        # await search_page.search("search query")
        # await page.screenshot(path=f"screenshots\\example.png")
        # print(page.title())


