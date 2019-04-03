# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from urllib import request
import os


class PicPipeline(object):
    def process_item(self, item, spider):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }
        req = request.Request(url=item['addr'], headers=headers)
        res = request.urlopen(req)
        # os.path.join 是拼接一个文件名，用反斜线“\”
        # “.”代表当前路径下，使用前先使用 os.getcwd 查看当前路径
        file_name = os.path.join(r".\pic\down_pic", item['name']+'.jpg')
        # 打开模式 'wb' 表示打开时如果没有文件则创建文件然后再写，但是一定得保证文件路径是存在的
        with open(file_name, 'wb') as fp:
            fp.write(res.read())
