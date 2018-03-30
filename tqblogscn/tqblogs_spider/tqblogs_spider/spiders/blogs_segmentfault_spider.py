
# 思否

import scrapy
import time


class SegmentfaultSpider(scrapy.Spider):
    name = 'blogs_segmentfault_spider'
    allowed_domains = ['segmentfault.com']
    start_urls = ['https://segmentfault.com/']
    # time_str = str(time.time()).replace('.', '')[:10]
    # start_urls = ['https://segmentfault.com/api/tag/python/contents?start='+time_str+'&_=python']

    def parse(self, response):

        # print(response.text)
        # TODO 未解决动态加载数据的抓取

        titles = response.xpath('//div[@class="mb6"]/h4/a/text()').extract()
        urls = response.xpath('//div[@class="mb6"]/h4/a/@href').extract()

        print(titles)
        print(urls)


