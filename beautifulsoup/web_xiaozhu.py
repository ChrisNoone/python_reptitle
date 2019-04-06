# coding: utf-8

from bs4 import BeautifulSoup
from urllib import request, error
import time
import random


def build_proxy_opener():
    proxy_list = ['68.107.176.152:80', '203.144.174.111:8080']
    item = random.randint(0, len(proxy_list)-1)
    proxy = {'proxy': proxy_list[item]}
    proxy_handler = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_handler)
    request.install_opener(opener)


def get_url(page_url):
    data = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    build_proxy_opener()

    try:
        req = request.Request(page_url, headers=headers)
        web_data = request.urlopen(req).read().decode()
        time.sleep(2)
        Soup = BeautifulSoup(web_data, 'lxml')
        details = Soup.select('#page_list > ul > li > a')
    except (error.HTTPError, error.URLError) as e:
        print(e)

    for detail in details:
        info = {
            'detail': detail.get('href')
        }
        data.append(info)
    return data


def get_data(page_url):
    print(page_url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    build_proxy_opener()

    try:
        req = request.Request(page_url, headers=headers)
        web_data = request.urlopen(req).read().decode()
        time.sleep(2)
        Soup = BeautifulSoup(web_data, 'lxml')
        titles = Soup.select('div.con_l > div.pho_info > h4 > em')
        addrs = Soup.select('div.con_l > div.pho_info > p > span')
    except (error.HTTPError, error.URLError) as e:
        print(e)

    for title, addr in zip(titles, addrs):
        info = {
            'title': title.get_text(),
            'addr': addr.get_text()
        }
        home.append(info)


if __name__ == '__main__':
    home = []
    for i in range(1, 3):
        url = 'http://bj.xiaozhu.com/search-duanzufang-p' + str(i) + '-0/'
        print(url)
        pages = get_url(url)
        for j in pages:
            get_data(j['detail'])

    for em in home:
        print('Title：', em['title'], 'Addr：', em['addr'])
