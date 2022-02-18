from selenium.webdriver.common.by import By


class Locators(object): 
    SEARCH_RESULT_LIST = (By.XPATH, "//ul[contains(@class, 'product_list')]/li")
    NO_SEARCH_RESULT_MESSAGE = (By.XPATH, '//p[contains(text(),"{}")]'.format("No results were found for your search"))

    @staticmethod    
    def search_result_message(number):
        singular_or_plural = "result has" if number else "results have"        
        return (By.XPATH, '//h1/*[contains(text(),"{} {} been found")]'.format(number, singular_or_plural))

