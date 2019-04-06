# coding: utf-8

import requests
from bs4 import BeautifulSoup


url = 'https://www.autohome.com.cn/news/'
web_page = requests.get(url)
# 汽车之家返回的文件编码格式是 gb2312，而python默认用utf-8编码，这个改一下获取到的web数据的编码格式
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
            # lstrip 命令删除链接前面的两个斜线，lstrip 表示删掉左边的字符，rstrip表示删掉后面的字符
            'src': item.find(name='a').attrs['href'].lstrip('/'),
            'img': item.find(name='img').attrs['src'].lstrip('/')
        }
        news.append(new)

for i in news:
    print('title: ', i['title'])
    print('dec: ', i['dec'])
    print('src: ', i['src'])
    print('img: ', i['img'], '\n下载图片中...')
    # 定义文件的存储路径和文件名称，./downloads 当前文件所在路径下的downloads文件下，文件名去链接的最后一个‘/’后的字符
    file_name = './downloads/' + i['img'].split('/')[-1]
    # 拼接图片文件的下载链接，用 :// 将 https 和 www.auto... 字符链接，组成“http://www.auto...”这样的链接
    file_d = requests.get('://'.join(['https', i['img']]))
    with open(file_name, 'wb') as fp:
        # 下载图片文件，用content命令
        fp.write(file_d.content)
    fp.close()
    print('===============================\n')



