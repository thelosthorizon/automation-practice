import pytest

from pages.search import search

@pytest.fixture(autouse=True)
def search_page(request, timeout):
    request.instance.search_page = search.Search(request.instance.driver, timeout)
    yield

@pytest.fixture(autouse=True)
def navigate_to_home_page(request, home_page):
    request.instance.home_page.load()
    yield