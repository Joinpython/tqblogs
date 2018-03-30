
# py社区

import scrapy


class BlogsPython88Spider(scrapy.Spider):
    name = 'blogs_python88_spider'
    allowed_domains = ['python88.com']

    # py社区　django主题　0-回复时间　1-主题时间 　2-回复量　3-精品主题
    # start_urls = ['http://www.python88.com/forum/djangoglobal?sort=1']

    # py社区　tab=12 DATA主题　0-回复时间　1-主题时间 　2-回复量　3-精品主题
    # start_urls = ['http://www.python88.com/?tab=12&sort=0']

    # py社区　tab=9 WEB开发主题　0-回复时间　1-主题时间 　2-回复量　3-精品主题
    # start_urls = ['http://www.python88.com/?tab=9&sort=0']


    # py社区　tab=1 python主题　0-回复时间　1-主题时间 　2-回复量　3-精品主题
    # start_urls = ['http://www.python88.com/?tab=1&sort=0']


    # py社区　tab=8 分享主题　0-回复时间　1-主题时间 　2-回复量　3-精品主题
    start_urls = ['http://www.python88.com/?tab=12&sort=0']

    def parse(self, response):

        titles = response.xpath('//span[@class="item_title"]/a/text()').extract()
        urls = response.xpath('//span[@class="item_title"]/a/@href').extract()
        dates = response.xpath('//span[@class="small fade"]/text()').extract()

        print(titles)
        # url 拼接　http://www.python88.com(urls)
        print(urls)
        print(dates)