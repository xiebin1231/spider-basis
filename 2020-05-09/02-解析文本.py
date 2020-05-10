import time
from selenium import webdriver


driver = webdriver.Chrome()

# 控制浏览器访问url地址
driver.get("https://www.taobao.com/")

button = driver.find_element_by_xpath('//div[@class="search-button"]/button')
print(button.text)
print(button.get_attribute('class'))

time.sleep(6)
# 退出浏览器
driver.quit()