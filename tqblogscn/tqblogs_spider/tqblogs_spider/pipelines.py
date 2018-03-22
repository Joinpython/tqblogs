# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import redis
import scrapy
from datetime import datetime
import logging
import pymysql
from tqblogs_spider import settings
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


# 数据保存
class SaveDataPipeline(object):

    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=False)
        self.id = 125

        # 通过cursor执行增删改查
        self.cursor = self.connect.cursor()

        self.host = settings.REDIS_HOST
        self.port = settings.REDIS_PORT
        self.db = settings.REDIS_DB

        self.connet = redis.StrictRedis(host=self.host, port=self.port, db=self.db)

    def process_item(self, item, spider):

        if spider.name == 'douban_hot_spider':
            try:
                # 查重处理
                self.cursor.execute("""select * from movies_movies where title = %s""", item['title'])

                # 是否有重复的数据
                repetition = self.cursor.fetchone()

                # 重复
                if repetition:
                    pass

                else:
                    # 插入数据
                    sql = "insert into movies_movies(id, create_time, update_time,title, url, rate, images, abstract) value(%s,%s,%s,%s, %s, %s, %s, %s)"
                    params =(self.id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.now().strftime("%Y-%m-%d %H:%M:%S"), item['title'], item['url'], item['rate'], item['images'], item['abstract'])
                    self.cursor.execute(sql, params)
                    # 提交sql语句
                    self.connect.commit()
                    self.id += 1

            except Exception as error:
                # 出现错误时打印
                logging.log(error,msg='错误信息')

        if spider.name == 'douban_top_spider':
            pass

        if spider.name == 'v2ex_spider':
            try:
                # 查重处理
                self.cursor.execute("""select * from  message_freshnews  where title = %s""", item['title'])

                # 是否有重复的数据
                repetition = self.cursor.fetchone()

                # 重复
                if repetition:
                    pass

                else:
                    # 插入数据
                    sql = "insert into message_freshnews(id, create_time, update_time,title, url, views, category) value(%s, %s, %s, %s, %s, %s, %s)"
                    params = (self.id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.now().strftime("%Y-%m-%d %H:%M:%S"),item['title'], item['original_urls'], item['views'], 'V2EX')
                    self.cursor.execute(sql, params)
                    # 提交sql语句
                    self.connect.commit()
                    self.id += 1

            except Exception as error:
                # 出现错误时打印
                logging.log(error, msg='错误信息')


        if spider.name == 'csdn_blogs_spider':

            try:
                # 查重处理
                self.cursor.execute("""select * from  message_freshnews  where title = %s""", item['title'])

                # 是否有重复的数据
                repetition = self.cursor.fetchone()

                # 重复
                if repetition:
                    pass

                else:
                    # 插入数据
                    sql = "insert into message_freshnews(id, create_time, update_time,title, url, views, category) value(%s, %s, %s, %s, %s, %s, %s)"
                    params = (self.id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.now().strftime("%Y-%m-%d %H:%M:%S"),item['title'], item['original_urls'], item['views'], 'CSDN')
                    self.cursor.execute(sql, params)
                    # 提交sql语句
                    self.connect.commit()
                    self.id += 1

            except Exception as error:
                # 出现错误时打印
                logging.log(error, msg='错误信息')

        if spider.name == 'open_chinese_community_spider':

            try:
                # 查重处理
                self.cursor.execute("""select * from  message_freshnews  where title = %s""", item['title'])

                # 是否有重复的数据
                repetition = self.cursor.fetchone()

                # 重复
                if repetition:
                    pass

                else:
                    # 插入数据
                    sql = "insert into message_freshnews(id, create_time, update_time,title, url, views, category) value(%s, %s, %s, %s, %s, %s, %s)"
                    params = (self.id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.now().strftime("%Y-%m-%d %H:%M:%S"),item['title'], item['original_urls'], item['views'], '开源中国')
                    self.cursor.execute(sql, params)
                    # 提交sql语句
                    self.connect.commit()
                    self.id += 1

            except Exception as error:
                # 出现错误时打印
                logging.log(error, msg='错误信息')

        return item

# 保存图片
class HotMoviesImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(url=image_url, meta={'item':item['title']})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        image_guid = item

        return '/%s.jpg'%(image_guid)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok ]

        if not image_paths:
            raise DropItem("Item contains no images")

        item['image_paths'] = image_paths

        return item


