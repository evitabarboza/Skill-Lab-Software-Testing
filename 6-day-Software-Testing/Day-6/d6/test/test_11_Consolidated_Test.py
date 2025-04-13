import time
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Or Firefox, Edge, etc.
    driver.maximize_window()
    yield driver
    driver.quit()

def test_11_Consolidated_Test(browser):
    driver = browser
    driver.get("http://qxf2.com/selenium-tutorial-main")

    # Step 3: Print the contents of the table
    table = driver.find_element("xpath", "//table[@name='Example Table']")
    rows = table.find_elements("xpath", "//tbody/descendant::tr")
    result_data = []
    for row in rows:
        cols = row.find_elements("tag name", "td")
        cols_data = [col.text.encode('utf-8') for col in cols]
        result_data.append(cols_data)
    print(result_data)  # Optional: for debugging/logging

    # Step 4: Fill all the text fields
    driver.find_element("xpath", "//input[@id='name']").send_keys('Avinash')
    driver.find_element("xpath", "//input[@name='email']").send_keys('avinash@qxf2.com')
    driver.find_element("id", "phone").send_keys('9999999999')

    # Step 5: Select Dropdown option
    driver.find_element("xpath", "//button[@data-toggle='dropdown']").click()
    time.sleep(1)
    driver.find_element("xpath", "//a[text()='Male']").click()

    # Step 6: Enable the checkbox
    checkbox = driver.find_element("xpath", "//input[@type='checkbox']")
    checkbox.click()

    # Step 7: Take a screenshot
    driver.save_screenshot('Qxf2_Tutorial.png')

    # Step 8: Click on Submit button
    driver.find_element("xpath", "//button[text()='Click me!']").click()

    # Step 9: Verify redirection URL
    time.sleep(3)
    assert driver.current_url == 'https://qxf2.com/selenium-tutorial-redirect', "Redirection failed"
