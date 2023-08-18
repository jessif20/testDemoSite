from pages.base_page import BasePage
from pages.register_page_locator import RegisterPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class RegisterPage(BasePage):

    def wait_and_type_user_name(self, userNameAndPwList):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, RegisterPageLocators.USER_NAME_TEXT_BOX).send_keys(
            userNameAndPwList[0])

    def type_password(self, userNameAndPwList):
        self.find_element(RegisterPageLocators.PASSWORD_TEXT_BOX).send_keys(
            userNameAndPwList[1])

    def type_confirm_password(self, userNameAndPwList):
        self.find_element(RegisterPageLocators.CONFIRM_PASSWORD_TEXT_BOX).send_keys(
            userNameAndPwList[1])

    def click_submit_btn(self):
        self.find_element(RegisterPageLocators.SUBMIT_BUTTON).click()