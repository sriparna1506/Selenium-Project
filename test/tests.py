from Homepage.products import Product
from Homepage.productsorting import Sorting
from Logged_In.loggin_in import Logging
from Logged_In.neg_logged_in import NegLogging
from LoginPage.login import LoginPg
from LoginPage.neg_logintest import NegloginPg

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
    loginpage = Logging(seconddriver)
    loginpage.SwagLabsusername("standard_user")
    loginpage.SwagLabpassword("secret_sauce")
    loginpage.Swag_lab_click_login()
    prod = Product(seconddriver)
    prod.product_select()
    sort = Sorting(seconddriver)
    sort.prod_sort()
def test_negswaglablogin(seconddriver):
    negloginpage = NegLogging(seconddriver)
    negloginpage.neg_SwagLabsusername("swag_standard_user")
    negloginpage.neg_SwagLabpassword("standard_secret_sauce")
    negloginpage.neg_Swag_lab_click_login()



