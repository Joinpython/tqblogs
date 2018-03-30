
# 腾讯体育

import scrapy
import time
import re


class QqSportsSpider(scrapy.Spider):
    name = 'basketball_news_qq_sports_spider'
    allowed_domains = ['sports.qq.com']
    time_str = str(time.time()).replace('.', '')[:13]

    # print(time_str)

    start_urls = ['http://tags.open.qq.com/interface/tag/articles.php?callback=tagListCb&p=1&l=20&tag=NBA&oe=gbk&ie=utf-8&source=web&site=sports&_='+time_str]

    def parse(self, response):
        data = response.text

        # TODO 未解决　有时访问可以　有时403 大多数第一次有效

        data_list = re.findall(r'.*?"title":"(.*?)",.*?"url":"(.*?)",.*?',str(data), re.S)
        print(data_list)

        print(data)
        print(type(data))