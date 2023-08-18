from selenium.webdriver.common.by import By


class RegisterPageLocators:

    USER_NAME_TEXT_BOX = (By.ID, "email")
    PASSWORD_TEXT_BOX = (By.NAME, "password")
    CONFIRM_PASSWORD_TEXT_BOX = (By.NAME)
    SUBMIT_BUTTON = (By.NAME, "submit")