from sync.pages.search_page import SearchPage


class SearchPageSteps(SearchPage):
    def navigate(self):
        self.page.goto("https://bing.com")

    def search(self, text):
        self.input_field().fill(text)
        self.input_field().press("Enter")