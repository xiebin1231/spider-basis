# _*_coding:utf-8 _*_

import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}


def get_one_page(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content.decode()
    return None


def parse_one_page(text):
    html = etree.HTML(text)
    # 获取10条电影信息节点
    films_infos = html.xpath('//div[@class="board-item-content"]')
    for films_info in films_infos:
        # 电影名
        name = films_info.xpath('.//p[@class="name"]/a/text()')
        name = name[0].strip() if name else None

        # 主演
        stars = films_info.xpath('.//p[@class="star"]/text()')
        stars = stars[0].strip() if stars else None

        # 上映时间
        releasetime = films_info.xpath('.//p[@class="releasetime"]/text()')
        releasetime = releasetime[0].strip() if releasetime else None

        # 评分
        score = films_info.xpath('.//p[@class="score"]/i/text()')
        score = ''.join(score)
        film_info = '\t'.join([name, stars, releasetime, score])
        yield film_info


def save_data(data):
    with open('film.txt', 'a') as F:
        F.write(data + '\n')


def main():
    url = 'https://maoyan.com/board/4?offset={}'
    for i in range(0,91,10):
        html = get_one_page(url.format(i))
        for line in parse_one_page(html):
            save_data(line)


main()
