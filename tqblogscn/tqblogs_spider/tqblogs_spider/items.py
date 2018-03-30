# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TqblogsSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

#ip代理池Item
class IpProxySpiderItem(scrapy.Item):
    ips = scrapy.Field()
    ports = scrapy.Field()


# 博客类信息
class BlogsSpiderItem(scrapy.Field):

    blogs_titles = scrapy.Field()
    blogs_urls = scrapy.Field()
    blogs_dates = scrapy.Field()
    blogs_abstracts = scrapy.Field()





