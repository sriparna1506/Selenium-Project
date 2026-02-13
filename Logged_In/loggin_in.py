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
#         # alert = self.driver.switch_to.alert
#         # alert.accept()
        time.sleep(4)
        # self.driver.refresh()
#
#
#
#
#         # try:
#         #     alert = self.driver.switch_to.alert
#         #     print("Alert text:", alert.text)
#         #     alert.accept()
#         # except NoAlertPresentException:
#         #     print("No alert present")



# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#         # Heroku
#         self.heroku_username = (By.ID, "username")
#         self.heroku_password = (By.ID, "password")
#         self.heroku_button = (By.CSS_SELECTOR, "button[type='submit']")
#         self.heroku_flash = (By.ID, "flash")
#
#         # SwagLabs
#         self.swag_username = (By.ID, "user-name")
#         self.swag_password = (By.ID, "password")
#         self.swag_button = (By.ID, "login-button")
#
#     def heroku_login(self, username, password):
#         self.wait.until(EC.visibility_of_element_located(self.heroku_username)).send_keys(username)
#         self.driver.find_element(*self.heroku_password).send_keys(password)
#         self.driver.find_element(*self.heroku_button).click()
#
#         message = self.wait.until(
#             EC.visibility_of_element_located(self.heroku_flash)
#         ).text
#
#         return message
#
#     def swaglabs_login(self, username, password):
#         self.wait.until(EC.visibility_of_element_located(self.swag_username)).send_keys(username)
#         self.driver.find_element(*self.swag_password).send_keys(password)
#         self.driver.find_element(*self.swag_button).click()
#
#         self.wait.until(EC.url_contains("inventory"))

# pages/login_page.py

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class HerokuLoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#         self.username = (By.ID, "username")
#         self.password = (By.ID, "password")
#         self.login_btn = (By.CSS_SELECTOR, "button[type='submit']")
#         self.flash = (By.ID, "flash")
#
#     def login(self, user, pwd):
#         self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(user)
#         self.driver.find_element(*self.password).send_keys(pwd)
#         self.driver.find_element(*self.login_btn).click()
#
#     def get_message(self):
#         return self.wait.until(
#             EC.visibility_of_element_located(self.flash)
#         ).text
#
#
# class SwagLoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#         self.username = (By.ID, "user-name")
#         self.password = (By.ID, "password")
#         self.login_btn = (By.ID, "login-button")
#
#     def swaglabs_login(self, user, pwd):
#         self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(user)
#         self.driver.find_element(*self.password).send_keys(pwd)
#         self.driver.find_element(*self.login_btn).click()
