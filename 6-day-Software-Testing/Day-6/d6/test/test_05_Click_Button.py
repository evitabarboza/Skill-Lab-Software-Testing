import pytest
import time
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_05_Click_Button(browser):
    browser.get("http://qxf2.com/selenium-tutorial-main")
    
    # Locate the button and click on it
    button = browser.find_element("xpath", "//button[text()='Click me!']")
    button.click()
    
    # Optional: wait to observe effects
    time.sleep(3)
    
    # Assert that we’re still on the same domain (basic sanity check)
    assert "qxf2.com" in browser.current_url
