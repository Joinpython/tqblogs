
# csdn

import scrapy
import json
import time

class CsdnBlogsSpider(scrapy.Spider):

    # t = str(time.time()).replace

    name = 'blogs_csdn_spider'
    allowed_domains = ['blog.csdn.net']
    # new表示刚刷新的文章,more刚刷新下面的表示全部文章
    start_urls = ['https://blog.csdn.net/api/articles?type=new&category=home']


    def parse(self, response):

        data = json.loads(response.text)

        for item in data['articles']:
            print(item['title'])
            print(item['url'])
            print(item['views'])
            print(item['created_at'])


