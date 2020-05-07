# _*_coding:utf-8 _*_
import requests
import fake_useragent
ua = fake_useragent.UserAgent()


url = 'https://www.baidu.com'

headers = {"User-Agent": ua.random}

# 在请求头中带上User-Agent，模拟浏览器发送请求
response = requests.get(url, headers=headers)

with open('baidu.html','w') as F:
    F.write(response.content.decode())

# 打印请求头信息
print(response.request.headers)
