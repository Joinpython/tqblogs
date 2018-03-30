
# NBA中文网

import scrapy

class BasketballChinaSpider(scrapy.Spider):
    name = 'basketball_news_china_spider'
    allowed_domains = ['china.nba.com']
    start_urls = ['http://china.nba.com/c/index_news.htm']

    def parse(self, response):
        # print(response.text)

        title = response.xpath('//div[@class="new"]/a/h3/text()').extract()
        url = response.xpath('//div[@class="new"]/a/@href').extract()

        print(title)
        print(url)