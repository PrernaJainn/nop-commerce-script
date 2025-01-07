# from selenium.webdriver.common.by import By
# from pages.base_page import BasePage
#
# class DashboardPage(BasePage):
#     DASHBOARD_HEADER = (By.XPATH, "//h1[text()='Dashboard']")
#
#     def is_dashboard_displayed(self):
#         return self.is_element_displayed(self.DASHBOARD_HEADER)

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    DASHBOARD_HEADER = (By.XPATH, "//h1[contains(text(),'Dashboard')]")

    def __init__(self, driver):
        super().__init__(driver)

    def is_dashboard_displayed(self):
        try:
            dashboard_element = self.driver.find_element(By.XPATH, "//*[contains(text(),'Dashboard')]")
            return dashboard_element.is_displayed()
        except NoSuchElementException:
            return False