#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   house_data.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/4/13 17:53   SeafyLiang   1.0          None
"""

# 房天下官网  https://sh.newhouse.fang.com/house/s/b91/

# 房源详情 https://sh.newhouse.fang.com/loupan/1210130400/housedetail.htm

"""
爬虫思路：遍历首页房源列表获取所有房源id，拼接详情URL，遍历获取所有房源详情信息。
"""
import requests  # 请求数据
from pyquery import PyQuery as pq  # 本次采用pyquery和re解析数据
import time
import re
import random
import pandas as pd

# 为了提高爬虫安全性，除了最基本的延时，本次爬虫还加了一些请求头和代理ip（网上down的，也可以购买），让程序从中随机抽取并请求网页。
global user_agents
global proxy_list
user_agents = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
]
proxy_list = ["218.91.13.2:46332",
              "121.31.176.85:8123",
              "218.71.161.56:80",
              "49.85.1.230:28643",
              "115.221.121.165:41674",
              "123.55.177.237:808"
              ]

# 定义一个get_id函数，遍历获取所有房源id，将其存放在列表idlist中
def get_id(city):
    url = 'https://' + city + '.newhouse.fang.com/house/s/b91'
    user_agent = random.choice(user_agents)
    header = {'User-Agent': user_agent}
    proxy = {'Proxies': random.choice(proxy_list)}
    r = requests.get(url, headers=header, proxies=proxy)
    # time.sleep(2)
    r.encoding = 'GBK'
    pattern1 = re.compile('(?<=现有新楼盘)\d+')
    total = int(re.findall(pattern1, r.text)[0]) // 20 + 1
    idlist = []
    for i in range(1, total+1):
        print("正在获取第%s页的id，共%s页" % (i, total))
        url = 'https://' + city + '.newhouse.fang.com/house/s/b9' + str(i)
        user_agent = random.choice(user_agents)
        header = {'User-Agent': user_agent}
        proxy = {'Proxies': random.choice(proxy_list)}
        r = requests.get(url, headers=header, proxies=proxy)
        # time.sleep(2)
        r.encoding = 'gb2312'
        pattern = re.compile('(?<=loupan/)\d+')
        id = re.findall(pattern, r.text)
        for j in id:
            idlist.append(j)
    # print(idlist)
    return idlist


# 定义一个get_data函数，将房源id传入详情页URL中，遍历获取所有房源详情信息：
def get_data(city, id):
    house_name = ''
    detail1 = ''
    detail2 = ''
    detail3 = ''
    url = 'https://' + city + '.newhouse.fang.com/loupan/' + id + '/housedetail.htm'
    user_agent = random.choice(user_agents)
    header = {'User-Agent': user_agent}
    proxy = {'Proxies': random.choice(proxy_list)}
    r = requests.get(url, headers=header, proxies=proxy)
    time.sleep(1)
    r.encoding = 'utf8'
    doc = pq(r.text)
    # print(doc)
    data1 = doc('.ts_linear').items()
    for i in data1:
        if i.text() != '':
            house_name = i.text()
    data1 = doc('.list').items()
    index = 1
    for i in data1:
        detail = i.text()
        # print(detail)  # 房屋详细信息,3个str
        if index == 1:
            detail1 = detail
        elif index == 2:
            detail2 = detail
        elif index == 3:
            detail3 = detail
        index += 1

    row = {'house_name': house_name, 'detail1': detail1, 'detail2': detail2, 'detail3': detail3}
    print("新增一条记录:%s" % house_name)
    return row


if __name__ == '__main__':
    id = get_id('sh')
    list2 = []
    list1 = id
    for i in list1:
        if i not in list2:
            list2.append(i)
    list2
    print(list2)
    print("记录总数：%s条" % len(list2))
    df = pd.DataFrame(columns=['house_name', 'detail1', 'detail2', 'detail3'])
    for i in range(len(list2)):
        print("get_data:id=%s，第%s条，共%s条" % (list2[i], i, len(list2)))
        row = get_data('sh', list2[i])
        df = df.append(row, ignore_index=True)
    df.to_csv('house_out.csv')
