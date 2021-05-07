import re
import os
import urllib
import requests
from lxml import etree

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'http://www.chery.cn/'
response = requests.get(url=url, headers=headers)
html = etree.HTML(response.text)
result = html.xpath('//div[@class="wrapper"]//img/@src')
Car_Type = ['Car', 'SUV']
for i in range(2):
    folder_path = "F:/Car/Chery/" + Car_Type[i] + "/"
    os.makedirs(folder_path)
for i in range(len(result)):
    url_handle = 'http://www.chery.cn' + result[i]
    cn_name = re.findall('\d/(.*?).png', url_handle)
    name_second = urllib.parse.quote(cn_name[0])
    name_first = result[i].replace(cn_name[0], '').replace('.png', '')
    url = 'http://www.chery.cn' + name_first + name_second + '.png'
    r = requests.get(url)
    picture_name = url.replace('http://www.chery.cn/media/', '').replace('/', '')
    if i < 6:
        with open('F:\\Car\\Chery\\SUV\\' + picture_name, 'wb') as f:
            f.write(r.content)
    else:
        with open('F:\\Car\\Chery\\Car\\' + picture_name, 'wb') as f:
            f.write(r.content)
    f.close()
    print(url)

