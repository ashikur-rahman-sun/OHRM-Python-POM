from selenium.webdriver.common.by import By

class DashboardPage:
    """Page Object for OrangeHRM Dashboard Page"""

    def __init__(self, driver):
        self.driver = driver
        self.dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")
        self.profile_dropdown = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
        self.logout_button = (By.XPATH, "//a[text()='Logout']")

    def is_dashboard_displayed(self):
        return "Dashboard" in self.driver.find_element(*self.dashboard_header).text

    def logout(self):
        self.driver.find_element(*self.profile_dropdown).click()
        self.driver.find_element(*self.logout_button).click()
