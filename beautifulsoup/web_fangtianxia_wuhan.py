# coding: utf-8

from bs4 import BeautifulSoup
import requests
import pymysql


def s_fang(url):
    html = requests.get(url)
    html.encoding = 'gb2312'
    Soup = BeautifulSoup(html.text, 'lxml')
    names = Soup.select('div.nlc_details div.nlcd_name > a')
    areas = Soup.select('div.nlc_details div.address > a > span')
    address = Soup.select('div.nlc_details div.address > a')
    status = Soup.select('div.nlc_details span.inSale')
    labels = Soup.select('div.nlc_details div.fangyuan')
    prices = Soup.select('div.nlc_details div.nhouse_price > span')
    numbers = Soup.select('div.nlc_details div.tel > p')
    types = Soup.select('div.nlc_details div[class="house_type clearfix"]')
    data = []

    for name, area, addres, statu, label, price, number, type in zip(names, areas, address, status, labels, prices, numbers, types):
        size = [text.strip()[-10:].strip() for text in type.find_all(text=True) if text.parent.name != 'a' and text.strip()]
        if len(size):
            size = [text.strip()[-10:].strip() for text in type.find_all(text=True) if text.parent.name != 'a' and text.strip()][-1]
        else:
            size = '暂无信息'
        info = {
            'name': name.get_text().strip(),
            'area': area.get_text().strip().lstrip('[').rstrip(']'),
            'address': [text.strip() for text in addres.find_all(text=True) if text.parent.name != 'span' and text.strip()][0],
            'statu': statu.get_text().strip(),
            'label': [text.strip() for text in label.find_all(text=True) if text.parent.name != 'span' and text.strip()],
            'price': format_int(price.get_text().strip()),
            'number': number.get_text().strip(),
            'type': [text.strip() for text in type.find_all(text=True) if text.parent.name == 'a' and text.strip()],
            'size': size
        }
        print(info)
        data.append(info)
    return data


def format_data(dict):
    dict['label'] = ','.join(dict['label'])
    dict['type'] = ','.join(dict['type'])
    return tuple(dict.values())


def format_int(str):
    try:
        return int(str)
    except:
        return 0


def insert_db(data):
    conn = pymysql.connect('127.0.0.1', 'root', 'root', 'spider')
    cur = conn.cursor()
    head = 'insert into ftx(`name`, `area`, `address`, `status`, `label`, `price`, `number`, `type`, `size`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    sql = []
    for i in data:
        tmp = format_data(i)
        sql.append(tmp)
    try:
        cur.executemany(head, sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
    conn.close()


baseurl = 'https://wuhan.newhouse.fang.com/house/s/b9'
for i in range(1, 36):
    url = baseurl + str(i) + '/'
    d = s_fang(url)
    insert_db(d)
    print('第%s页爬取完成' % str(i))
