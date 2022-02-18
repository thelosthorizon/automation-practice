from selenium.webdriver.support import expected_conditions as EC

from pages.page import Page
from pages.search.locators import Locators

class Results(Page):

    @property
    def number_of_matching_products(self):
        return len(self.wait.until(
            EC.visibility_of_all_elements_located(Locators.MATCHING_PRODUCTS)
        ))
