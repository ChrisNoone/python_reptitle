# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from pic.items import PicItem


class XhSpider(scrapy.Spider):
    name = 'xh'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/list-1-1.html']
    url_set = set()

    def parse(self, response):
        allpics = response.xpath('//div[@class="img"]/a')
        for pic in allpics:
            item = PicItem()
            name = pic.xpath('./img/@alt').extract()[0]
            addr = pic.xpath('./img/@src').extract()[0]
            if 'http' in addr:
                addr = addr
            else:
                addr = 'http://www.xiaohuar.com' + addr
            item['name'] = name
            item['addr'] = addr
            yield item

        # 获取所有的地址链接
        urls = response.xpath('//a/@href').extract()
        for url in urls:
            if url.startswith('http://www.xiaohuar.com/list-'):
                if url in XhSpider.url_set:
                    pass
                else:
                    XhSpider.url_set.add(url)
                    yield self.make_requests_from_url(url)
            else:
                pass
