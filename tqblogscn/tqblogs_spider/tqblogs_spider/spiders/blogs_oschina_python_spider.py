
# 开源中国python

import scrapy


class BlogsOschinaPythonSpider(scrapy.Spider):
    name = 'blogs_oschina_python_spider'
    allowed_domains = ['oschina.net']
    # 25/python-python开源软件　28/javascript-js开源软件　358/go-go开源软件 19/java-java开源软件
    start_urls = ['https://www.oschina.net/project/lang/19/java/']

    def parse(self, response):
        # print(response.text)

        titles = response.xpath('//div[@class="box-aw"]/a/div[@class="title"]/text()').extract()
        urls = response.xpath('//div[@class="box-aw"]/a/@href').extract()
        abstracts = response.xpath('//div[@class="box-aw"]/a/div[@class="summary"]/text()').extract()
        dates = response.xpath('//div[@class="box-aw"]/footer/span[1]/text()').extract()
        rates = response.xpath('//div[@class="box-aw"]/footer/span[4]/text()').extract()

        print(titles)
        print(urls)
        print(abstracts)
        print(dates)
        print(rates)