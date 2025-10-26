from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_logout(setup):
    driver = setup
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    # Login first
    login_page.login("Admin", "admin123")
    assert dashboard_page.is_dashboard_displayed(), "Login failed!"

    # Perform logout
    dashboard_page.logout()

    # Verify redirected to login page
    assert "login" in driver.current_url.lower(), "Logout failed — still on dashboard!"
