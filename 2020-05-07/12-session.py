# _*_coding:utf-8 _*_

import requests
from lxml import etree

url = 'https://github.com/login'
post_url = 'https://github.com/session'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

session = requests.Session()

# 向登录界面发起请求
response = session.get(url, headers=headers)
html = etree.HTML(response.content.decode())

# 构造请求数据

authenticity_token = html.xpath('//input[@name="authenticity_token"]/@value')
ga_id = html.xpath('//meta[@name="octolytics-dimension-ga_id"]/@content')
timestamp = html.xpath('//input[@name="timestamp"]/@value')
timestamp_secret = html.xpath('//input[@name="timestamp_secret"]/@value')
password = ''
data = {
    'ga_id': ga_id,
    'authenticity_token': authenticity_token,
    'timestamp': timestamp,
    'timestamp_secret': timestamp_secret,
    'login': '1120448506@qq.com',
    'password': 'b20170227y'
}
response = session.post(post_url, headers=headers, data=data)
response = session.get('https://github.com/')
with open('session.html', 'wb') as F:
    F.write(response.content)
# response = requests.get('https://github.com/')
# with open('request.html', 'wb') as F:
#     F.write(response.content)
