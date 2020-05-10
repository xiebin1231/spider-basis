import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

# 在百度搜索框中搜索'python'
driver.find_element_by_id('kw').send_keys('python')
# 点击'百度搜索'
driver.find_element_by_id('su').click()

time.sleep(6)
# 退出浏览器
driver.quit()