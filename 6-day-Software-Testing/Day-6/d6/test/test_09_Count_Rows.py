import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Or Firefox if you prefer
    driver.maximize_window()
    yield driver
    driver.quit()

def test_09_Count_Rows(browser):
    driver = browser
    driver.get("http://qxf2.com/selenium-tutorial-main")

    # Find the table element
    table = driver.find_element("xpath", "//table[@name='Example Table']")

    # Find all rows within the table body
    rows = table.find_elements("xpath", "//tbody/descendant::tr")
    row_count = len(rows)

    print(f"Total No of Rows: {row_count}")

    # Assertion to make sure the table has rows (customize as needed)
    assert row_count > 0, "Table should contain at least one row"
