import pytest
from utils.driver_setup import get_driver

@pytest.fixture
def setup():
    """Fixture to initialize and quit the WebDriver"""
    driver = get_driver()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()
