"""
It uses Selenium WebDriver for browser interactions:
https://www.seleniumhq.org/projects/webdriver/
Setup and cleanup are handled using hooks.
Prerequisites:
 - Slimjet portable must be installed.
 - Chromedriver must be installed.
"""
import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

SLIM_JET_INSTALLATION_PATH="d:/Internet/Slimjet/slimjet.exe"
CHROME_DRIVER_INSTALLATION_PATH = "d:/Programacion/Selenium/ChromeDriver/74.0.3729.6/chromedriver.exe"

scenarios('../features/web.feature')


@pytest.fixture
def browser():
    options = Options()
    options.binary_location = SLIM_JET_INSTALLATION_PATH
    driver = webdriver.Chrome(chrome_options=options,
                              executable_path=CHROME_DRIVER_INSTALLATION_PATH, )
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@given("the DuckDuckGo home page is displayed")
def ddg_home(browser):
    duckduckgo_url = 'https://duckduckgo.com/'
    browser.get(duckduckgo_url)


@when(parsers.cfparse('the user searches for {text}'))
@when(parsers.parse('the user searches for the phrase: {text}'))
def search_phrase(browser, text):
    search_input = browser.find_element_by_name('q')
    search_input.send_keys(text + Keys.RETURN)


@then(parsers.cfparse('results are shown for {text}'))
def results_have_one(browser, text):
    xpath = '//*[@id="links_wrapper"]/div[2]/div[1]/div[1]/div[1]/div/div[1]/span'
    results = browser.find_elements_by_xpath(xpath)
    assert len(results) > 0


@then('one of the results contains "One"')
def search_results(browser):
    xpath = '//*[@id="links_wrapper"]/div[2]/div[1]/div/div[1]/div/div[1]/span'
    results = browser.find_elements_by_xpath(xpath)
    assert len(results) > 0
