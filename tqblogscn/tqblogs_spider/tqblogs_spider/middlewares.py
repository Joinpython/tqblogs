# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html


import random
from scrapy import signals
from tqblogs_spider.settings import IP_PROXY_POOLS
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware


# ip代理中间件
class IpProxySpiderMiddleware(HttpProxyMiddleware):

    def __init__(self, ip=''):
        super(IpProxySpiderMiddleware, self).__init__()

        self.ip = ip

    def process_request(self, request, spider):
        this_ip = random.choice(IP_PROXY_POOLS)

        print("当前使用的ip:"+this_ip['ip_address'])

        request.meta['proxy'] = 'http://'+this_ip['ip_address']

# user-agent代理中间件
class UserAgentSpiderMiddleware(UserAgentMiddleware):
    def __str__(self, user_agent=''):
        super(UserAgentSpiderMiddleware, self).__init__()
        self.user_agent = user_agent

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            user_agent=crawler.settings.get('USER_AGENT_PROXY_POOLS')
        )

    def process_request(self, request, spider):
        user_agent = random.choice(self.user_agent)
        print('当前使用的User-Agent:'+user_agent)
        request.headers['User-Agent'] = user_agent



class TqblogsSpiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
