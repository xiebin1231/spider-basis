import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.mogu.com/")
time.sleep(1)

js = 'window.scrollTo(0,document.body.scrollHeight)' # js语句
while True:
    driver.execute_script(js) # 执行js的方法
    time.sleep(5)

time.sleep(5)
driver.quit()