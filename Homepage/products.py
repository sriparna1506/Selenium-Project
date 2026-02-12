import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Product:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.item=(By.XPATH,"//div[@class='inventory_item']")
        self.name=(By.XPATH,".//div[@class='inventory_item_name ']")

    def product_select(self):
        products = self.driver.find_elements(*self.item)
        item_count = len(products)
        print("Total products are:", item_count)
        for i in range(item_count):
            item_name = products[i].find_element(*self.name).text
            print(item_name)

            time.sleep(5)

