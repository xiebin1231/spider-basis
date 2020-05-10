import time
from selenium import webdriver
from scroll_bottom import scroll_to_bottom
driver = webdriver.Chrome()
driver.get("https://www.mogu.com/")
time.sleep(1)
scroll_to_bottom(driver)
