from selenium import webdriver
import time
options = webdriver.ChromeOptions() # 创建一个配置对象
options.add_argument('--user-agent=Mozilla/5.0 HAHA') # 替换User-Agent

driver = webdriver.Chrome(chrome_options=options)

driver.get('http://www.baidu.com')
print(driver.title)
time.sleep(15)
# driver.quit()