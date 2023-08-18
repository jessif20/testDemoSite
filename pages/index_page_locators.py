from selenium.webdriver.common.by import By


class IndexPageLocators:

    REGISTER_LINK = (By.XPATH, "//a[text()='REGISTER']")
    OK_BUTTON = (By.NAME, "btn_ok")