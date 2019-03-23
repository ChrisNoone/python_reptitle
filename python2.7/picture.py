# coding: utf-8

import urllib
import re


def get_html(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def get_image(html_code):
    reg = r'src="(.+?\.jpg)" width'
    reg_img = re.compile(reg)
    imglist = reg_img.findall(html_code)
    x = 0
    for i in imglist:
        urllib.urlretrieve(i, 'D://workspace/%s.jpg' % x)
        x += 1


print "请输入url："
url = raw_input()
if url:
    pass
else:
    url = 'http://tieba.baidu.com/p/1753935195'
get_image(get_html(url))
