from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_valid_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.login("Admin", "admin123")

    assert dashboard_page.is_dashboard_displayed(), "Login failed — Dashboard not visible!"
