from pages.base_page import BasePage
from pages.common.header import (
    navbar
)

class Header(BasePage):
    """This class exposes all the sections available in header"""
    URL = "http://automationpractice.com/"

    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self.navbar = navbar.NavBar(self.driver, self.timeout)