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
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


#     # options = webdriver.ChromeOptions()
#     # driver = webdriver.Chrome(options=options)
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#
#
# @pytest.fixture
# def heroku_page(seconddriver):
#     seconddriver.get("https://the-internet.herokuapp.com/login")
#     return seconddriver
#
#
# @pytest.fixture
# def swaglabs_page(seconddriver):
#     seconddriver.get("https://www.saucedemo.com/")
#     return seconddriver

# @pytest.fixture
# def seconddriver():
#     options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(options=options)
#     driver.maximize_window()
#     driver.set_page_load_timeout(30)
#
#     yield driver
#     driver.quit()