# 果壳网

import scrapy
import json

class GuoKrSpider(scrapy.Spider):
    name = 'science_guokr_spider'
    allowed_domains = ['guokr.com']
    start_urls = ['https://www.guokr.com/apis/minisite/article.json?retrieve_type=by_channel&channel_key=hot&limit=20&offset=1&_=1521380169023']


    def parse(self, response):
        data = json.loads(response.text, encoding='utf-8')
        for item in data['result']:
            print(len(item))
            print(item['title'])
            print(item['url'])
            print(item['summary'])
            print(item['date_modified'])
