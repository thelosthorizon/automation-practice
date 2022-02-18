import pytest

@pytest.mark.small
class Test_Search():

    def test_valid_keyword(self):   
        self.search_page.search_something("t-shirt")
        assert self.search_page.loaded()
        assert self.search_page.count_results == 1
