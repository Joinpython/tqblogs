
# mysql社区

import scrapy


class BlogsInnoMysqlSpider(scrapy.Spider):
    name = 'blogs_innomysql_spider'
    allowed_domains = ['innomysql.com']
    start_urls = ['http://www.innomysql.com/page/1/']


    def parse(self, response):
        # data = response.text
        #
        # print(data)

        titles = response.xpath('//div[@class="mob-ctt"]/h3/a/text()').extract()
        urls = response.xpath('//div[@class="mob-ctt"]/h3/a/@href').extract()
        abstracts = response.xpath('//div[@class="mob-ctt"]/div[@class="mob-sub"]/text()').extract()
        print(titles)
        print(urls)
        print(abstracts)