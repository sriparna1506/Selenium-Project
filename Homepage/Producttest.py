import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ==========================================
# PAGE OBJECT CLASSES
# ==========================================

class LoginPg:
    """Handles The Internet (Heroku) Login"""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.u_input = (By.ID, "username")
        self.p_input = (By.ID, "password")
        self.btn = (By.CSS_SELECTOR, "button[type='submit']")
        self.flash = (By.ID, "flash")

    def login(self, user, pwd):
        self.wait.until(EC.visibility_of_element_located(self.u_input)).send_keys(user)
        self.driver.find_element(*self.p_input).send_keys(pwd)
        self.driver.find_element(*self.btn).click()
        msg = self.wait.until(EC.visibility_of_element_located(self.flash)).text
        assert "You logged into a secure area!" in msg

class SwagLogging:
    """Handles SwagLabs (SauceDemo) Login"""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.u_name = (By.ID, "user-name")
        self.p_word = (By.ID, "password")
        self.l_btn = (By.ID, "login-button")

    def login(self, user, pwd):
        self.wait.until(EC.visibility_of_element_located(self.u_name)).send_keys(user)
        self.driver.find_element(*self.p_word).send_keys(pwd)
        self.driver.find_element(*self.l_btn).click()
        assert "inventory" in self.driver.current_url

class ProductPage:
    """Handles Product extraction and Sorting verification"""
    def __init__(self, driver):
        self.driver = driver
        self.items = (By.XPATH, "//div[@class='inventory_item']")
        self.name = (By.XPATH, ".//div[@class='inventory_item_name']")
        self.price = (By.XPATH, ".//div[@class='inventory_item_price']")
        self.sort_drop = (By.CLASS_NAME, "product_sort_container")

    def sort_products(self, visible_text):
        select = Select(self.driver.find_element(*self.sort_drop))
        select.select_by_visible_text(visible_text)

    def get_all_prices(self):
        # 1. Re-find the list of product containers to ensure they aren't 'Stale'
        elements = self.driver.find_elements(*self.items)

        # 2. Initialize an empty list to store our final numbers
        price_list = []

        # 3. Loop through each product element found
        for p in elements:
            # Step A: Find the price element inside this specific product
            price_element = p.find_element(*self.price)

            # Step B: Get the raw text (e.g., "$7.99")
            raw_text = price_element.text

            # Step C: Remove the currency symbol
            clean_text = raw_text.replace('$', '')

            # Step D: Convert the string "7.99" to a decimal number (float)
            numeric_price = float(clean_text)

            # Step E: Add the final number to our list
            price_list.append(numeric_price)

        # 4. Return the complete list of numbers
        return price_list

# ==========================================
# E2E TEST EXECUTION
# ==========================================

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Uncomment to run without opening browser
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_heroku_login_e2e(driver):
    """Scenario 1: Heroku App Positive Login"""
    driver.get("https://the-internet.herokuapp.com/login")
    login_pg = LoginPg(driver)
    login_pg.login("tomsmith", "SuperSecretPassword!")

def test_swaglabs_sorting_e2e(driver):
    """Scenario 2: SwagLabs Login and Price Sort Verification"""
    driver.get("https://www.saucedemo.com/")

    # 1. Login
    swag = SwagLogging(driver)
    swag.login("standard_user", "secret_sauce")

    # 2. Sort by Price
    prod_pg = ProductPage(driver)
    prod_pg.sort_products("Price (low to high)")

    # 3. Verify Sort Order
    actual_prices = prod_pg.get_all_prices()
    expected_prices = sorted(actual_prices)

    print(f"UI Prices: {actual_prices}")
    assert actual_prices == expected_prices, f"Sort failed! Expected {expected_prices} but got {actual_prices}"

if __name__ == "__main__":
    # This allows running the file directly via 'python filename.py'
    pytest.main([__file__, "-v", "-s"])