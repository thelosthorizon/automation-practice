from selenium.webdriver.common.by import By


class Locators(object): 
    MATCHING_PRODUCTS = (By.XPATH, "//ul[contains(@class, 'product_list')]/li")
