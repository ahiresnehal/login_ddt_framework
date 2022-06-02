from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path="/home/snehal/Downloads/chromedriver_linux64/chromedriver")
    return driver
