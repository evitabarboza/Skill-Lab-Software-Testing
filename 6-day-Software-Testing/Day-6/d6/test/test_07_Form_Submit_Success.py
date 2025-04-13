import pytest
import time
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_07_Form_Submit_Success(browser):
    driver = browser
    driver.get("http://qxf2.com/selenium-tutorial-main")

    # Fill in the form
    driver.find_element("xpath", "//input[@id='name']").send_keys("Avinash")
    driver.find_element("xpath", "//input[@name='email']").send_keys("avinash@qxf2.com")
    driver.find_element("id", "phone").send_keys("9999999999")

    # Click the "Click me!" button
    driver.find_element("xpath", "//button[text()='Click me!']").click()
