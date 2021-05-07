import os
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'https://www.saicmaxus.com/'
response = requests.get(url=url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
ul = soup.find_all(class_='item show clearfix')
Car_Type = ['MPV', 'SUV', 'PICK UP', 'MPV-1', 'MPV-2']
num = 0
for a in ul[:5]:
    num += 1
    folder_path = "F:/Car/SAIC Motor/maxus/" + Car_Type[num - 1] + "/"
    os.makedirs(folder_path)
    img = a.find_all(name='img')
    for item in img:
        url = 'https://www.saicmaxus.com/' + item['src']
        r = requests.get(url)
        picture_name = url.replace('https://www.saicmaxus.com//static/series/', '').replace('https://www.saicmaxus.com//uploads/month_1712/20171229075', '')
        with open('F:\\Car\\SAIC Motor\\maxus\\' + Car_Type[num-1] + "\\" + picture_name, 'wb') as f:
            f.write(r.content)
        f.close()
        print(url)