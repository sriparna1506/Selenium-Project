import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Sorting:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver)
        self.dropdown_list=(By.XPATH,"product_sort_container")


    def prod_sort(self):
        dropdown = Select(self.driver.find_elements(*self.dropdown_list))
        for i in dropdown:
            if i.text == "Price (low to high)":
                i.click()
            time.sleep(5)


