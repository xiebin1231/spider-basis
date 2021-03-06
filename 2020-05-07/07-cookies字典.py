# _*_coding:utf-8 _*_

import requests

url = 'https://github.com/explore'

# 构造请求头字典
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}
# 构造cookies字典
cookies_str = '_octo=GH1.1.1095903611.1588819946; _ga=GA1.2.1884338280.1588819965; tz=Asia%2FShanghai; _device_id=3a806c9a91a623c2d5861fbda194ba80; has_recent_activity=1; user_session=fTPIToQoA1a1LxyeazBccl2JhVwJockdYfVHidJ2LLYAKL4_; __Host-user_session_same_site=fTPIToQoA1a1LxyeazBccl2JhVwJockdYfVHidJ2LLYAKL4_; logged_in=yes; dotcom_user=xiebin1231; _gat=1; _gh_sess=n08l2v7VLtK1s1qOtsGdpzS7vwgz%2BlRKokbkSWzGef42ph%2F%2F2i1OLUwilVPv0fnTKt0IqWuJNO1h6DNcA9VRskpjmh0oNZGVuNkhU9v9miNTGMT512qRJjdKKRXMc%2BQnF7JcWRDeEyvL%2Fo35DyWXJldQpzmMUQhzJ%2BbE2kFWJq8Y0V80OAbHP%2BANpFU%2FmlYfnvqP%2Bm3lGgEPliJUb7PbppnDBEWAE5kew4XEhVxOiov2saUeb5EpZxqCOW0p7IY6xpX5Qgv%2FPZ3NCxZKycjLQEfErW6cA6c9DDjMLFAXOd3IxuOdZWyyRq7HIGPWIiqct2rBtJLkrw2nfQZMCHmz8was7aLfy%2BvopVcN7Mq6Cv53SVZEl8Kjy%2FaC5ZbXRjBWyH%2BV1JHuW6R4DvERmuY2yD12NlXLfOJLRg%2FOGHHC4cHpY%2BLJps1MUdfgzzIjOT%2FdqLNTlLFUyckD6K%2Bka2EXDC0R9JjUsAArYqTnX9M2offWtLrWhkuqf6bZQbwmqrHSWUWwDFtQGc1Yh27jhyj5CpF94H4UJYu9bmu1ZxDwzUZWymGYYNeAdOJYGvCe6G8cQE8QZWwbEMzn32hz%2BAW5zpFg68gF5ixKPi2f2Yb0b5StsbVXygorK%2BfMaWyf6esuqQxNY0mxTgx6mHFfwjwyPQ9%2FOSC7Zf%2Fn2giGRyjgfWvsc8eFS6qnDQqSqkEaUrp%2FpTGG6fFl%2FzRXYUQT895sErc9uvC7hJCt1esMBDMAW6iiLnrXiy%2BD93RVQVbSCIPvHghuIteNV6Os%2FgvSos57GZONwUk6%2FexjV4mOH8hrd1uNoeNnj0TFlqptwifYqhqzTK4SKZU8JJWg%2Bn5RUGQwwMSaq5TS%2Fl6%2BlYQbrmtZJP4bsPW8%2BLYXoTtPxLivzQy60X7RnT9sO7eD25ASGKiugdbPymB%2B1%2BhcJglAiD3dYBor3J%2BEaOJY9AJwvpnG4IPqY1s5HDV2Z6ZtHDi2v5Y%2F2wPjLbiXo69Pfsy%2B8vGTjnBfTonxlQaA8CuirJqVk0tQycoKCVdXZ8cTfDzKNZPV2lVjelZFahc9MOJIbDj5g%2F539JgL%2BPisnHu9ifza3Oc0k%2Fnvd1Rh3YFx529u6dT%2BiU7GlHUVjCmJvzkqCF8Dsnax%2F7mvoAdJaa%2FRW2RdXX7tFnTt2WE0bUVraF9QaiV%2Bs1CUAveLnFyvRQn75QU0ia2pS%2BsqQXj64KUWsP08jaUKflLB%2Baxp1xJkd0WJttdgHPnqrx9KbuRTbFeWyQkwTOlqiVZFNsjYNKUihM6yUPu7NHL3bWhSTz%2Fv5IV0l%2BKsQWnFSrkwNK8tr52UkGYt777hdIyZIsx8ni35ViFc1du%2FU%2Bn85WVVBdi%2Bk%2F3k21LtOzZdTmyGxiop2uJX8obSV3MNsbOWpifd7toBwmDY%2FhQ2Yo9oFfRAnZ3qVKR9TdMvUJJX6OWo3nFna%2FxaiflxSFA2VE7qLKNdFA8yEk37pUBjz1TkVLaF%2BbN2MJchgeDB4ar7raKRM3KkO%2FT1r0QF7aPtLaNf%2FOq1h4ewxtVllNp%2BzSlSm7d6R99q7H5%2BYBil4OIsZOfb2x6P3Aas06eRt5bBbMKXb3ClCKc2kzb1gUD%2FTaZi3VTR0YUztTxCAj0uh%2BgmNPXZdVFIWyQmP7oBoNx1%2F%2BYFX2X%2BMNh8FBDW%2FJyXkyZ713tEYiG4S1ls42seynM7qgsmji4yKv2jFgav5WOUdUhOKGZqrXghVTSe277lX7%2BjwFcqiCBCzmLm9GsAk2hW11gGdqth2n%2BbnuvF3VDGFkQY9NLyTUKK%2FRF%2BZPza3n2%2BLLuSZozh%2B5vmtpLku7%2B9eVI5humnUNEJr1BfYdbPgcrfyIs%2B88vpAl9VbnkGrQfpO8rKboB4fI0QkvQGfxY0x3Be63es1hesB9ELEy25coKnyuwV73o8iedFwLs%2FLKPxoF8u5tqFRldxJzf7WRXaKfx1quTOygdiOaEafHHdYaSbXE28fkRc6L1Cj8pZAA0qesw%2FtvyBoVLSYt3Ff4Q%2BIbEuSfefFN%2Bk9jTyCA9xIeTa--Ml7XENU7ZLwej6w5--GakFvratlb8vvFOZCL%2BgXQ%3D%3D'

cookies_dict = {cookie.split('=')[0]:cookie.split('=')[-1] for cookie in cookies_str.split('; ')}
print(cookies_dict)
# 请求头参数字典中携带cookie字符串
resp = requests.get(url, headers=headers, cookies=cookies_dict)

with open('github.html','w',encoding='utf-8') as fp:
    fp.write(resp.text)
print(resp.text)
