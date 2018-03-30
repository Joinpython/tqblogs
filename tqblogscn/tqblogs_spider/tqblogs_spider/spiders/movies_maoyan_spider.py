
# 猫眼电影

import scrapy
import json


class MaoYanSpider(scrapy.Spider):
    name = 'movies_maoyan_spider'
    allowed_domains = ['piaofang.maoyan.com']
    start_urls = ['https://box.maoyan.com/promovie/api/box/second.json']

    def parse(self, response):
        data = json.loads(response.text, encoding='utf-8')

        print(data['data']['list'])

        for item in data['data']['list']:
            # 电影名
            print(item['movieName'])
            # 总票房
            print(item['splitSumBoxInfo'])
            # 当前票房
            print(item['boxInfo'])
            # 上座率
            print(item['avgSeatView'])
            # 拼接url链接影片资源　http://piaofang.maoyan.com/movie/(movieId)?_v_=yes
            print(item['movieId'])
