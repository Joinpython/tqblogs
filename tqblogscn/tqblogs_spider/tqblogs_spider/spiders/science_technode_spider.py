
#　动点科技网


import scrapy

import re
import json

class TechnodeSpider(scrapy.Spider):
    name = 'science_technode_spider'
    allowed_domains = ['cn.technode.com']
    start_urls = ['https://cn.technode.com/post/category/startups/page/1']

    # def start_requests(self):
    #     url = 'https://cn.technode.com/wp-admin/admin-ajax.php'
    #
    #     formdata = {
    #         'action':'td_ajax_block',
    #         'td_atts':'{"ajax_pagination":"infinite"}',
    #         'td_cur_cat':'',
    #         'td_block_id':'td_uid_11_5aae2d829e4c4',
    #         'td_column_number':'2',
    #         'td_current_page':'1',
    #         'block_type':'6',
    #     }
    #
    #     yield scrapy.FormRequest(url=url, formdata=formdata,callback=self.parse)
    #
    # def parse(self, response):
    #     data = json.loads(response.text, encoding='utf-8')
    #     print(data)
    #
    #     html = re.findall(r'.*? <a .*? href="(.*?)" title="(.*?)">.*?', str(data), re.S)
    #     print(html)
    #     print(len(html))
    #
    #
    #     for m in html:
    #         print(m[0][:20])
    #         print(m[1])

    def parse(self, response):
        titles = response.xpath('//div[@class="item-details"]/h3/a/text()').extract()
        urls = response.xpath('//div[@class="item-details"]/h3/a/@href').extract()
        abstracts = response.xpath('//div[@class="item-details"]/p/text()').extract()
        image_urls =response.xpath('//div[@class="thumb-wrap"]/a/img/@src').extract()
        dates = response.xpath('//div[@class="meta-info"]/time/text()').extract()


        print(titles)
        print(urls)
        print(abstracts)
        print(image_urls)
        print(dates)





