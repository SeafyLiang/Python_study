import os
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'http://www.saicmg.com/'
response = requests.get(url=url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
ul = soup.find_all(class_='se_tu')[0]
img = ul.find_all(class_='img100')[0:6]
folder_path = "F:/Car/SAIC Motor/mg/"
os.makedirs(folder_path)
for item in img:
    url = 'http://www.saicmg.com/' + item['src']
    r = requests.get(url)
    picture_name = url.replace('http://www.saicmg.com/images/', '')
    with open('F:\\Car\\SAIC Motor\\mg\\' + picture_name, 'wb') as f:
        f.write(r.content)
    f.close()
    print(url)