from pageobject.helpers import SearchHelper
import logging

logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')


def test_search(browser):
    logging.info("Open search page")
    main_page = SearchHelper(browser)
    logging.info("Enter text")
    main_page.enter_text('нк ч2')
    logging.info("Click on find button")
    main_page.click_on_the_search_button()
    logging.info("Get search result")
    found_result = main_page.result_element()
    assert found_result, 'Не выведен результат поиска'
    logging.info("Search OK")


def test_open_document(browser):
    main_page = SearchHelper(browser)
    logging.info("Click on found document")
    main_page.open_first_document()
    logging.info("Get opened page name")
    descriptors = browser.window_handles
    logging.info("Swith to opened page")
    browser.switch_to.window(descriptors[1])
    logging.info("Get frame with text on the page")
    frame = main_page.go_to_frame()
    logging.info("Swith to frame")
    browser.switch_to.frame(frame)
    logging.info("Wait until page loaded")
    loading_page = main_page.document_title()
    assert loading_page, 'Страница не загрузилась за 10 секунд'


def test_document_name(browser):
    main_page = SearchHelper(browser)
    logging.info("Get document title")
    title = main_page.document_title().lower()
    assert "налоговый кодекс" in title
    assert "часть вторая" in title


def test_window_title(browser):
    logging.info("Get window title")
    title = browser.title.lower()
    assert "налоговый кодекс" in title
    assert "часть вторая" in title
