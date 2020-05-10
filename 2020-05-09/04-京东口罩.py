from selenium import webdriver
import time

driver = webdriver.Chrome()
url = 'https://search.jd.com/Search?keyword=%E5%8F%A3%E7%BD%A9&enc=utf-8&wq=%E5%8F%A3%E7%BD%A9&pvid=4c2bf769ed4347388c85da1cb56860f2'
driver.get(url)
driver.maximize_window()

kou_zhaos = driver.find_elements_by_xpath('//ul[@class="gl-warp clearfix"]/li/div/div[1]/a')

i = 0
while i <3:
    kou_zhao = kou_zhaos[i]
    kou_zhao.click()
    # 所有句柄列表
    windows = driver.window_handles
    # 切换句柄到第二个
    driver.switch_to.window(windows[1])
    time.sleep(4)
    driver.close()
    # 切回第一个句柄
    driver.switch_to.window(windows[0])
    time.sleep(1)
    i += 1

driver.quit()