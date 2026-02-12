import time

from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Logging:
    def __init__(self,driver):
        self.driver = driver
        self.wait= WebDriverWait(driver,10)
        self.username=(By.XPATH,"//input[@id='user-name']")
        self.password=(By.XPATH,"//input[@id='password']")
        self.login=(By.XPATH,"//input[@id='login-button']")


    def SwagLabsusername(self,textinp):
        username_inp= self.driver.find_element(*self.username)
        username_inp.send_keys(textinp)
        time.sleep(2)
    def SwagLabpassword(self,passwordinp):
        password_inp=self.driver.find_element(*self.password)
        password_inp.send_keys(passwordinp)
        time.sleep(2)
    def Swag_lab_click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login)).click()
        time.sleep(2)
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html","Homepage not loaded successfully"
        # alert = self.driver.switch_to.alert
        # alert.accept()
        time.sleep(4)
        # self.driver.refresh()




        # try:
        #     alert = self.driver.switch_to.alert
        #     print("Alert text:", alert.text)
        #     alert.accept()
        # except NoAlertPresentException:
        #     print("No alert present")
