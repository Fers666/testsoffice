from sync.steps.search_page_steps import SearchPageSteps
from playwright.sync_api import sync_playwright
def search_page() -> SearchPageSteps:
    with sync_playwright() as PW:
        playwright = PW
    return SearchPageSteps(playwright)
