import os
import requests
from lxml import etree

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'http://www.fawcar.com.cn/products/public/car_bt.html'
response = requests.get(url=url, headers=headers)
html = etree.HTML(response.text)
result = html.xpath('//dl[@class="imglist"]//img/@src')
Car_Type = ['Car', 'SUV']
for i in range(2):
    folder_path = "F:/Car/FAW/Bt/" + Car_Type[i] + "/"
    os.makedirs(folder_path)
for j in range(11):
    url = 'http://www.fawcar.com.cn/products/' + result[j]
    r = requests.get(url)
    picture_name = url.replace('http://www.fawcar.com.cn/products/images/', '')
    if j in [0, 3, 4, 5, 6, 10]:
        with open('F:\\Car\\FAW\\Bt\\Car\\' + picture_name, 'wb') as f:
            f.write(r.content)
    else:
        with open('F:\\Car\\FAW\\Bt\\SUV\\' + picture_name, 'wb') as f:
            f.write(r.content)
    f.close()
    print(url)

