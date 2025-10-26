from selenium.webdriver.common.by import By

class LoginPage:
    """Page Object for OrangeHRM Login Page"""

    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.error_message = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")

    def enter_username(self, username):
        element = self.driver.find_element(*self.username_field)
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        element = self.driver.find_element(*self.password_field)
        element.clear()
        element.send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        """Performs full login sequence"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
