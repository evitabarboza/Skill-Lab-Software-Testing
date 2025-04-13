import pytest
from selenium import webdriver
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_02_Fill_Text(browser):
    browser.get("http://qxf2.com/selenium-tutorial-main")

    assert browser.title == "Qxf2 Services: Selenium training main", "Page title mismatch"

    # Fill name field using xpath with id
    name = browser.find_element("xpath", "//input[@id='name']")
    name.send_keys('Avinash')

    # Fill email field using xpath without id
    email = browser.find_element("xpath", "//input[@name='email']")
    email.send_keys('avinash@qxf2.com')

    # Fill phone no field using ID
    phone = browser.find_element("id", "phone")
    phone.send_keys('9999999999')

    # Pause for visibility
    time.sleep(2)

    # Assert fields are filled correctly
    assert name.get_attribute('value') == 'Avinash'
    assert email.get_attribute('value') == 'avinash@qxf2.com'
    assert phone.get_attribute('value') == '9999999999'
