# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 10:56:06 2020

@author: loginov_d
"""

import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://stepik.org/lesson/25969/step/8")



def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
        #browser = webdriver.Firefox(firefox_binary=binary)
        browser =  webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()