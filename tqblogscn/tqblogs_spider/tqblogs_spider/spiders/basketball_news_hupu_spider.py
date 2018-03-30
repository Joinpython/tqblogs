
# 虎扑篮球
import scrapy




class HupuSpider(scrapy.Spider):
    name = 'basketball_news_hupu_spider'
    allowed_domains = ['nba.hupu.com']
    start_urls = ['https://voice.hupu.com/nba/1']


    def parse(self, response):
        titles = response.xpath('//div[@class="list-hd"]/h4/a/text()').extract()
        urls = response.xpath('//div[@class="list-hd"]/h4/a/@href').extract()


        print(titles)
        print(urls)