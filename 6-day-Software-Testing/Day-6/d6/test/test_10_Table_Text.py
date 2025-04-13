import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # You can use Firefox() if preferred
    driver.maximize_window()
    yield driver
    driver.quit()

def test_10_Table_Text(browser):
    driver = browser
    driver.get("http://qxf2.com/selenium-tutorial-main")

    # Find the Example table element in the page
    table = driver.find_element("xpath", "//table[@name='Example Table']")
    rows = table.find_elements("xpath", "//tbody/descendant::tr")

    result_data = []
    for row in rows:
        cols = row.find_elements("tag name", "td")
        cols_data = [col.text.encode('utf-8') for col in cols]
        result_data.append(cols_data)

    # You can add an assertion or keep print for debugging
    print("Extracted Table Data:", result_data)

    # Example assertion (optional): Ensure table has at least one row
    assert len(result_data) > 0, "Table has no data"
