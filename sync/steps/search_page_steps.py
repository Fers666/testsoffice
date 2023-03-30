from sync.pages.search_page import SearchPage
from playwright.sync_api import sync_playwright

class SearchPageSteps(SearchPage):
    @property
    def search_page() -> SearchPage:
        # with sync_playwright() as PW:
        #     playwright = PW
        return SearchPage

    def navigate(self):
        self.search_page.page.goto("https://bing.com")

    def search(self, text):
        self.search_page.input_field.fill(text)
        self.search_page.input_field.press("Enter")
        # self.input_field().fill(text)
        # self.input_field().press("Enter")
