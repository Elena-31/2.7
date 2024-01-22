from selenium.webdriver import Remote
import pytest


@pytest.fixture
def set_up_browser():
    driver = Remote(desired_capabilities={
        "browserName": "chrome",
        "browserVersion": "latest"
    }, conmand_executor="http://127.0.0.1:4444/wd/hub")
    yield driver
    driver.quit