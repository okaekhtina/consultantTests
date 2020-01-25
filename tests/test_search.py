from time import sleep

from pageobject.helpers import SearchHelper
import logging

logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')


def test_search(browser):
    logging.info("START")
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.enter_text('нк ч2')
    main_page.click_on_the_search_button()
    main_page.text_in_field()
    found_result = main_page.result_element()
    assert found_result, 'не выведен результат поиска'
    logging.info("SEARCH OK")


def test_open_document(browser):
    main_page = SearchHelper(browser)
    main_page.open_first_document()
    descriptors = browser.window_handles
    browser.switch_to.window(descriptors[1])
    frame = main_page.go_to_frame()
    browser.switch_to.frame(frame)
    loading_page = main_page.loading_document()
    assert loading_page, 'страница не загрузилась за 10 секунд'
