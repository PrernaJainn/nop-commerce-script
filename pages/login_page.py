# from selenium import webdriver
# import pytest
# from selenium.webdriver.common.by import By
#
# class LoginPage:
#     textbox_username_id = "Email"
#     textbox_password_id = "Password"
#     button_login = "//button[@text ='Log in']"
#
#
#     def __init__(self,driver):
#         self.driver = driver
#
#     def set_UserName(self,admin_username):
#         self.driver.find_element_by_id(self.textbox_username_id).send_keys(admin_username)
#
#     def set_Password(self,admin_password):
#         self.driver.find_element_by_id(self.textbox_password_id).send_keys(admin_password)
#
#     def click_login(self,):
#         self.driver.find_element_by_id(self.button_login).click()

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_FIELD = (By.ID, "Email")
    PASSWORD_FIELD = (By.ID, "Password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Log in']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Logout']")

    def login(self, email, password):
        self.find_element(self.EMAIL_FIELD).clear()
        self.enter_text(self.EMAIL_FIELD, email)
        self.find_element(self.PASSWORD_FIELD).clear()
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def logout(self):
        self.click(self.LOGOUT_BUTTON)