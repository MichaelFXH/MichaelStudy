# -*- coding: utf-8 -*-
import scrapy


class YdjpkSpider(scrapy.Spider):
    name = 'ydjpk'
    allowed_domains = ['youdao.com']
    start_urls = ['http://youdao.com/']

    def start_requests(self):
        urls=['https://ke.youdao.com/tag/1528?outVednor=zw_zsttx_baidupz_pc_title_0206_001&Pdt=CourseWeb']
        for url in urls:
            yield  scrapy.Request(url,callback=self.parse) #爬取到页面交给parse 处理

    def parse(self, response):
        with open('yd.html','wb') as f:
           f.write(response.body)
        print('进入解析')