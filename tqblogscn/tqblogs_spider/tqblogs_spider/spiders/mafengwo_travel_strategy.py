import scrapy


class MaFengWoStrategy(scrapy.Spider):
    name = 'mafengwo_travel_strategy'
    allowed_domains = ['mafengwo.cn']
    start_urls = ['http://www.mafengwo.cn/gonglve/']

    def parse(self, response):
        print(response.text)