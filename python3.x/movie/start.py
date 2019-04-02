# coding: utf-8

from scrapy import cmdline

"""
直接运行次文件即可运行scrapy，相当于在terminal中执行命令 "scrapy crawl meiju --nolog"
"""
cmdline.execute(['acrapy', 'crawl', 'meiju', '--nolog'])
