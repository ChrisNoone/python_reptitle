# coding: utf-8

from bs4 import BeautifulSoup
import requests
import time


def get_url(page_url):
    data = []
    web_data = requests.get(page_url)
    time.sleep(2)
    Soup = BeautifulSoup(web_data.text, 'lxml')
    details = Soup.select('#page_list > ul > li > a')

    for detail in details:
        info = {
            'detail': detail.get('href')
        }
        data.append(info)
    return data


def get_data(page_url):
    web_data = requests.get(page_url)
    time.sleep(2)
    Soup = BeautifulSoup(web_data.text, 'lxml')
    titles = Soup.select('div.con_l > div.pho_info > h4 > em')
    addrs = Soup.select('div.con_l > div.pho_info > p > span')

    for title, addr in zip(titles, addrs):
        info = {
            'title': title.get_text(),
            'addr': addr.get_text()
        }
        home.append(info)


home = []
for i in range(1, 3):
    url = 'http://bj.xiaozhu.com/search-duanzufang-p' + str(i) + '-0/'
    pages = get_url(url)
    for j in pages:
        get_data(j['detail'])

for em in home:
    print('Title：', em['title'], 'Addr：', em['addr'])
