import pytest
from playwright.async_api import async_playwright
from async_pw.steps.search_page_steps import SearchPageSteps


@pytest.mark.asyncio
async def test_async():
    async with async_playwright() as playwright:
        search_page = SearchPageSteps(playwright)
        # Для синхроннки мы бы это сделали в конструкторе
        await search_page.create_browser()
        await search_page.navigate()
        await search_page.search("search query")
        await search_page.screenshot("screenshots\\example.png")

        print(await search_page.get_title())

        await search_page.close()