# coding: utf-8

import requests
from urllib import error
from bs4 import BeautifulSoup
import pymysql


def get_web_data(url):
    """
    接受一个url，返回beautiful对象
    :param url:
    :return:
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/\
        73.0.3683.86 Safari/537.36'
    }
    try:
        rsp = requests.get(url, headers=headers).text
        html = BeautifulSoup(rsp, 'lxml')
    except (error.HTTPError, error.URLError) as e:
        print(e)
    return html


def parse_data(html_data):
    """
    接受一个beautifulsoup对象，返回提取信息的列表，一个返回一个页面的数据
    :param html_data:
    :return:
    """
    news = html_data.find_all(name='div', attrs={'class': 'item'})
    page_data = []
    for item in news:
        content = item.find(name='a', attrs={'class': 'show-content color-chag'})
        if item.find(name='div', attrs={'class': 'area-summary'}):
            summary = item.find(name='div', attrs={'class': 'area-summary'}).text
        else:
            summary = '暂无'
        digg = item.find(name='a', attrs={'class': 'digg-a'}).find(name='b')
        discus = item.find(name='a', attrs={'class': 'discus-a'}).find(name='b').text
        user = item.find(name='a', attrs={'class': 'user-a'}).find(name='b').text
        time = item.find(name='a', attrs={'class': 'time-a'}).find(name='b')
        href = item.find(name='a', attrs={'class': 'show-content color-chag'})
        img = item.find_all(name='img')[0]

        info = {
            'content': fix_str(content.text.strip()),
            'summary': fix_str(summary),
            'digg': fix_str(digg.text),
            'discus': fix_str(discus),
            'user': fix_str(user),
            'time': fix_str(time.text),
            'href': fix_str(href.attrs['href']),
            'img': 'https:' + fix_str(img.attrs['original'])
        }
        page_data.append(info)
    return page_data


def print_data(data):
    # 测试用
    for item in data:
        print(item, '\n----------------------------------------------\n')


def fix_str(strx):
    """
    处理sql语句中包含单引号和双引号的问题，使用replace方法给引号前加反斜线
    :param strx:
    :return:
    """
    return strx.replace('"', '\\\"').replace("'", "\\\'")


def data_to_database(data):
    conn = pymysql.connect('127.0.0.1', 'root', 'root', 'spider')
    cursor = conn.cursor()
    list_sql = []
    for item in data:
        list_sql.append(dict_to_str(item))
        '''
        sql = 'insert into chouti(`content`, `summary`, `digg`,`discus`, `user`, `time`, `href`, `img`) values ("%s","%s","%s","%s","%s","%s","%s","%s");' % dict_to_str(item)
        sql_str = sql_str + sql + '\n'
        '''
    tem = 'insert into chouti(`content`, `summary`, `digg`,`discus`, `user`, `time`, `href`, `img`) values (%s,%s,%s,%s,%s,%s,%s,%s);'
    # %s 不需要再用引号括起来
    cursor.executemany(tem, list_sql)
    conn.commit()


def dict_to_str(data):
    # li = list(data.values())
    # return '"' + '","'.join(li) + '"'
    return tuple(data.values())


if __name__ == '__main__':
    base_url = 'https://dig.chouti.com/all/hot/recent/'
    for i in range(1, 11):
        url = base_url + str(i)
        html_data = get_web_data(url)
        news = parse_data(html_data)
        print('正在存储第%s页数据...' % str(i))
        data_to_database(news)
