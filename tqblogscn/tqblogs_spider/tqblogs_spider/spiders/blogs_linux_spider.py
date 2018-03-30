
# linux开源中国社区

import scrapy


class BlogsLinuxSpider(scrapy.Spider):
    name = 'blogs_linux_spider'
    allowed_domains = ['linux.cn']

    # news 表示新闻页　tech 表示技术页　
    start_urls = ['https://linux.cn/news/']


    def parse(self, response):
        titles = response.xpath('//span[@class="title"]/a/span/text()').extract()
        urls = response.xpath('//span[@class="title"]/a/@href').extract()
        abstracts = response.xpath('//ul[@class="article-list leftpic"]/li/p/text()').extract()
        dates = response.xpath('//ul[@class="article-list leftpic"]/li/p[@class="info"]/text()').extract()

        print(titles)
        print(urls)
        print(abstracts)
        print(dates)
