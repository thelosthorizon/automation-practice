from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException        

from pages.base_page import BasePage
from pages.login.locators import Locators

    
def generic_error_message_exists(wait):
    try:
        wait.until(
            EC.visibility_of_element_located(Locators.ERROR_MESSAGE_PARA)
        )   
    except NoSuchElementException:
        return False
    return True

def password_reset_confirmation_email_msg(wait, email):
    return wait.until(
        EC.visibility_of_element_located(Locators.password_reset_confirmation_email_para(email))
    )   

