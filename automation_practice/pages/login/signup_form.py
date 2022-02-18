from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from pages.page import Page
from pages.login.locators import Locators

import time


class SignupForm(Page):
    
    def fill_in_personal_data(self, newuserdata):     
        firstname_input = self.wait.until(
            EC.visibility_of_element_located(Locators.SIGNUP_PERSONAL_FIRSTNAME_INPUT)
        )  
        firstname_input.send_keys(newuserdata["First name"])
      
        lastname_input = self.wait.until(
            EC.visibility_of_element_located(Locators.SIGNUP_PERSONAL_LASTNAME_INPUT)
        )
        lastname_input.send_keys(newuserdata["Last name"])

        password_input = self.wait.until(
            EC.visibility_of_element_located(Locators.SIGNUP_PASSWORD_INPUT)
        )
        password_input.send_keys(newuserdata["Password"])

        self.driver.execute_script("arguments[0].scrollIntoView()", password_input)

    def fill_in_address_data(self, newuserdata):     

        firstname_input = self.wait.until(
            EC.visibility_of_element_located(Locators.SIGNUP_ADDRESS_FIRSTNAME_INPUT)
        )  
        firstname_input.send_keys(newuserdata["First name"])
      
        lastname_input = self.wait.until(
            EC.visibility_of_element_located(Locators.SIGNUP_ADDRESS_LASTNAME_INPUT)
        )
        lastname_input.send_keys(newuserdata["Last name"])

        address = self.wait.until(
            EC.visibility_of_element_located(Locators.SIGNUP_ADDRESS_INPUT)
        )
        address.send_keys(newuserdata["Address"])

        city_input = self.wait.until(
            EC.visibility_of_element_located(Locators.SIGNUP_CITY_INPUT)
        )

        self.driver.execute_script("arguments[0].scrollIntoView()", city_input)

        city_input.send_keys(newuserdata["City"])

        state_select = self.wait.until(
            EC.presence_of_element_located(Locators.SIGNUP_STATE_SELECT)
        )

        Select(state_select).select_by_visible_text(newuserdata["State"])

        postcode_input = self.wait.until(
            EC.visibility_of_element_located(Locators.SIGNUP_POSTCODE_INPUT)
        )

        postcode_input.send_keys(newuserdata["Postal Code"])

        self.driver.execute_script("arguments[0].scrollIntoView()", postcode_input)

        country_select = self.wait.until(
            EC.presence_of_element_located(Locators.SIGNUP_COUNTRY_SELECT)
        )
        
        Select(country_select).select_by_visible_text(newuserdata["Country"])

        phone_input = self.wait.until(
            EC.visibility_of_element_located(Locators.SIGNUP_PHONE_INPUT)
        )  
        phone_input.send_keys(newuserdata["Mobile Phone"])
             
        address_alias_input = self.wait.until(
            EC.element_to_be_clickable(Locators.SIGNUP_ADDRESS_ALIAS_INPUT)
        )           
        address_alias_input.clear()
        address_alias_input.send_keys(newuserdata["Address Alias"])

    def click_submit_button(self):
        self.wait.until(
            EC.visibility_of_element_located(Locators.SIGNUP_SUBMIT_BUTTON)
        ).click()
