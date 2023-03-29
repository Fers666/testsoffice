from playwright.sync_api import sync_playwright
from pages.search_page import SearchPage


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)

    page = browser.new_page()
    search_page = SearchPage(page)
    search_page.navigate()
    search_page.search("search query")
    page.screenshot(path="screenshots\\example.png")
    print(page.title())
    browser.close()