import pytest
from selenium import webdriver
@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/login")
    print(driver.title)
    print(driver.current_url)

    yield driver
    driver.quit()
@pytest.fixture
def seconddriver():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    print(driver.title)
    print(driver.current_url)
    yield driver
    driver.quit()
