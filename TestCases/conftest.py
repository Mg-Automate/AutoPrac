from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.chrome import ChromeDriverManager

import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver
