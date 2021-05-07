import os
import requests
from lxml import etree

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'http://www.faw-hongqi.com.cn/'
response = requests.get(url=url, headers=headers)
html = etree.HTML(response.text)
result = html.xpath('//div[@class="logo_t logo_t1"]//img/@src')
folder_path = "F:/Car/FAW/Hongqi/"
os.makedirs(folder_path)
for i in range(len(result)):
    url = 'http://www.faw-hongqi.com.cn/' + result[i]
    r = requests.get(url)
    picture_name = url.replace('http://www.faw-hongqi.com.cn//pcs/images/top_', '')
    with open('F:\\Car\\FAW\\Hongqi\\' + picture_name, 'wb') as f:
        f.write(r.content)
    f.close()
    print(url)