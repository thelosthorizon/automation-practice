import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException        

from pages.page import Page
from pages.search.locators import Locators

class Results(Page):

    @property
    def number_of_hits(self):
        try:            
            hits = self.wait.until(
                EC.visibility_of_all_elements_located(Locators.SEARCH_RESULT_LIST)
            )
        except TimeoutException:
            return 0    
        return len(hits)
    
    def search_result_message(self, number):
        return self.wait.until(
            EC.visibility_of_element_located(Locators.search_result_message(number))
        )
    
    def click_any_result(self):
        hits = self.wait.until(
            EC.visibility_of_all_elements_located(Locators.SEARCH_RESULT_LIST)
        )
        random.choice(hits).click()



