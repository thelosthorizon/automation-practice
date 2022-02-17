from selenium.common.exceptions import NoSuchElementException        
from pages.base_page import BasePage
from pages.login import (
    login_form,
    login_error
)
from pages.common.header import header


class Login(BasePage):
    """This exposes all the sections/functionalities available via login page"""

    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self.login_form = login_form.LoginForm(self.driver, self.timeout)
        self.header = header.Header(self.driver, self.timeout)
    
    def signin(self, email, password):
        self.login_form.fill_in(email, password)
        self.login_form.click_submit_button()     

    def am_i_signed_in(self, name):
        try:
            self.header.navbar.account_link
        except NoSuchElementException:
            return False
        return True
    
    def log_me_out(self):
        self.header.navbar.signout_link.click()
    
    def login_should_fail(self):
        try:
            login_error.get_error_para(self.wait)
        except NoSuchElementException:
            return False
        return True
    
    def loaded(self):
        if (self.driver.title == "Login - My Store"):
            return True
        return False        


