from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.page import Page
from pages.login.locators import Locators

class PreSignupForm(Page):
    
    def fill_in(self, email):     
        email_input = self.wait.until(
            EC.visibility_of_element_located(Locators.CREATE_ACCOUNT_EMAIL_INPUT)
        )        
        email_input.send_keys(email)

    def click_submit_button(self):
        self.wait.until(
            EC.visibility_of_element_located(Locators.CREATE_ACCOUNT_SUBMIT_BUTTON)
        ).click()
    
