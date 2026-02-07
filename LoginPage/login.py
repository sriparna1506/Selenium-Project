import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class LoginPg:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_input= (By.XPATH,"//input[@id='username']")
        self.password_input=(By.XPATH,"//input[@id='password']")
        self.login_click=(By.XPATH,"//button[@type='submit']")
        self.success=(By.XPATH,"//div[@id='flash']")

    def username(self,text):
        username= self.driver.find_element(*self.username_input)
        username.send_keys(text)
        time.sleep(2)
    def password(self,password):
        enter_password=self.driver.find_element(*self.password_input)
        enter_password.send_keys(password)
        time.sleep(2)
    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_click)).click()
        time.sleep(2)
        success_message = self.driver.find_element(*self.success).text
        assert "You logged into a secure area!" in success_message,"Your username is invalid!"