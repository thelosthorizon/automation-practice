from pages.common.header import header

from pages.search import (
    results
)
from pages.common.header import header
from pages.common.footer import footer
from pages.page import Page

class Search(Page):
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self.header = header.Header(self.driver, self.timeout)
        self.footer = footer.Footer(self.driver, self.timeout)           
        self.results = results.Results(self.driver, self.timeout)
    
    def search_something(self, keyword):
        self.header.search(keyword)

    @property    
    def count_results(self):
        return self.results.number_of_matching_products
    
    def loaded(self):
        if (self.driver.title == "Search - My Store"):
            return True
        return False
