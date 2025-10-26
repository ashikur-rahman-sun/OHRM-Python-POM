from pages.login_page import LoginPage

def test_invalid_login(setup):
    driver = setup
    login_page = LoginPage(driver)

    login_page.login("InvalidUser", "wrongpass")

    error_text = login_page.get_error_message()
    assert "Invalid credentials" in error_text, "No error message shown for invalid login!"
