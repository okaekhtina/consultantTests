from _ast import Assert

from pageobject.helpers import SearchHelper


def test_search(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.enter_text('нк ч2')
    main_page.click_on_the_search_button()
    main_page.text_in_field()
    found_result = main_page.result_element()
    Assert(found_result)
