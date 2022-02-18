from selenium.webdriver.support import expected_conditions as EC

from pages.page import Page
from pages.common.header.locators import Locators

class SearchBar(Page):

    def type_search_keyword(self, keyword):
        search_input = self.wait.until(
            EC.visibility_of_element_located(Locators.SEARCHBAR_INPUT)
        )
        search_input.send_keys(keyword)


    def click_search_icon(self):
        search_icon = self.wait.until(
            EC.element_to_be_clickable(Locators.SEARCHBAR_SEARCH_ICON)
        )
        search_icon.click()
