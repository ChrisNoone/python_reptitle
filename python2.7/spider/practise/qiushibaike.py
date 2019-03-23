# -*- coding:utf-8 -*-

import urllib,urllib2
import re

pageIndex = 1
url = 'https://www.qiushibaike.com/hot/page/'+str(pageIndex)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
headers = {"User-Agent":user_agent}

try:
    req = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(req)
    html = response.read()
#     html = response.read().replace('\n','').replace('\r','').replace(' ','')
    fp = open(r"C:\Users\imade\Desktop\qiushibaike.txt","w")
    fp.write(html)
#     pattern = re.compile(r'<divclass="content"><span>(.*?)</span></div></a><!--.*?-->(.*?)<divclass="stats"><!--.*?--><spanclass="stats-vote"><iclass="number">(\d*?)</i>')
    pattern = re.compile(r'<div.*?class="author.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?<!--.*?-->(.*?)<div class="stats">.*?<i class="number">(\d*?)</i>',re.S)
    m_tr =  re.findall(pattern,html)
    for item in m_tr:
        hasImg = re.search('img',item[2])
        if not hasImg:
            print '作者：',item[0].replace('\n','').replace('\r','')
            print '段子：',item[1].replace('\n','').replace('\r','').replace('<br/>','')
            print '评论数：',item[3].replace('\n','').replace('\r',''),'\n'
            
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
        