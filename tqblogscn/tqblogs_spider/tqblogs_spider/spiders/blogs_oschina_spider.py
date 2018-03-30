
# 开源中国

import scrapy


class BlogsOschinaSpider(scrapy.Spider):
    name = 'blogs_oschina_spider'
    allowed_domains = ['oschina.net']
    'https://www.oschina.net/action/ajax/get_more_recent_blog?classification=0&p=2'
    # recent 最新文章　recommend 最新推荐
    start_urls = ['https://www.oschina.net/action/ajax/get_more_recent_blog?classification=0&p=1']

    def parse(self, response):
        # print(response.text)

        titles = response.xpath('//div[@class="box-aw"]/header/a/h2/text()').extract()
        urls = response.xpath('//div[@class="box-aw"]/header/a/@href').extract()
        abstracts = response.xpath('//div[@class="box-aw"]/section/text()').extract()
        dates = response.xpath('//div[@class="box-aw"]/footer/span[3]/text()').extract()
        views = response.xpath('//div[@class="box-aw"]/footer/span[4]/text()').extract()

        print(titles)
        print(urls)
        print(abstracts)
        print(dates)
        print(views)
