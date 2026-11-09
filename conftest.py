import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    options = Options()
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()