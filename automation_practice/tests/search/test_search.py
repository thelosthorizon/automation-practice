import pytest

@pytest.mark.small
class Test_Search():

    @pytest.mark.medium
    def test_search_and_then_view_a_result(self):   
        self.search_page.search_something("t-shirt")
        assert self.search_page.loaded()
        assert self.search_page.search_result_message_should_contain(1)        
        self.search_page.click_any_result()

    @pytest.mark.usefixtures("bogussearchterm")
    def test_bogus_searchterm(self, bogussearchterm):   
        self.search_page.search_something(bogussearchterm)
        assert self.search_page.loaded()
        assert self.search_page.search_result_message_should_contain(0)

    def test_no_searchterm(self):   
        self.search_page.search_something("")
        assert self.search_page.loaded()
        assert self.search_page.search_result_message_should_contain(0)