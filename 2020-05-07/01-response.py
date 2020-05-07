# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 8:54
# @Author  : Shark
# @Explain :
# @Software: PyCharm

import requests

url = 'https://www.baidu.com/'
response = requests.get(url)

# 打印响应内容
# print(response.text)
# print(response.content.decode()) 			# 注意这里！
print(response.url)							# 打印响应的url
print(response.status_code)					# 打印响应的状态码
print(response.request.headers)				# 打印响应对象的请求头
print(response.headers)						# 打印响应头
print(response.request._cookies)			# 打印请求携带的cookies
print(response.cookies)						# 打印响应中携带的cookies
