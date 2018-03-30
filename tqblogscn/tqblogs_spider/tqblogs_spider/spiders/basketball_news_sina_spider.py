
# 新浪体育

import scrapy


class SinaSpider(scrapy.Spider):
    name = 'basketball_news_sina_spider'
    allowed_domains = ['sports.sina.com']
    start_urls = ['http://sports.sina.com.cn/nba/']

    def parse(self, response):

        titles = response.xpath('//li[@class="item"]/p/a/text()').extract()
        urls = response.xpath('//li[@class="item"]/p/a/@href').extract()

        print(titles)
        print(urls)
