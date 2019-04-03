# coding: utf-8

import scrapy
from zhihutopic.items import ZhihutopicItem


class ZhihutopicSpider(scrapy.Spider):
    name = 'topic'
    # 设置allowed_domains的含义是过滤爬取的域名，在插件OffsiteMiddleware启用的情况下（默认是启用的），不在此允许范围内的域名就会被过滤，而不会进行爬取
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/topics']

    def parse(self, response):
        topics = response.xpath('//div[@class="zh-general-list clearfix"]/div')
        for each_topic in topics:
            print(item)
            item = ZhihutopicItem()
            item['name'] = each_topic.xpath('./div/div/a[1]/img').text
            item['dec'] = each_topic.xpath('./div/div/p').text
            # print(item['name'])
            yield item
