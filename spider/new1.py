# coding:utf-8

import urllib.request

req = urllib.request.Request("http://www.baidu.com")
response = urllib.request.urlopen(req)
fp = open("D://main1.html", "w+")
fp.write(response.read())
fp.close()