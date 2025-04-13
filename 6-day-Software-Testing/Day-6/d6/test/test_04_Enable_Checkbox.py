import pytest
import time
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_04_Enable_Checkbox(browser):
    browser.get("http://qxf2.com/selenium-tutorial-main")

    # Locate the checkbox and click on it
    checkbox = browser.find_element("xpath", "//input[@type='checkbox']")
    checkbox.click()
    
    time.sleep(2)  # Optional wait to observe change
    
    # Verify that checkbox is selected
    assert checkbox.is_selected(), "Checkbox was not selected after clicking"
