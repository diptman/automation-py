import logging

import configparser
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def browser_type(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        logging.critical("# Invalid browser argument passed ", browser)
    driver.implicitly_wait(10)
    return driver
    # Similarly we can add all required browsers here.


# for running test on specific browser user needs to pass argurment as --browser="browser_name"

def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome')


config = configparser.ConfigParser()
config.read('config.ini')
app_url = config.get("APPLICATION", "url")


# return browser to setup method
@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(autouse=True, scope='function')
def connect_to_app(browser_type):
    driver = browser_type
    driver.get(app_url)
    yield connect_to_app
    driver.close()