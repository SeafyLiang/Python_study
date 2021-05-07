import os
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'http://www.roewe.com.cn/htmlinclude/header.html'
response = requests.get(url=url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
Car_Type = ['Car','SUV']
for i in [1, 2]:
    folder_path = "F:/Car/SAIC Motor/roewe/" + Car_Type[i - 1] + "/"
    os.makedirs(folder_path)
    ul = (soup.find_all(class_='clearfix ul' + str(i)))[0]
    img = ul.find_all(name='img')
    for item in img:
        url = 'http://www.roewe.com.cn' + item['src']
        r = requests.get(url)
        picture_name = url.replace('http://www.roewe.com.cn/images/headernav/', '')
        with open('F:\\Car\\SAIC Motor\\roewe\\' + Car_Type[i-1] + "\\" + picture_name, 'wb') as f:
            f.write(r.content)
        f.close()
        print(url)
    print('\n\n')