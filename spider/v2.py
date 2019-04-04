# coding: utf-8

from urllib import request

base_url = 'https://www.zhihu.com/topics'

req = request.Request(base_url, method='GET')
rsp = request.urlopen(req)
html = rsp.read().decode('utf-8')
print(html)
