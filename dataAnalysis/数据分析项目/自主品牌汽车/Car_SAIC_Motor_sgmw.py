import os
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'https://www.sgmw.com.cn/'
response = requests.get(url=url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
ul = soup.find_all(class_='det_box')
Car_Type = ['SUV', 'MPV', 'Car', 'Mini-Car']
num = 0
for i in range(len(ul)):
    num += 1
    folder_path = "F:/Car/SAIC Motor/sgmw/" + Car_Type[num - 1] + "/"
    os.makedirs(folder_path)
    p = ul[i]
    box = p.find_all(class_='itembox')
    for j in range(len(box)):
        g = (box[j].find_all(class_='item_img'))[0]
        item = (g.find_all(name='img'))[0]
        url = 'https://www.sgmw.com.cn/' + item['src']
        r = requests.get(url)
        picture_name = url.replace('https://www.sgmw.com.cn/images/childnav/', '').replace('https://www.sgmw.com.cn/images/', '').replace('https://www.sgmw.com.cn/hy310w/images/310w/', '').replace('510/', '').replace('s3/', '')
        with open('F:\\Car\\SAIC Motor\\sgmw\\' + Car_Type[num - 1] + "\\" + picture_name, 'wb') as f:
            f.write(r.content)
        f.close()
        print(url)



