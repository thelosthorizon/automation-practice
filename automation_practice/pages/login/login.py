from selenium.common.exceptions import NoSuchElementException        
from pages.login import (
    login_form,
    notifications,
    signup_form,
    pre_signup_form,
    forgot_password_form
)
from pages.common.header import header
from pages.common.footer import footer
from pages.page import Page


class Login(Page):
    """This exposes all the sections/functionalities available via login page"""

    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self.header = header.Header(self.driver, self.timeout)
        self.footer = footer.Footer(self.driver, self.timeout)        
        self.login_form = login_form.LoginForm(self.driver, self.timeout)
        self.pre_signup_form = pre_signup_form.PreSignupForm(self.driver, self.timeout)
        self.signup_form = signup_form.SignupForm(self.driver, self.timeout)
        self.forgot_password_form = forgot_password_form.ForgotPasswordForm(self.driver, self.timeout)
    
    def login(self, email, password):
        self.login_form.fill_in(email, password)
        self.login_form.click_submit_button()     

    def am_i_logged_in(self, name):
        try:
            self.header.account_link(name)
        except NoSuchElementException:
            return False
        return True
    
    def log_me_out(self):
        self.header.signout_link.click()
    
    def login_failed(self):
        return notifications.generic_error_message_exists(self.wait)

    def sign_me_up(self, newuserdata):
        self.pre_signup_form.fill_in(newuserdata["Email"])
        self.pre_signup_form.click_submit_button()
        self.signup_form.fill_in_personal_data(newuserdata)
        self.signup_form.fill_in_address_data(newuserdata)
        self.signup_form.click_submit_button()

    def forgot_password(self, email):
        self.login_form.click_forgot_password_link()
        self.forgot_password_form.fill_in(email)
        self.forgot_password_form.click_retrieve_button()

    def password_reset_confirmation_email_sent(self, email):
        try:
            notifications.password_reset_confirmation_email_msg(self.wait, email)
        except NoSuchElementException:
            return False
        return True

    def password_reset_failed(self):
        return notifications.generic_error_message_exists(self.wait)

    def loaded(self):
        if (self.driver.title == "Login - My Store"):
            return True
        return False        


