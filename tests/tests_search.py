import asyncio

import pytest
from playwright.async_api import async_playwright
from pages.search_page import SearchPage

@pytest.mark.asyncio
async def test_input():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)

        page = await browser.new_page()
        search_page = SearchPage(page)
        await search_page.navigate()
        await search_page.search("search query")
        await page.screenshot(path=f"screenshots\\example.png")
        print(await page.title())
        await browser.close()
# asyncio.run(test_input())