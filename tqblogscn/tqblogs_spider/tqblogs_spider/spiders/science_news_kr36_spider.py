
# 36kr网

import re
import scrapy

import json

class Kr36Spider(scrapy.Spider):
    name = 'science_news_kr36_spider'
    allowed_domains = ['36kr.com']
    start_urls = ['http://36kr.com/api/search-column/mainsite?per_page=20&page=1']

    def parse(self, response):
        html = json.loads(response.text, encoding='utf-8')

        print(html['data']['items'])

        for item in html['data']['items']:
            print(item['title'])
            # 拼接程url链接　http://36kr.com/p/(id).html
            print(item['id'])
            # 图片
            print(item['cover'])
            print(item['published_at'])
        # print(type(html))

        # kr36_data = re.findall(r'.*?"id":(.*?),.*?"title":"(.*?)".*?"cover":"(.*?)".*?"published_at":"(.*?)".*?', str(html), re.S)
        # # print(data)
        # for data in kr36_data:
        #     print(data[0])
        #     print(data[1])
        #     print(data[2])
        #     print(data[3])


        # print(html)
        # print(type(html))


# 硅谷密探网
class SiliconSecretSpider(scrapy.Spider):
    name = 'science_news_silicon_secret_spider'
    allowed_domains = ['svinsight.com']
    start_urls = ['http://www.svinsight.com/']

    def parse(self, response):
        titles = response.xpath('//div[@class="content2"]/h2/text()').extract()
        urls = response.xpath('//div[@class="row underline"]/a/@href').extract()

        print(titles)
        print(urls)


