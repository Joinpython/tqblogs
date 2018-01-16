
import re
import requests
from lxml import etree


def get_ip(ip):
    html = requests.get('http://ip.chinaz.com/'+ip)
    return html.text

with open('/home/tqblogs/project/tqblogscn/access.log','r') as file:
    data_list = []
    data_dict = {}
    for index,line in enumerate(file):
        data = line.split(' -')
        ip = data[0]
        if ip not in data_list:
            data_list.append(ip)
        data_dict['ip'] = ip

        time = data[2]
        time = re.search(r'.*?\[(.*?)\].*?"(.*?)/.*?" "(.*?)"',str(time))
        data_dict['time'] = time.group(1)

        get = time.group(2)
        data_dict['method'] = get

        user_agent = time.group(3)
        data_dict['user_agent'] = user_agent

    print(data_dict)
    print(data_list)

    ip = data_list[0]

    response = get_ip(ip)
    html = etree.HTML(response)
    city = html.xpath("//*[@id='leftinfo']/div[3]/div[2]/p[2]/span[4]/text()")
    print(city)

    del data_list
    del data_dict


