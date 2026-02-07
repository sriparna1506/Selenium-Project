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

