
# 科技行者

import scrapy


class CnetnewsSpider(scrapy.Spider):
    name = 'science_cnetnews_spider'
    allowed_domains = ['cnetnews.com.cn']
    start_urls = ['http://www.cnetnews.com.cn/list-7-1-0-0-1-0.htm']


    def parse(self, response):
        # print(response.text)
        titles = response.xpath('//div[@class="qu_tix"]/b/a/text()').extract()
        urls = response.xpath('//div[@class="qu_tix"]/b/a/@href').extract()
        abstracts = response.xpath('//div[@class="qu_tix"]/p[1]/text()').extract()
        # dates = response.xpath('//div[class="qu_loop"]/div[@class="qu_times"]/text()').extract()

        print(titles)
        print(urls)
        print(abstracts)
        # print(dates)
