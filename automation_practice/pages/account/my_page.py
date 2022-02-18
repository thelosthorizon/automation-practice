from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.page import Page
from pages.account.locators import Locators

class MyPage(Page):
    
    def click_personal_information_link(self):     
        email_input = self.wait.until(
            EC.visibility_of_element_located(Locators.PERSONAL_INFORMATION_LINK)
        ).click()

