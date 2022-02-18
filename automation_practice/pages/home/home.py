
from pages.page import Page
from pages.common.header import header
from pages.common.footer import footer
from pages.home import main

class Home(Page):
    """This class exposes all the sections available in home page"""
    URL = "http://automationpractice.com/"

    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self.header = header.Header(self.driver, self.timeout)
        self.footer = footer.Footer(self.driver, self.timeout)  

    def load(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def click_signin_link(self):
        self.header.signin_link.click()
    
    def search_something(self, keyword):
        self.header.search(keyword)

    def loaded(self):
        if (self.driver.title == "My Store"):
            return True
        return False
