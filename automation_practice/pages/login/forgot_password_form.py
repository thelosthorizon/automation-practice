from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.login.locators import Locators

class ForgotPasswordForm(BasePage):
    
    def fill_in(self, email):     
        email_input = self.wait.until(
            EC.visibility_of_element_located(Locators.FORGOT_PASSWORD_EMAIL_INPUT)
        )        
        email_input.send_keys(email)

    def click_retrieve_button(self):
        self.wait.until(
            EC.visibility_of_element_located(Locators.FORGOT_PASSWORD_RETRIEVE_BUTTON)
        ).click()