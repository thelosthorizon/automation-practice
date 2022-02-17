from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.common.header.locators import Locators

class NavBar(BasePage):

    @property
    def signin_link(self):
        return self.wait.until(
            EC.visibility_of_element_located(Locators.SIGNIN_LINK)
        )

    @property
    def contact_us_link(self):
        return self.wait.until(
            EC.visibility_of_element_located(Locators.CONTACTUS_LINK)
        )

    @property
    def signout_link(self):
        return self.wait.until(
            EC.visibility_of_element_located(Locators.SIGNOUT_LINK)
        )

    def account_link(self, name):
        return self.wait.until(
            EC.visibility_of_element_located(Locators.account_link(name))
        )
        

