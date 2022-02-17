import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

from pages.home import home
from pages.account import account

@pytest.fixture(scope="class", autouse=True)
def chrome_driver_init(request):
    # ChromeDriverManager().install() to get location used by WebDriver manager and pass that to Service class
    service = ChromeService(executable_path=ChromeDriverManager().install())
    # Use the specific chrome capabilities
    options=ChromeOptions()
    chrome_driver = webdriver.Chrome(service=service, options=options)
    #request.class is the test class that is using the fixture
    # we set a class variable "driver" which references WebDriver instance
    request.cls.driver = chrome_driver        
    yield
    # This portion of code will run after 
    chrome_driver.close()

def pytest_addoption(parser):
    parser.addoption("--timeout", action="store", default=20)

@pytest.fixture(scope="function", autouse=True)
def timeout(request):
    yield request.config.option.timeout

@pytest.fixture
def home_page(request, timeout):
    request.instance.home_page = home.Home(request.instance.driver, timeout)
    yield