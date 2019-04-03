# coding: utf-8

from scrapy import cmdline

"""
直接运行次文件即可运行scrapy，相当于在terminal中执行命令 "scrapy crawl meiju --nolog"
参考：https://www.cnblogs.com/llssx/p/8378832.html
"""
cmdline.execute(['acrapy', 'crawl', 'topic'])

"""
创建工程命令：scrapy startproject projectName
参考：https://www.cnblogs.com/kongzhagen/p/6549053.html
"""