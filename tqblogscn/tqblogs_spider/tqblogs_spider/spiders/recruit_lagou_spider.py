
# 拉勾网

import scrapy




class LagouSpider(scrapy.Spider):
    name = 'recruit_lagou_spider'
    allowed_domains = ['lagou.com']


    def start_requests(self):
        url = 'https://www.lagou.com/jobs/list_python?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput='

        formdata = {
            'first':'true',
            'pn':'1',
            'kd':'python',
        }

        yield scrapy.FormRequest(url=url, formdata=formdata, callback=self.parse)

    def parse(self, response):
        print(response.text)
        # TODO 获取数据失败

