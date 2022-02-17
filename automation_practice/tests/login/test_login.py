import pytest
from pages.account import account

@pytest.mark.small
@pytest.mark.usefixtures("chrome_driver_init")
class Test_Login():
    
    @pytest.mark.usefixtures("home_page", "login_page", "userdata")
    def test_valid_login(self, userdata):
        self.home_page.load()
        self.home_page.click_signin_link()
        self.login_page.signin(userdata["email"], userdata["password"])
        assert self.login_page.am_i_signed_in(" ".join([userdata["firstname"], userdata["lastname"]]))
        self.login_page.log_me_out()
        assert self.login_page.loaded()


    @pytest.mark.usefixtures("home_page", "login_page")
    @pytest.mark.parametrize('email,password', [("test@test.com", "iabdib"), ("test@test.com", ""), ("", "")])
    def test_invalid_login(self, email, password):
        self.home_page.load()
        self.home_page.click_signin_link()
        self.login_page.signin(email, password)
        assert self.login_page.login_should_fail


