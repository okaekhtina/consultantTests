from selenium.webdriver.common.by import By
from pageobject.base_page import BasePage

timeout = 10


class Locators:
    SEARCH_FIELD = (By.ID, "dictFilter")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".doSearchBtn.flat")
    SEARCH_RESULT_ELEMENT = (By.CSS_SELECTOR, ".results.withBanners .name")
    RESULT_FIRST_DOCUMENT = (By.CSS_SELECTOR, "[index='0']")
    DOCUMENT_FRAME = (By.CSS_SELECTOR, '#mainContent > div.textContainer.visible > iframe')
    DOCUMENT_TITLE = (By.CSS_SELECTOR, '.document.title')


class SearchHelper(BasePage):

    def enter_text(self, word):
        search_field = self.find_element(Locators.SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(Locators.SEARCH_BUTTON, timeout).click()

    def text_in_field(self):
        search_field = self.find_element(Locators.SEARCH_FIELD)
        text_in_field = search_field.text
        return text_in_field

    def result_element(self):
        return self.find_element(Locators.SEARCH_RESULT_ELEMENT, time=timeout)

    def open_first_document(self):
        first_document = self.find_element(Locators.RESULT_FIRST_DOCUMENT, time=timeout)
        first_document.click()
        return first_document

    def go_to_frame(self):
        frame = self.find_element(Locators.DOCUMENT_FRAME, time=timeout)
        return frame

    def document_title(self):
        title = self.find_element(Locators.DOCUMENT_TITLE)
        title_text = title.text
        return title_text

    # def window_title(self):
    #     title = self.find_element(Locators.DOCUMENT_TITLE)
    #     title_text = title.text
    #     return title_text
