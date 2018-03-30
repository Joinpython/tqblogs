
# 镁客网

import json
import scrapy
import time



class Im2makerSpider(scrapy.Spider):

    name = 'science_im2maker_spider'
    allowed_domains = ['www.im2maker.com']
    # start_urls = ['']

    def start_requests(self):

        url = 'http://www.im2maker.com/index.php?m=content&c=index&a=get_more'

        t = time.time()

        # 首页提交内容
        index_formdata = {
            'last_time':str(int(t)),
            'pages':'1',
            'pagesize':'15',
        }

        # 技术页提交内容
        technology_formdata = {
            'last_time':str(int(t)),
            'catid':'12',
            'pages':'1',
            'pagesize':'15',
        }

        # 新鲜事页提交内容
        fresh_formdata = {
            'last_time':str(int(t)),
            'catid':'2',
            'pages':'1',
            'pagesize':'15',
        }

        yield scrapy.FormRequest(url=url, formdata=fresh_formdata, callback=self.parse)

    def parse(self, response):
        html = json.loads(response.text)

        print(html)

        for data in html:
            print(data['title'])
            print(data['url'])
            print(data['picture'])
            print(data['description'])
            print(data['inputtime_str'])

