import pytest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_06_Form_Validation(browser):
    driver = browser
    driver.get("http://qxf2.com/selenium-tutorial-main")

    # Click the "Click me!" button without entering data
    driver.find_element("xpath", "//button[text()='Click me!']").click()
    time.sleep(3)  # Allow time for validation message to appear

    # Check for the validation message
    try:
        validation = driver.find_element("xpath", "//label[text()='Please enter your name']")
        assert validation.is_displayed(), "Validation label found but not visible"
    except NoSuchElementException:
        pytest.fail("Validation message for 'name' field is NOT present")
