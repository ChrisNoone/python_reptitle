# coding: utf-8

from urllib import request
import requests
import os


def def_requests(url):
    rsp = requests.get(url)
    return rsp


def def_request(url):
    rsp = request.urlopen(url)
    return rsp


if __name__ == '__main__':
    base_url = 'https://www.baidu.com'
    html1 = def_requests(base_url).text
    html2 = def_request(base_url).read().decode()
    print('requests：', type(html1))
    print('request：', type(html2))

    '''
    file_name = os.path.join(r'.\down_pic', 'baidu.html')
    print(file_name)
    '''
