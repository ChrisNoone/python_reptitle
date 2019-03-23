# coding:utf-8

import urllib2

req = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(req)
fp = open("D://main1.html", "w+")
fp.write(response.read())
fp.close()