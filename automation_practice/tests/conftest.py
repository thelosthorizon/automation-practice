import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from pages.home import home
from pages.account import account

def _chrome_driver_init():
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from webdriver_manager.chrome import ChromeDriverManager
    # ChromeDriverManager().install() to get location used by WebDriver manager and pass that to Service class
    service = ChromeService(executable_path=ChromeDriverManager().install())
    # Use the specific chrome capabilities
    options=ChromeOptions()
    return webdriver.Chrome(service=service, options=options)

def _firefox_driver_init():
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from selenium.webdriver.firefox.options import Options as FirefoxOptions 
    from webdriver_manager.firefox import GeckoDriverManager    

    # GeckoDriverManager().install() to get location used by WebDriver manager and pass that to Service class
    service = FirefoxService(executable_path=GeckoDriverManager().install())
    # Use the specific firefox capabilities
    options=FirefoxOptions()
    return webdriver.Firefox(service=service, options=options)

@pytest.fixture(scope="class", autouse=True)
def driver_init(request):
    driver = None
    browser = request.config.getoption("browser")
    if browser == "chrome":
        driver = _chrome_driver_init()
    elif browser == "firefox":
        driver = _firefox_driver_init()
    request.cls.driver = driver 
    #request.class is the test class that is using the fixture
    # we set a class variable "driver" which references WebDriver instance           
    yield
    # This portion of code will run after 
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--timeout", action="store", default=10)
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox"])   

@pytest.fixture(scope="function", autouse=True)
def timeout(request):
    yield request.config.option.timeout

@pytest.fixture
def home_page(request, timeout):
    request.instance.home_page = home.Home(request.instance.driver, timeout)
    yield