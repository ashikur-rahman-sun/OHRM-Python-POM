# OHRM-Python-POM

Project Flow / Workflow

1. Setup:
  Created a virtual environment (venv) for isolation.
  Installed dependencies: selenium, pytest, webdriver-manager.
2. Page Object Model (POM):
   pages/login_page.py → handles login page actions.
   pages/dashboard_page.py → handles dashboard page actions like logout.
3. Test Cases:
   tests/test_login.py → valid login.
   tests/test_invalid_login.py → invalid login.
   tests/test_logout.py → logout functionality.
4. Utilities:
   utils/driver_setup.py → centralizes WebDriver setup with Chrome options and waits.
   conftest.py → Pytest fixture for setup/teardown of WebDriver.
5. Execution Flow:
   Tests launch Chrome, perform login/logout operations, and validate results using assertions.
