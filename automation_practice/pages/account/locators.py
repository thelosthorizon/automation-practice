
from selenium.webdriver.common.by import By

class Locators(object): 
    PERSONAL_INFORMATION_LINK = (By.XPATH, '//a[span[contains(text(),"{}")]]'.format( "My personal information"))

