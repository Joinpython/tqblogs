
import scrapy
from tqblogs_spider.items import ArticleWebsiteItem


class OpenSourceChineseCommunity(scrapy.Spider):
    name = 'open_chinese_community_spider'
    allowed_domains = ['oschina.net']
    start_urls = ['https://www.oschina.net/action/ajax/get_more_recommend_blog?classification=0&p=1']

    items = ArticleWebsiteItem()

    def parse(self, response):
        # print(response.text)
        title = response.xpath('//div[@class="box-aw"]/header/a/@title').extract()
        url = response.xpath('//div[@class="box-aw"]/header/a/@href').extract()
        views = response.xpath('//div[@class="box-aw"]/footer/span[4]/text()').extract()

        self.items['title'] = title
        self.items['original_urls'] = url
        self.items['views'] = views

        yield self.items