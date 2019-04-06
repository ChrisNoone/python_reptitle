# coding: utf-8

from bs4 import BeautifulSoup

data = []
path = './1_2_homework_required/index.html'
with open(path, 'r') as web_data:
    Soup = BeautifulSoup(web_data, 'lxml')
    names = Soup.select('div.col-md-9 > div:nth-child(2) > div > div > div.caption > h4:nth-child(2) > a')
    pics = Soup.select('div.col-md-9 > div:nth-child(2) > div > div > img')
    prices = Soup.select('div.col-md-9 > div:nth-child(2) > div > div > div.caption > h4.pull-right')
    reviews = Soup.select('div.col-md-9 > div:nth-child(2) > div > div > div.ratings > p.pull-right')
    stars = Soup.select('div.col-md-9 > div:nth-child(2) > div > div > div.ratings > p:nth-child(2)')

for name, pic, price, review, star in zip(names, pics, prices, reviews, stars):
    info = {
        'name': name.get_text(),
        'pic': pic.get('src'),
        'price': price.get_text(),
        'review': review.get_text(),
        'star': len(star.find_all(class_='glyphicon-star'))
    }
    data.append(info)

for i in data:
    if i['star'] == 3:
        print(i['name'])
