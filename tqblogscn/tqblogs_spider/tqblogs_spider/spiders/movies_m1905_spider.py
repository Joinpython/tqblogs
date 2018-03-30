
# 电影网1905

import scrapy


class M1905Spider(scrapy.Spider):
    name = 'movies_m1905_spider'
    allowed_domains =['1905.com']
    start_urls = ['http://www.1905.com/list-p-catid-220.html?page=1']

    def parse(self, response):

        titles = response.xpath('//div[@class="pic-pack-inner"]/h3/a/text()').extract()
        urls = response.xpath('//div[@class="pic-pack-inner"]/h3/a/@href').extract()
        abstracts = response.xpath('//div[@class="pic-pack-inner"]/p/text()').extract()
        image_urls = response.xpath('//li[@class="pic-pack-out pic-vertical"]/a/img/@src').extract()

        print(titles)
        print(urls)
        print(abstracts)
        print(image_urls)
