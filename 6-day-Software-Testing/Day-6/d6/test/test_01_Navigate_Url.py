import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()  # Ensures the browser closes after test execution

def test_01_Navigate_Url(browser):
    browser.get("http://qxf2.com/selenium-tutorial-main")
    
    print("Navigated to:", browser.current_url)  # Will be printed during pytest execution

    expected_title = "Qxf2 Services: Selenium training main"
    assert browser.title == expected_title, f"Failed: Expected '{expected_title}', but got '{browser.title}'"

    print("Success: Qxf2 Tutorial page launched successfully")  # Print output after assertion
