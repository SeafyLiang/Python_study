import os
import json
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'http://www.baicmotorsales.com/jeesite/web/car/queryCarSeries'
response = requests.get(url=url, headers=headers)
data = json.loads(response.text)
Car_Type = ['SUV', 'Car', 'ORV']
Car = ['s', 'j', 'y']
for i in range(3):
    folder_path = "F:/Car/BAIC_Motor/" + Car_Type[i] + "/"
    os.makedirs(folder_path)
    str = Car[i] + 'list'
    for item in data['body'][str]:
        url = 'http://www.baicmotorsales.com' + item.get('modelPicPc')
        r = requests.get(url)
        picture_name = url.replace('http://www.baicmotorsales.com/upload/userfiles/1/files/car/contrastCarModel/', '').replace('2018/05/', '').replace('2018/09/', '')
        with open('F:\\Car\\BAIC_Motor\\' + Car_Type[i] + '\\' + picture_name, 'wb') as f:
            f.write(r.content)
        f.close()
        print(url)