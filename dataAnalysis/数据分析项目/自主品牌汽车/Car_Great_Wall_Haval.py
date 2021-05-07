import os
import requests
from lxml import etree

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'http://www.haval.com.cn/photo/index.shtml'
response = requests.get(url=url, headers=headers)
html = etree.HTML(response.text)
result = html.xpath('//ul[@class="photoCont-list clearfix"]//img/@src')
folder_path = "F:/Car/Great_Wall_Automobile/Haval/"
os.makedirs(folder_path)
for i in range(13):
    if i == 0:
        url = 'http:' + result[i]
    else:
        url = result[i]
    r = requests.get(url)
    picture_name = url[-13:]
    with open('F:\\Car\\Great_Wall_Automobile\\Haval\\' + picture_name, 'wb') as f:
        f.write(r.content)
    f.close()
    print(url)
