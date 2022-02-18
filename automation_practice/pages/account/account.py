from selenium.common.exceptions import NoSuchElementException        
from pages.account import (
    my_page
)
from pages.common.header import header
from pages.common.footer import footer
from pages.page import Page



class Account(Page):
    """This exposes all the sections/functionalities available via account page"""

    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self.header = header.Header(self.driver, self.timeout)
        self.footer = footer.Footer(self.driver, self.timeout)           
        self.my_page = my_page.MyPage(self.driver, self.timeout)


