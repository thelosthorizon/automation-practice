
from selenium.webdriver.common.by import By

class Locators(object): 
    SIGNIN_LINK = (By.LINK_TEXT, "Sign in")
    CONTACT_LINK = (By.LINK_TEXT, "Contact Us")
    SIGNOUT_LINK = (By.LINK_TEXT, "Sign out")
    SEARCHBAR_INPUT = (By.CSS_SELECTOR, 'input#{}'.format("search_query_top"))
    SEARCHBAR_SEARCH_ICON = (By.XPATH, "//form[@id='searchbox']/button[@type='submit']")

    @staticmethod    
    def account_link(name):
        return (By.XPATH, '//a[./span[contains(text(),"{}")]]'.format(name))
