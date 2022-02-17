from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.account.locators import Locators

class MyPage(BasePage):
    
    def click_personal_information_link(self):     
        email_input = self.wait.until(
            EC.visibility_of_element_located(Locators.PERSONAL_INFORMATION_LINK)
        ).click()

