import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Checkout:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.checking=(By.XPATH,"//button[@id='checkout']")
        self.name=(By.XPATH,"//input[@id='first-name']")
        self.title=(By.XPATH,"//input[@id='last-name']")
        self.zip=(By.XPATH,"//input[@id='postal-code']")
        self.submit=(By.XPATH,"//input[@id='continue']")
        self.scroll=(By.XPATH,"//button[@class='btn btn_action btn_medium cart_button']")

    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.checking)).click()
        time.sleep(1)

    def name_input(self):
        firstname = self.driver.find_element(*self.name)
        firstname.send_keys("Sriparna")
        time.sleep(1)
    def surname_input(self):
        lastname = self.driver.find_element(*self.title)
        lastname.send_keys("Chatterjee")
        time.sleep(1)
    def code(self):
        postalcode= self.driver.find_element(*self.zip)
        postalcode.send_keys("700034")
        time.sleep(1)
    def continueclick(self):
        self.wait.until(EC.element_to_be_clickable(self.submit)).click()
        time.sleep(1)
    def click_finish(self):
        scrolling = self.driver.find_element(*self.scroll)
        self.driver.execute_script("arguments[0].scrollIntoView();", scrolling)
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable(self.scroll)).click()
        time.sleep(1)