from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.page import Page
from pages.login.locators import Locators

class LoginForm(Page):
    
    def fill_in(self, email, password):     
        email_input = self.wait.until(
            EC.visibility_of_element_located(Locators.LOGIN_EMAIL_INPUT)
        )        
        password_input = self.wait.until(
            EC.visibility_of_element_located(Locators.LOGIN_PASSWORD_INPUT)
        )
        email_input.send_keys(email)
        password_input.send_keys(password)

    def click_submit_button(self):
        self.wait.until(
            EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON)
        ).click()

    def click_forgot_password_link(self):
        self.wait.until(
            EC.visibility_of_element_located(Locators.LOGIN_FORGOT_PASSWORD_LINK)
        ).click()
    
    
    @property
    def error_para(self):
        return self.wait.until(
            EC.visibility_of_element_located(Locators.LOGIN_ERROR_PARA)
        )        

