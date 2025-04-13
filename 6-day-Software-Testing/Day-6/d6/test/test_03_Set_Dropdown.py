import pytest
import time
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_03_Set_Dropdown(browser):
    browser.get("http://qxf2.com/selenium-tutorial-main")

    # Click the dropdown to reveal options
    dropdown_button = browser.find_element("xpath", "//button[@data-toggle='dropdown']")
    dropdown_button.click()
    time.sleep(1)  # Optional pause for visibility

    # Click the "Male" option
    male_option = browser.find_element("xpath", "//a[text()='Male']")
    male_option.click()

    # Optional wait to observe change
    time.sleep(2)

    # Verify if dropdown has selected "Male"
    # Let's assume the selected item is shown in the dropdown button itself (you can adjust based on the actual behavior)
    selected_value = dropdown_button.text.strip()  # or any other element that shows the selected value
    assert selected_value == "Male", f"Dropdown selection failed. Expected 'Male', but got '{selected_value}'"
