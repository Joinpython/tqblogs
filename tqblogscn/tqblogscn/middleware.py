
import requests
from lxml import etree
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin



class BlockedIpMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print(request.META['REMOTE_ADDR'])
        print(request.META['HTTP_HOST'])
        print(request.META['SERVER_PORT'])
        print(request.META["HTTP_USER_AGENT"])

        ip = request.META['REMOTE_ADDR']

        if request.META['REMOTE_ADDR'] == ip:
            ip_address_html = requests.get(url='http://ip.chinaz.com/?IP='+str(ip))
            data = etree.HTML(ip_address_html.text)
            ip_address = data.xpath('//*[@id="leftinfo"]/div[3]/div[2]/p[2]/span[4]/text()')[0]
            print(ip_address)

            if ip_address == '国外':

                return HttpResponseForbidden('欢迎来到德莱联盟！！')

            else:
                return None
        else:
            return None

