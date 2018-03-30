
# 博客园python

import scrapy
from tqblogs_spider.items import BlogsSpiderItem

class BlogsCnblogsSpider(scrapy.Spider):
    name = 'blogs_cnblogs_spider'
    allowed_domains = ['cnblogs.com']
    start_urls = ['https://www.cnblogs.com/cate/python/#p1']

    items = BlogsSpiderItem()

    def parse(self, response):

        titles = response.xpath('//div[@class="post_item_body"]/h3/a/text()').extract()
        urls = response.xpath('//div[@class="post_item_body"]/h3/a/@href').extract()
        abstracts = response.xpath('//div[@class="post_item_body"]/p[@class="post_item_summary"]/text()').extract()
        dates = response.xpath('//div[@class="post_item_foot"]/text()').extract()
        views = response.xpath('//div[@class="post_item_foot"]/span[@class="article_view"]/a/text()').extract()

        self.items['blogs_titles'] = titles
        self.items['blogs_urls'] = urls
        self.items['blogs_dates'] = dates
        self.items['blogs_abstracts'] = abstracts
        self.items['blogs_titles'] =titles

        yield self.items




