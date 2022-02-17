from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):
    def __init__ (self, driver, timeout):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)
