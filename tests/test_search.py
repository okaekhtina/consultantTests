from pageobject.helpers import SearchHelper
import logging

logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')


def test_search(browser):
    logging.info("START")
    main_page = SearchHelper(browser)
    main_page.enter_text('нк ч2')
    main_page.click_on_the_search_button()
    main_page.text_in_field()
    found_result = main_page.result_element()
    assert found_result, 'Не выведен результат поиска'
    logging.info("SEARCH OK")


def test_open_document(browser):
    main_page = SearchHelper(browser)
    main_page.open_first_document()
    descriptors = browser.window_handles
    browser.switch_to.window(descriptors[1])
    frame = main_page.go_to_frame()
    browser.switch_to.frame(frame)
    loading_page = main_page.document_title()
    assert loading_page, 'Страница не загрузилась за 10 секунд'


def test_document_name(browser):
    main_page = SearchHelper(browser)
    title = main_page.document_title().lower()
    assert "налоговый кодекс" in title
    assert "часть вторая" in title


def test_window_title(browser):
    title = browser.title.lower()
    assert "налоговый кодекс" in title
    assert "часть вторая" in title
