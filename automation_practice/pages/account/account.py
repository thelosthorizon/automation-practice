from selenium.common.exceptions import NoSuchElementException        
from pages.base_page import BasePage
from pages.account import (
    my_page

)
from pages.common.header import header


class Account(BasePage):
    """This exposes all the sections/functionalities available via account page"""

    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self.header = header.Header(self.driver, self.timeout)
        self.profile = my_page.Profile(self.driver, self.timeout)


