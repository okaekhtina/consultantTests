import pytest
from selenium import webdriver

base_url = "http://base.consultant.ru/cons/"


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.get(base_url)
    yield driver
    driver.quit()
