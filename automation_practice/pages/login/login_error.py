from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.account.locators import Locators

    
def get_error_para(wait):
    return wait.until(
        EC.visibility_of_element_located(Locators.ERROR_PARA)
    )        
