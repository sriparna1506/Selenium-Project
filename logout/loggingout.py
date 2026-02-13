import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Logouts:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.home=(By.XPATH,"//button[@id='back-to-products']")
        self.menu=(By.XPATH,"//button[@id='react-burger-menu-btn']")
        self.out=(By.XPATH,"//a[@id='logout_sidebar_link']")


    def click_back_to_home(self):
        self.wait.until(EC.element_to_be_clickable(self.home)).click()
        time.sleep(3)
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html", "Homepage not loaded successfully"
    def click_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.menu)).click()
        time.sleep(3)
    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.out)).click()
        time.sleep(3)

