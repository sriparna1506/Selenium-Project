import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class NegloginPg:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_input= (By.XPATH,"//input[@id='username']")
        self.password_input=(By.XPATH,"//input[@id='password']")
        self.login_click=(By.XPATH,"//button[@type='submit']")
        self.failed=(By.XPATH,"//div[@id='flash']")

    def neg_username(self,text):
        username= self.driver.find_element(*self.username_input)
        username.send_keys(text)
        time.sleep(2)
    def neg_password(self,password):
        enter_password=self.driver.find_element(*self.password_input)
        enter_password.send_keys(password)
        time.sleep(2)

    def neg_click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_click)).click()
        time.sleep(2)
        failed_message = self.driver.find_element(*self.failed).text
        assert "Your username is invalid!" in failed_message
        time.sleep(5)