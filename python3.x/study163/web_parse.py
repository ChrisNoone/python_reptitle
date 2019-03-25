from bs4 import BeautifulSoup

data = []
path = './1_2/web/new_index.html'
with open(path, 'r') as web_data:
    Soup = BeautifulSoup(web_data, 'lxml')
    titles = Soup.select('ul > li > div.article-info > h3 > a')
    images = Soup.select('ul > li > img')
    descs = Soup.select('ul > li > div.article-info > p.description')
    rates = Soup.select('ul > li > div.rate > span')
    cates = Soup.select('ul > li > div.article-info > p.meta-info')

# print(titles, images, descs, rates, cates, sep='\n-------------------------\n')
for title, image, desc, rate, cate in zip(titles, images, descs, rates, cates):
    info = {
        'title': title.get_text(),
        'image': image.get('src'),
        'desc': desc.get_text(),
        'rate': rate.get_text(),
        'cate': list(cate.stripped_strings)
    }
    data.append(info)

for i in data:
    if float(i['rate']) > 3:
        print(i['title'], i['cate'])
