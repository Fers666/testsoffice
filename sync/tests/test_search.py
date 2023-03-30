import pytest
from playwright.sync_api import sync_playwright
# from sync.steps.search_page_steps import SearchPageSteps
from sync.steps import steps

def test_sync():
    # with sync_playwright() as playwright:
    #     search_page = SearchPageSteps(playwright)

        # search_page.navigate()
        # search_page.search("search query")
        #
        # search_page.screenshot("screenshots\\example.png")
        #
        # print(search_page.get_title())


        # search_page.close()
    # with sync_playwright() as playwright:
        steps.search_page().navigate()
        steps.search_page().close()
