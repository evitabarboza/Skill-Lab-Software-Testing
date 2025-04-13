import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_08_Hover(browser):
    driver = browser
    driver.get("http://qxf2.com/selenium-tutorial-main")

    # Click on the menu icon
    menu = driver.find_element("xpath", "//img[@src='./assets/img/menu.png']")
    menu.click()

    # Hover over the "Resources" link
    resource = driver.find_element("xpath", "//a[text()='Resources']")
    action = ActionChains(driver)
    action.move_to_element(resource).perform()
    time.sleep(2)  # Visual delay

    # Click on "GUI automation" link
