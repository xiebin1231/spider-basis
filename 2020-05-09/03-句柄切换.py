import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

time.sleep(1)
driver.find_element_by_id('kw').send_keys('python')
time.sleep(1)
driver.find_element_by_id('su').click()
time.sleep(1)

# 通过执行js来新开一个标签页
js = 'window.open("https://www.sogou.com");'
driver.execute_script(js)
time.sleep(1)

# 1. 获取当前所有的窗口
windows = driver.window_handles

time.sleep(2)
# 2. 根据窗口索引进行切换
driver.switch_to.window(windows[0])
time.sleep(2)
driver.switch_to.window(windows[1])

time.sleep(6)
driver.quit()