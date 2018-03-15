# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleWebsiteItem(scrapy.Item):

    title = scrapy.Field()
    original_urls = scrapy.Field()
    views = scrapy.Field()


class TqblogsSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()
    url = scrapy.Field()
    rate = scrapy.Field()
    images = scrapy.Field()
    abstract = scrapy.Field()
    image_urls = scrapy.Field()
    image_paths = scrapy.Field()








