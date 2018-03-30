import scrapy
from tqblogs_spider.items import ArticleWebsiteItem

class V2exSpider(scrapy.Spider):
    name = 'v2ex_spider'
    allowed_domains = ['v2ex.com']
    start_urls = ['https://www.v2ex.com/?tab=hot']

    items = ArticleWebsiteItem()

    def parse(self, response):
        # print(response.text)
        url_list = response.xpath('//span[@class="item_title"]/a/@href').extract()
        title = response.xpath('//span[@class="item_title"]/a/text()').extract()
        views = response.xpath('//div[@class="cell item"]/table/tr/td[4]/a/text()').extract()

        urls_list = []
        for url in url_list:
            urls_list.append('https://www.v2ex.com' + url)

        # self.items['original_urls'] = urls_list
        # self.items['title'] = title
        # self.items['views'] = views

        for url in urls_list:
            self.items['original_urls'] = url
            yield self.items

        for t in title:
            self.items['title'] = t
            yield self.items

        for v in views:
            self.items['views'] = v
            yield self.items

        yield scrapy.Request(url=self.start_urls[0], callback=self.parse, dont_filter=True)





