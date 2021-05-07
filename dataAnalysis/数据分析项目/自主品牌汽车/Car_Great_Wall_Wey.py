import os
import requests
from lxml import etree

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'https://www.wey.com/'
response = requests.get(url=url, headers=headers)
html = etree.HTML(response.text)
result = html.xpath('//div[@class="new-car-box col-xs-12 col-sm-6 col-lg-3"]//img/@src')
folder_path = "F:/Car/Great_Wall_Automobile/Wey/"
os.makedirs(folder_path)
for i in range(len(result)):
    url = 'https://www.wey.com/' + result[i]
    r = requests.get(url)
    picture_name = url.replace('https://www.wey.com/home/img/home/', '')
    with open('F:\\Car\\Great_Wall_Automobile\\Wey\\' + picture_name, 'wb') as f:
        f.write(r.content)
    f.close()
    print(url)