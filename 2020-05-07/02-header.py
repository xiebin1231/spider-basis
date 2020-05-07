# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 9:20
# @Author  : Shark
# @Explain :
# @Software: PyCharm

import requests

url = 'https://www.baidu.com'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# 在请求头中带上User-Agent，模拟浏览器发送请求
response = requests.get(url, headers=headers)

print(response.content)

# 打印请求头信息
print(response.request.headers)
