# coding:utf-8

import urllib2

req1 = urllib2.Request("http://www.abc99xyz.com/")
req2 = urllib2.Request("http://cn163.net/")
req = [req1,req2]

for i in req:
    print i.get_full_url()
    try:
        print urllib2.urlopen(i).read()
    except urllib2.HTTPError,e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):    
            print e.reason
    except urllib2.URLError,e:
        if hasattr(e,"reason"): 
            print e.reason
    print "\n"