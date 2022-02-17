from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.account.locators import Locators

class LoginForm(BasePage):
    
    def fill_in(self, email, password):     
        email_input = self.wait.until(
            EC.visibility_of_element_located(Locators.EMAIL_INPUT)
        )        
        password_input = self.wait.until(
            EC.visibility_of_element_located(Locators.PASSWORD_INPUT)
        )
        email_input.send_keys(email)
        password_input.send_keys(password)

    def click_submit_button(self):
        self.wait.until(
            EC.visibility_of_element_located(Locators.SUBMIT_BUTTON)
        ).click()
    
    @property
    def error_para(self):
        return self.wait.until(
            EC.visibility_of_element_located(Locators.ERROR_PARA)
        )        

