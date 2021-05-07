import os
import re
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'http://www.changan.com.cn/cache/car_json.js'
response = requests.get(url=url, headers=headers)
res = response.text
result = re.findall('"car_model_photo":"(.*?)","car_model_price_name"', res, re.S)
Car_Type = ['Car', 'SUV', 'MPV']
for i in range(3):
    folder_path = "F:/Car/CHANGAN/" + Car_Type[i] + "/"
    os.makedirs(folder_path)
for j in range(16):
    url = 'http:' + result[j].replace('\\', '')
    r = requests.get(url)
    picture_name = url.replace('http://www.changan.com.cn/uploads/car_model_photo/', '')
    if j < 9:
        with open('F:\\Car\\CHANGAN\\Car\\' + picture_name, 'wb') as f:
            f.write(r.content)
    elif j < 15:
        with open('F:\\Car\\CHANGAN\\SUV\\' + picture_name, 'wb') as f:
            f.write(r.content)
    else:
        with open('F:\\Car\\CHANGAN\\MPV\\' + picture_name, 'wb') as f:
            f.write(r.content)
    f.close()
    print(url)