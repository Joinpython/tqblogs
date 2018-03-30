
# 虎嗅网

import scrapy
import json
import re

class HuXiuSpider(scrapy.Spider):
    name = 'science_huxiu_spider'
    allowed_domains = ['huxiu.com']
    start_urls = ['']

    def start_requests(self):
        url = 'https://www.huxiu.com/channel/ajaxGetMore'

        formdata = {
            'huxiu_hash_code':'76be7a12973e77661507717a17030c46',
            'page':'1',
            'catId':'107',
        }

        yield scrapy.FormRequest(url=url, formdata=formdata, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text, encoding='utf-8')

        html = data['data']['data']
        print(html)

        # TODO 未解决 正则匹配问题

        data_list = re.findall(r'.*? <a class="transition" title="(.*?)" herf="(.*?)" .*?>(.*?)</a> .*?', str(html), re.S)
        print(data_list)

