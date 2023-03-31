from playwright.sync_api import Locator

from ..pages.base_page import BasePage


class SearchPage(BasePage):
    @property
    def input_field(self) -> Locator:
        return self.page.locator('[aria-label="Enter your search term"]')


