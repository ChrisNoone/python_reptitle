# coding: utf-8

from bs4 import BeautifulSoup
import requests

data = []
base_url = 'https://wh.fang.lianjia.com/loupan/pg'


# 传入地址，取出本页数据
def get_data(url):    
    web_data = requests.get(url)
    Soup = BeautifulSoup(web_data.text, 'lxml')
    names = Soup.select('ul.resblock-list-wrapper > li > div > div.resblock-name > a')
    pics = Soup.select('ul.resblock-list-wrapper > li > a > img')
    addrs = Soup.select('ul.resblock-list-wrapper > li > div > div.resblock-location > a')
    prices = Soup.select('ul.resblock-list-wrapper > li > div > div.resblock-price > div.main-price > span.number')
    types = Soup.select('ul.resblock-list-wrapper > li > div > div.resblock-name > span.resblock-type')
    status = Soup.select('ul.resblock-list-wrapper > li > div > div.resblock-name > span.sale-status')
    cates = Soup.select('ul.resblock-list-wrapper > li > div > div.resblock-tag')

    for name, pic, addr, price, type, statu, cate in zip(names,pics, addrs, prices, types, status, cates):
        info = {
            'name': name.get_text(),
            'pic': pic.get('src'),
            'addr': addr.get_text(),
            'price': price.get_text(),
            'type': type.get_text(),
            'statu': statu.get_text(),
            'cate': list(cate.stripped_strings)
        }
        data.append(info)


for i in range(1, 11):
    url = base_url + str(i)
    get_data(url)

for i in data:
    print(i)
