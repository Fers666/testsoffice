from playwright.async_api import  Locator

from async_pw.pages.base_page import BasePage


class SearchPage(BasePage):

    def input_field(self) -> Locator:
        return self.page.locator('[aria-label="Enter your search term"]')
