from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(3)
    def visit(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)
        self.driver.implicitly_wait(10)
    def get_text(self, locator):
        return self.find_element(locator).text

    def is_element_displayed(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False
