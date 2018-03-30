
# 免费ip代理　西刺　快代

import  scrapy
from tqblogs_spider.items import IpProxySpiderItem


items = IpProxySpiderItem()

class IpProxyXiciSpider(scrapy.Spider):
    name = 'xici_spider'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/nn']

    custom_settings = {
        'ITEM_PIPELINES': {
            'tqblogs_spider.pipelines.IpProxySpiderPipline': 100
        }
    }

    def parse(self, response):
        ips = response.xpath('//tr[@class="odd"]/td[2]/text()').extract()
        ports = response.xpath('//tr[@class="odd"]/td[3]/text()').extract()

        items['ips'] = ips
        items['ports'] = ports

        yield items


class KuaidaiSpider(scrapy.Spider):
    name = 'kuaidai_spider'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/inha/1/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'tqblogs_spider.pipelines.IpProxySpiderPipline': 101
        }
    }


    def parse(self, response):
        ips = response.xpath('//tbody/tr/td[1]/text()').extract()
        ports = response.xpath('//tbody/tr/td[2]/text()').extract()

        items['ips'] = ips
        items['ports'] = ports

        yield items

