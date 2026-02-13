# from Homepage.products import Product
# from Logged_In.loggin_in import HerokuLoginPage, Logging
# from Logged_In.loggin_in import SwagLoginPage
from Homepage.productsorting import ProductPage
from Homepage.products import Product
from Logged_In.loggin_in import Logging

# from Homepage.productsorting import ProductPage
# from Logged_In.loggin_in import Logging
from Logged_In.neg_logged_in import NegLogging
from LoginPage.login import LoginPg
from LoginPage.neg_logintest import NegloginPg
from checkout.checkingout import Checkout
from logout.loggingout import Logouts
from utilities.read_json import read_json


def test_loginPortion(driver):
    logged_in = LoginPg(driver)
    logged_in.username("tomsmith")
    logged_in.password("SuperSecretPassword!")
    logged_in.click_login()
def test_negtestcase(driver):
    negative_test = NegloginPg(driver)
    negative_test.neg_username("TomSmith")
    negative_test.neg_password("SuperSecret!")
    negative_test.neg_click_login()
def test_swaglablogin(seconddriver):
    data = read_json("credentials.json")
    username = data["login"]["username"]
    password = data["login"]["password"]
    loginpage = Logging(seconddriver)
    loginpage.SwagLabsusername(username)
    loginpage.SwagLabpassword(password)
    loginpage.Swag_lab_click_login()
    prod = Product(seconddriver)
    prod.product_select()
    prod_pg = ProductPage(seconddriver)
    prod_pg.sort_products("Price (low to high)")
    actual_prices = prod_pg.get_all_prices()
    expected_prices = sorted(actual_prices)
    print(f"UI Prices: {actual_prices}")
    assert actual_prices == expected_prices, f"Sort failed! Expected {expected_prices} but got {actual_prices}"
    prod_pg.add_to_cart(2)
    prod_pg.cart()
    check =Checkout(seconddriver)
    check.click_checkout()
    check.name_input()
    check.surname_input()
    check.code()
    check.continueclick()
    check.click_finish()
    submit=Logouts(seconddriver)
    submit.click_back_to_home()
    submit.click_menu()
    submit.click_logout()
def test_negswaglablogin(seconddriver):
    negloginpage = NegLogging(seconddriver)
    negloginpage.neg_SwagLabsusername("swag_standard_user")
    negloginpage.neg_SwagLabpassword("standard_secret_sauce")
    negloginpage.neg_Swag_lab_click_login()



