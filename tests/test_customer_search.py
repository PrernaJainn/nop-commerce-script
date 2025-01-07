import pytest
from config.config import BASE_URL, ADMIN_EMAIL, ADMIN_PASSWORD
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.customers_page import CustomersPage


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_search_customer_by_email(driver):
    login_page = LoginPage(driver)
    #customers_page = pages.customers_page.CustomersPage(driver)
    customers_page=CustomersPage(driver)
    login_page.visit(BASE_URL)
    login_page.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    customers_page.navigate_to_customers()
    customers_page.search_customer_by_email("victoria_victoria@nopCommerce.com")
    assert customers_page.get_first_customer_email() == "victoria_victoria@nopCommerce.com"
    assert customers_page.is_customer_found_by_email(TEST_EMAIL)
    login_page.logout()
