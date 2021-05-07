import os
import requests
from lxml import etree

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'http://www.jac.com.cn/jacweb/procenter/'
response = requests.get(url=url, headers=headers)
html = etree.HTML(response.text)
Car_Type = ['Refine', 'MPV', 'Light_truck', 'Heavy_truck']
for i in range(4):
    folder_path = "F:/Car/JAC/" + Car_Type[i] + "/"
    os.makedirs(folder_path)
ID = ['98', '74', '144', '75', '76', '77', '78', '985']
for i in ID:
    if i in ['98', '74']:
        result = html.xpath('//div[contains(@class, "brandWordList") and @id="floor' + i + '"]//div[@class="brandWordLeft"]//img/@src')
        for j in range(len(result)):
            url = 'http://www.jac.com.cn' + result[j]
            r = requests.get(url)
            picture_name = url.replace('http://www.jac.com.cn/u/cms/www/', '').replace('/', '')
            with open('F:\\Car\\JAC\\Refine\\' + picture_name, 'wb') as f:
                f.write(r.content)
            f.close()
            print(url)
    elif i == '144':
        result = html.xpath('//div[contains(@class, "brandWordList") and @id="floor' + i + '"]//div[@class="brandWordLeft"]//img/@src')
        for j in range(len(result)):
            url = 'http://www.jac.com.cn' + result[j]
            r = requests.get(url)
            picture_name = url.replace('http://www.jac.com.cn/u/cms/www/', '').replace('/', '')
            with open('F:\\Car\\JAC\\MPV\\' + picture_name, 'wb') as f:
                f.write(r.content)
            f.close()
            print(url)
    elif i in ['75', '76', '77']:
        result = html.xpath('//div[contains(@class, "brandWordList") and @id="floor' + i + '"]//div[@class="brandWordLeft"]//img/@src')
        for j in range(len(result)):
            url = 'http://www.jac.com.cn' + result[j]
            r = requests.get(url)
            picture_name = url.replace('http://www.jac.com.cn/u/cms/www/', '').replace('/', '')
            with open('F:\\Car\\JAC\\Light_truck\\' + picture_name, 'wb') as f:
                f.write(r.content)
            f.close()
            print(url)
    else:
        result = html.xpath('//div[contains(@class, "brandWordList") and @id="floor' + i + '"]//div[@class="brandWordLeft"]//img/@src')
        for j in range(len(result)):
            url = 'http://www.jac.com.cn' + result[j]
            r = requests.get(url)
            picture_name = url.replace('http://www.jac.com.cn/u/cms/www/', '').replace('/', '')
            with open('F:\\Car\\JAC\\Heavy_truck\\' + picture_name, 'wb') as f:
                f.write(r.content)
            f.close()
            print(url)
