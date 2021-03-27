#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   simple_crawler.py    
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/27 23:09   SeafyLiang   1.0          None
"""
import csv  # 用于把爬取的数据存储为csv格式，可以excel直接打开的
import time  # 用于对请求加延时，爬取速度太快容易被反爬
from time import sleep  # 同上
import random  # 用于对延时设置随机数，尽量模拟人的行为
import requests  # 用于向网站发送请求
from lxml import etree  # lxml为第三方网页解析库，强大且速度快

"""
# 查找li带有class属性,值为two的元素,下的div元素下的a元素

rst3 = html.xpath('//li[@class="two"]/div/a') # <class 'list'>
rst3 = rst3[0]  #选中res3列表中的第一个元素

print('-------------\n',type(rst3)) # ==><class 'lxml.etree._Element'>
print(rst3.tag)  # ==>输出res3的标签名
print(rst3.text)  # ==> 输出res3中的文本内容
"""

"""
构造请求url，添加头部信息headers即复制前文标记的User-Agent，
通过requests.get方法向服务器发送请求，返回html文本。
添加headers目的在于告诉服务器，你是真实的人在访问其网站。
如果你不添加headers直接访服务器，会在对方服务器显示python在访问，那么，你很可能会被反爬，常见的反爬就是封你ip。
"""
url = 'http://yz.yuzhuprice.com:8003/findPriceByName.jspx?page.curPage=1&priceName=红木类'
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
}
response = requests.get(url, headers=headers, timeout=10)
html = response.text
parse = etree.HTML(html)  # 解析网页
total_pagenum = parse.xpath('//*[@id="page"]/span[1]/b[3]')[0].text
print('共计%s页' % total_pagenum)
for x in range(1, int(total_pagenum)):
    print('正在爬取第%s页' % x)
    url = 'http://yz.yuzhuprice.com:8003/findPriceByName.jspx?page.curPage={}&priceName=红木类'.format(
        x)
    response = requests.get(url, headers=headers, timeout=10)
    html = response.text
    parse = etree.HTML(html)  # 解析网页
    all_tr = parse.xpath('//*[@id="173200"]')
    total_pagenum = parse.xpath('//*[@id="page"]/span[1]/b[3]')[0].text

    i = 0
    for tr in all_tr:
        tr = {
            'name': ''.join(tr.xpath('./td[1]/text()')).strip(),
            'price': ''.join(tr.xpath('./td[2]/text()')).strip(),
            'unit': ''.join(tr.xpath('./td[3]/text()')).strip(),
            'supermaket': ''.join(tr.xpath('./td[4]/text()')).strip(),
            'time': ''.join(tr.xpath('./td[5]/text()')).strip()
        }
        with open('wood.csv', 'a', encoding='utf_8_sig', newline='') as fp:
            # 'a'为追加模式（添加）
            # utf_8_sig格式导出csv不乱码
            fieldnames = ['name', 'price', 'unit', 'supermaket', 'time']
            writer = csv.DictWriter(fp, fieldnames)
            writer.writerow(tr)
        i += 1
    print('第%s页，爬取%s条数据' % (x, i))
