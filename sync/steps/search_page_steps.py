from typing import Type
from sync.pages.search_page import SearchPage
from playwright.sync_api import sync_playwright

class SearchPageSteps(SearchPage):
    @property
    def search_page_func(self) -> Type[SearchPage]:
        return SearchPage

    def navigate(self):
        # self.search_page_func.page.goto("https://bing.com")
        self.search_page_func.get_page().goto("https://bing.com")

    def search(self, text):
        self.search_page_func.input_field().fill(text)
        self.search_page_func.input_field().press("Enter")
        # self.input_field().fill(text)
        # self.input_field().press("Enter")
