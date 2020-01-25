from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Locators:
    # SEARCH_FIELD = (By.CSS_SELECTOR, ".filterContainer")
    SEARCH_FIELD = (By.ID, "dictFilter")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".doSearchBtn.flat")
    SEARCH_RESULT_ELEMENT = (By.CSS_SELECTOR, ".results.withBanners .name")


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://base.consultant.ru/cons/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)


class SearchHelper(BasePage):

    def enter_text(self, word):
        search_field = self.find_element(Locators.SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(Locators.SEARCH_BUTTON, time=2).click()

    def text_in_field(self):
        search_field = self.find_element(Locators.SEARCH_FIELD)
        text_in_field = search_field.text
        return text_in_field

    def result_element(self):
        return self.find_element(Locators.SEARCH_RESULT_ELEMENT, time=10)
