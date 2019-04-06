# coding: utf-8

import requests
from bs4 import BeautifulSoup


url = 'https://www.autohome.com.cn/news/'
web_page = requests.get(url)
web_page.encoding = 'gb2312'
soup = BeautifulSoup(web_page.text, 'lxml')

div = soup.find(name='div', attrs={'id': 'auto-channel-lazyload-article'})
lis = div.find_all(name='li')
news = []
for item in lis:
    if item.find(name='h3'):
        new = {
            'title': item.find(name='h3').text,
            'dec': item.find(name='p').text,
            'src': item.find(name='a').attrs['href'].lstrip('/'),
            'img': item.find(name='img').attrs['src'].lstrip('/')
        }
        news.append(new)

for i in news:
    print('title: ', i['title'])
    print('dec: ', i['dec'])
    print('src: ', i['src'])
    print('img: ', i['img'], '\n下载图片中...')
    file_name = './downloads/' + i['img'].split('/')[-1]
    file_d = requests.get('://'.join(['https', i['img']]))
    with open(file_name, 'wb') as fp:
        fp.write(file_d.content)
    fp.close()
    print('===============================\n')



