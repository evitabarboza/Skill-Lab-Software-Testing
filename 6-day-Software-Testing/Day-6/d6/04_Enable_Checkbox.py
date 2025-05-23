"""
Learn to select a checkbox using Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com

SCOPE:
1) Launch Firefox Driver
2) Navigate to Qxf2 Tutorial page
3) Find the Checkbox element in the Example form and enable it
4) Close the browser
"""
import time
from selenium import webdriver

# Create an instance of Firefox WebDriver
driver = webdriver.Chrome()
# Maximize the browser window
driver.maximize_window()
driver.get("http://qxf2.com/selenium-tutorial-main")

# KEY POINT: Locate the checkbox and click on it
checkbox = driver.find_element("xpath", "//input[@type='checkbox']")
checkbox.click()

# Pause the script for 3 sec so you can confirm the check box was selected
time.sleep(3)

# Close the browser window
driver.close()


