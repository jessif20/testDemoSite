from selenium.webdriver.common.by import By


class RegisterPageLocators:

    USER_NAME_TEXT_BOX = (By.ID, "email")
    PASSWORD_TEXT_BOX = (By.NAME, "password")
    CONFIRM_PASSWORD_TEXT_BOX = (By.NAME, "confirmPassword")
    SUBMIT_BUTTON = (By.NAME, "submit")

import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def username_password():
    user_name = "dan25"
    password = "dan123"
    return [user_name, password]


@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()


from pages.base_page import BasePage
from pages.register_page_locators import RegisterPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class RegisterPage(BasePage):

    def wait_and_type_user_name(self, usr_and_pw):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, RegisterPageLocators.USER_NAME_TEXT_BOX).send_keys(
            usr_and_pw[0])

    def type_password(self, usr_and_pw):
        self.find_element(RegisterPageLocators.PASSWORD_TEXT_BOX).send_keys(
            usr_and_pw[1])

    def type_confirm_password(self, usr_and_pw):
        self.find_element(RegisterPageLocators.CONFIRM_PASSWORD_TEXT_BOX).send_keys(
            usr_and_pw[1])

    def click_submit_btn(self):
        self.find_element(RegisterPageLocators.SUBMIT_BUTTON).click()