from ..steps.search_page_steps import SearchPageSteps
def search_page(playwright) -> SearchPageSteps:
    return SearchPageSteps(playwright)


