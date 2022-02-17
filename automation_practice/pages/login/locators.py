
from selenium.webdriver.common.by import By

class Locators(object): 
    ERROR_MESSAGE_PARA = (By.XPATH, '//p[contains(text(),"{}") and contains(text(),"{}")]'.format("There is", "error"))

    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, 'input#{}'.format("email"))
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input#{}'.format("passwd"))
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button#{}'.format("SubmitLogin"))
    LOGIN_FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot your password?")

    CREATE_ACCOUNT_EMAIL_INPUT = (By.CSS_SELECTOR, 'input#{}'.format("email_create"))
    CREATE_ACCOUNT_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button#{}'.format("SubmitCreate"))

    SIGNUP_PERSONAL_FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input#{}'.format("customer_firstname"))
    SIGNUP_PERSONAL_LASTNAME_INPUT = (By.CSS_SELECTOR, 'input#{}'.format("customer_lastname"))
    SIGNUP_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input#{}'.format("passwd"))

    SIGNUP_ADDRESS_FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input#{}'.format("firstname"))
    SIGNUP_ADDRESS_LASTNAME_INPUT = (By.CSS_SELECTOR, 'input#{}'.format("lastname"))
    SIGNUP_ADDRESS_INPUT = (By.CSS_SELECTOR, 'input#{}'.format("address1"))
    SIGNUP_CITY_INPUT = (By.CSS_SELECTOR, 'input#{}'.format("city"))
    SIGNUP_STATE_SELECT = (By.CSS_SELECTOR, 'select#{}'.format("id_state"))
    SIGNUP_POSTCODE_INPUT = (By.CSS_SELECTOR, 'input#{}'.format("postcode"))
    SIGNUP_COUNTRY_SELECT = (By.CSS_SELECTOR, 'select#{}'.format("id_country"))
    SIGNUP_PHONE_INPUT = (By.CSS_SELECTOR, 'input#{}'.format("phone_mobile"))
    SIGNUP_ADDRESS_ALIAS_INPUT = (By.CSS_SELECTOR, 'input#{}'.format("alias"))
    SIGNUP_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button#{}'.format("submitAccount"))


    FORGOT_PASSWORD_EMAIL_INPUT = (By.CSS_SELECTOR, 'input#{}'.format("email"))
    FORGOT_PASSWORD_RETRIEVE_BUTTON = (By.XPATH, '//button[./span[contains(text(),"{}")]]'.format("Retrieve Password"))

    PERSONAL_INFORMATION_LINK = (By.XPATH, '//a[./span[contains(text(),"{}")]]'.format("My personal information"))

    @staticmethod    
    def password_reset_confirmation_email_para(email):
        return (By.XPATH, '//p[contains(text(),"A confirmation email has been sent to your address: {}")]'.format(email))



