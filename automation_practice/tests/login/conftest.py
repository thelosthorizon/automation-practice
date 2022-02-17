import pytest

from pages.login import login

@pytest.fixture
def login_page(request, timeout):
    request.instance.login_page = login.Login(request.instance.driver, timeout)
    yield

@pytest.fixture
def userdata(request):
    yield {
        "type": "valid",
        "firstname": "Sulav",
        "lastname": "Ghimire",
        "email": "swatantra.thtlive+automationpractice@gmail.com", 
        "password": "Test123."
    }

