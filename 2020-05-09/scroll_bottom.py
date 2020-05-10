import time
def scroll_to_bottom(driver):
	js = "return action=document.body.scrollHeight"
	# 初始化现在滚动条所在高度为0
	height = 0
	# 当前窗口总高度
	new_height = driver.execute_script(js)

	while height < new_height:
		# 将滚动条调整至页面底部
		for i in range(height, new_height, 100):
			driver.execute_script('window.scrollTo(0, {})'.format(i))
			time.sleep(0.5)
		height = new_height
		time.sleep(2)
		new_height = driver.execute_script(js)
