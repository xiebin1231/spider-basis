# _*_coding:utf-8 _*_
import requests


url = 'https://twitter.com'
response = requests.get(url, timeout=3)     # 设置超时时间
