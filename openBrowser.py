from selenium import webdriver
from selenium.webdriver.common import keys

driver=webdriver.Firefox();
driver.maximize_window()
driver.get("http://www.google.com")
driver.quit()
