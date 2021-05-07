import os
import requests
from lxml import etree

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'http://www.geely.com/?mz_ca=2071413&mz_sp=7D3ws&mz_kw=8398784&mz_sb=1'
response = requests.get(url=url, headers=headers)
res = response.text
html = etree.HTML(response.text)
result = html.xpath('//div[@class="car"]/img/@src')
Car_Type = ['Car', 'SUV']
for i in range(2):
    folder_path = "F:/Car/GEELY_AUTO/" + Car_Type[i] + "/"
    os.makedirs(folder_path)
for j in range(17):
    url = result[j]
    r = requests.get(url)
    picture_name = url.replace('https://dm30webimages.geely.com/GeelyOfficial/Files/Car/CarType/', '')
    if 0 < j < 4 or 6 < j < 12 or j == 16:
        with open('F:\\Car\\GEELY_AUTO\\Car\\' + picture_name, 'wb') as f:
            f.write(r.content)
    elif 3 < j < 7 or 11 < j < 16:
        with open('F:\\Car\\GEELY_AUTO\\SUV\\' + picture_name, 'wb') as f:
            f.write(r.content)
    else:
        continue
    f.close()
    print(url)