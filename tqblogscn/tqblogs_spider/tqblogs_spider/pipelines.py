# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymongo
from tqblogs_spider import settings


class TqblogsSpiderPipeline(object):

    def process_item(self, item, spider):
        return item


class IpProxySpiderPipline(object):

    def __init__(self):
        self.file = open('ip.json', 'w+',encoding='utf-8')

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) +'\n'

        self.file.write(lines)

        return item


class BlogsSpiderPipeline(TqblogsSpiderPipeline):

    def __init__(self):

        self.client = pymongo.MongoClient(host=settings.MONGODB_HOST,
                                          port=settings.MONGODB_PORT)

        self.db = self.client[settings.MONGODB_DB]
        self.collection = ''

    def process_item(self, item, spider):

        if spider.name == 'blogs_cnblogs_spider':

            self.collection = self.db['cnblogs']
            self.collection.insert(dict(item))

        if spider.name == 'blogs_csdn_spider':
            self.collection = self.db['csdn']
            self.collection.insert(dict(item))

        return item






