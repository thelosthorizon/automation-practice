import pytest
from pages.account import account

@pytest.mark.small
class Test_Login():

    @pytest.mark.usefixtures("newuserdata")
    def test_signup(self, newuserdata):       
        self.login_page.sign_me_up(newuserdata)
        assert self.login_page.am_i_logged_in(" ".join([newuserdata["First name"], newuserdata["Last name"]]))
        self.login_page.log_me_out()

    @pytest.mark.usefixtures("existinguserdata")
    def test_valid_login(self, existinguserdata):   
        self.login_page.login(existinguserdata["Email"], existinguserdata["Password"])
        assert self.login_page.am_i_logged_in(" ".join([existinguserdata["First name"], existinguserdata["Last name"]]))
        self.login_page.log_me_out()
        assert self.login_page.loaded()

    @pytest.mark.parametrize('email,password', [("test@test.com", "iabdib"), ("test@test.com", ""), ("", "")])
    def test_invalid_login(self, email, password):
        self.login_page.login(email, password)
        assert self.login_page.login_failed()

    @pytest.mark.usefixtures("existinguserdata")
    def test_forgot_password_registered_account(self, existinguserdata):
        self.login_page.forgot_password(existinguserdata["Email"])
        assert self.login_page.password_reset_confirmation_email_sent(existinguserdata["Email"])

    @pytest.mark.usefixtures("bogusemail")
    def test_forgot_password(self, bogusemail):
        self.login_page.forgot_password(bogusemail)
        assert self.login_page.password_reset_failed()

