import scrapy
import json
import time

from tqblogs_spider.items import ArticleWebsiteItem




class CsdnBlogsSpider(scrapy.Spider):
    t = time.time()
    t = str(t)
    t.replace('.', '')

    name = 'csdn_blogs_spider'
    allowed_domains = ['blog.csdn.net']
    # new表示刚刷新的文章,more刚刷新下面的表示全部文章
    start_urls = ['https://blog.csdn.net/api/articles?type=new&category=home&shown_offset=' + t]


    items = ArticleWebsiteItem()

    def parse(self, response):

        data = json.loads(response.text)

        # title_list = []
        # url_list = []
        # views_list = []
        # for item in data['articles']:
        #     title_list.append(item['title'])
        #     url_list.append(item['url'])
        #     views_list.append(item['views'])
        #
        # self.items['title'] = title_list
        # self.items['original_urls'] = url_list
        # self.items['views'] = views_list

        # print(data)
        # print(data['articles'])

        for item in data['articles']:
            print(item)
            self.items['title'] = item['title']
            self.items['original_urls'] = item['url']
            self.items['views'] = item['views']

            yield self.items
