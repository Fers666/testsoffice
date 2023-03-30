import pytest
from playwright.sync_api import sync_playwright
from sync.steps.search_page_steps import SearchPageSteps

async def test_async():
    with sync_playwright() as playwright:
        search_page = SearchPageSteps(playwright)
        # Для синхроннки мы бы это сделали в конструкторе
        search_page.create_browser()
        search_page.navigate()
        search_page.search("search query")
        search_page.screenshot("screenshots\\example.png")

        print(search_page.get_title())

        search_page.close()