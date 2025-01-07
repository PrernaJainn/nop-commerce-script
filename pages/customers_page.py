from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CustomersPage(BasePage):
    CUSTOMERS_MENU = (By.XPATH, "//a[@href='#']//p[contains(text(),'Customers')]")
    CUSTOMERS_OPTION = (By.XPATH, "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")
    SEARCH_EMAIL_FIELD = (By.ID, "SearchEmail")
    SEARCH_BUTTON = (By.ID, "search-customers")
    RESULT_EMAIL = (By.XPATH, "//table[@id='customers-grid']//tbody/tr/td[2]")

    def navigate_to_customers(self):
        self.click(self.CUSTOMERS_MENU)
        self.click(self.CUSTOMERS_OPTION)

    def search_customer_by_email(self, email):
        self.enter_text(self.SEARCH_EMAIL_FIELD, email)
        self.click(self.SEARCH_BUTTON)

    def get_first_customer_email(self):
        return self.get_text(self.RESULT_EMAIL)
