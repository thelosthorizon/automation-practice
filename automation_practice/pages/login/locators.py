
from selenium.webdriver.common.by import By

EMAIL_INPUT_ID = "email"
PASSWORD_INPUT_ID = "passwd"
SIGNIN_BUTTON_ID = "SubmitLogin"
PERSONAL_INFORMATION_LINK_TITLE = "My personal information"
ERROR_TEXT = "There is error"

class Locators(object): 
    EMAIL_INPUT = (By.ID, EMAIL_INPUT_ID)
    PASSWORD_INPUT = (By.ID, PASSWORD_INPUT_ID)
    SUBMIT_BUTTON = (By.ID, SIGNIN_BUTTON_ID)
    PERSONAL_INFORMATION_LINK = (By.XPATH, '//a[span[contains(text(),"{}")]]'.format(PERSONAL_INFORMATION_LINK_TITLE))
    ERROR_PARA = (By.XPATH, '//p[contains(text(),{})]]'.format(ERROR_TEXT))

