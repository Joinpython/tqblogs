
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


        for t in title:
            self.items['title'] = t
            yield self.items

        for u in url:
            self.items['original_urls'] = u
            yield self.items

        for v in views:
            self.items['views'] = v
            yield self.items

        yield scrapy.Request(url=self.start_urls[0], callback=self.parse, dont_filter=True)
