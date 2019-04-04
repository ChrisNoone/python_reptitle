# coding: utf-8

from urllib import request
import os


if __name__ == '__main__':
    rsp = request.urlopen('https://www.baidu.com')
    html = rsp.read().decode()
    file_name = os.path.join(r'.\down_pic', 'baidu.html')
    print(file_name)
