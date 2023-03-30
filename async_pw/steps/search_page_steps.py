from async_pw.pages.search_page import SearchPage


class SearchPageSteps(SearchPage):
    async def navigate(self):
        await self.page.goto("https://bing.com")

    async def search(self, text):
        await self.input_field().fill(text)
        await self.input_field().press("Enter")