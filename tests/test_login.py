# import pytest
# from selenium import webdriver
# from selenium.webdriver.support.ui import
#
# from page Objects.LoginPage import LoginPage
# path ="C:\\Drivers\\chromedriver-win64\\chromedriver.exe"
# class TestClass:
#     baseUrl = "https://admin-demo.nopcommerce.com/"
#     admin_username = "admin@yourstore.com"
#     admin_password= "admin"
#
#     def test_homePageTitle(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get(self.baseUrl)
#         print(self.baseUrl,"Url shows")
#         actual_title = self.driver.title
#         self.driver.close()
#         if actual_title == "Your store. Login":
#             print(actual_title,"Actual Title is matched")
#             assert True
#         else:
#             print(actual_title,"Actual Title is not matched")
#             assert False
import time
import pytest
from config.config import BASE_URL, ADMIN_EMAIL, ADMIN_PASSWORD
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.visit(BASE_URL)
    login_page.login(ADMIN_EMAIL, ADMIN_PASSWORD)
    time.sleep(5)
    assert dashboard_page.is_dashboard_displayed

    login_page.logout()
