import scrapy
import json
from tqblogs_spider.items import TqblogsSpiderItem

class DouBanSpider(scrapy.Spider):
    name = 'douban_hot_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=120&page_start=80']

    items = TqblogsSpiderItem()

    def parse(self, response):
        data = json.loads(response.text)
        for item in data['subjects']:
            url = item['url']

            yield scrapy.Request(url=url, callback=self.parse_abstract, meta={'meta':url})

    def parse_abstract(self,response):

        title = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        url = response.meta['meta']
        rate = response.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract()
        images = response.xpath('//*[@id="mainpic"]/a/img/@src').extract()
        abstract_list = response.xpath('//*[@id="link-report"]/span/text()').extract()

        abstracts_list = []

        for abstract in abstract_list:
            abstract = abstract.replace(' ', '').replace('\u3000', '').replace('\n', '')
            abstracts_list.append(abstract)

        self.items['title'] = title
        self.items['url'] = url
        self.items['rate'] = rate
        self.items['images'] = images
        self.items['abstract'] = abstracts_list
        self.items['image_urls'] = images

        yield self.items




