# coding:utf-8

import urllib,urllib2
import cookielib

'''
#声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
print type(cookie),cookie
for item in cookie:
    print 'Name = '+item.name+' | ','Value = '+item.value
'''

'''
#设置保存cookie的文件，同级目录下的cookie.txt
filename = r'D:/cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#创建一个请求，原理同urllib2的urlopen
response = opener.open("http://www.baidu.com")
#保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)
'''
'''    
cookiefile = r'C:\Users\imade\Desktop\cookie.txt'
cookie = cookielib.MozillaCookieJar(cookiefile)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open('http://www.google.com')
cookie.save(ignore_discard=True, ignore_expires=True)
'''

'''
#创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load(r'C:\Users\imade\Desktop\cookie.txt', ignore_discard=True, ignore_expires=True)
#创建请求的request
req = urllib2.Request("http://www.google.com")
#利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()
'''

filename = 'C:\Users\imade\Desktop\cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
data = urllib.urlencode({"j_username": "NooneLiu", "j_password": "123456", "remember_me": "false", "from": "/", "Jenkins-Crumb": "de513afba452d8fc82cdaab7afbadd8e"})
url = "http://localhost:8080/j_acegi_security_check"
result = opener.open(url,data)
cookie.save(ignore_discard=True, ignore_expires=True)
url2 = "http://localhost:8080/view/all/builds"
result = opener.open(url2)
print result.read()