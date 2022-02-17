import pytest

from pages.login import login
from utilities import random_user_data
from utilities.common import generate_random_string

@pytest.fixture(autouse=True)
def login_page(request, timeout):
    request.instance.login_page = login.Login(request.instance.driver, timeout)
    yield

@pytest.fixture(autouse=True)
def navigate_to_login_page(request, home_page):
    request.instance.home_page.load()
    request.instance.home_page.click_signin_link()  
    yield

@pytest.fixture
def existinguserdata():
    # Setting all the field name same as the signup form 
    yield {
        "First name": "SGTestFirstName",
        "Last name": "SGTestLastName",
        "Email": "sg@test.automation.practice.com", 
        "Password": "Test123.",
        "Address": "SGTestAddress",
        "City": "SGTestCity",
        "State": "Alabama",
        "Postal Code": 12345,
        "Country": "United States",
        "Mobile Phone": 123456789,
        "Address Alias": "My Address"
    }

@pytest.fixture
def newuserdata():
    yield random_user_data.generate(prefix="SG")

@pytest.fixture
def bogusemail():
    yield "@".join((generate_random_string(size=10), generate_random_string(size=10, suffix=".com"))) 
