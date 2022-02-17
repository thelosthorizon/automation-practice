
from selenium.webdriver.common.by import By

SIGNIN_LINK_TEXT = "Sign in"
CONTACTUS_LINK_TEXT = "Contact Us"
SIGNOUT_LINK_TEXT = "Sign out"

class Locators(object): 
    SIGNIN_LINK = (By.LINK_TEXT, SIGNIN_LINK_TEXT)
    CONTACT_LINK = (By.LINK_TEXT, CONTACTUS_LINK_TEXT)
    SIGNOUT_LINK = (By.LINK_TEXT, SIGNOUT_LINK_TEXT)

    @staticmethod    
    def get_account_link(name):
        return (By.XPATH, "a[span[contains(text(),'{}')]]".format(name))
