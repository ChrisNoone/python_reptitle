# coding: utf-8

from urllib import request

if __name__ == '__main__':
    rsp = request.urlopen('https://www.baidu.com')
    html = rsp.read().decode()
    print(html)
