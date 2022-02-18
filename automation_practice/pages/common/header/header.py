from pages.page import Page
from pages.common.header import (
    navbar,
    searchbar
)

class Header(Page):
    """This class exposes all the sections available in header"""

    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self.navbar = navbar.NavBar(self.driver, self.timeout)
        self.searchbar = searchbar.SearchBar(self.driver, self.timeout)

    @property
    def signin_link(self):
        return self.navbar.signin_link

    @property
    def contact_us_link(self):
        return self.navbar.contact_us_link

    @property
    def signout_link(self):
        return self.navbar.signout_link

    def account_link(self, name):
        return self.navbar.account_link(name)
    
    def search(self, keyword):
        self.searchbar.type_search_keyword(keyword)
        self.searchbar.click_search_icon()

