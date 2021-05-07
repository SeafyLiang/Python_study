import os
import requests
from lxml import etree

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'http://www.dfac.com/'
response = requests.get(url=url, headers=headers)
html = etree.HTML(response.text)
Car_Type = ['', 'Light_truck', 'Engineering_truck', 'Light_guest', 'Coach', '', 'School_bus', 'Pick-up_Truck']
for i in range(8):
    if i == 0:
        pass
    elif i == 5:
        pass
    else:
        folder_path = "F:/Car/DFAC/" + Car_Type[i] + "/"
        os.makedirs(folder_path)
        result = html.xpath('//div[@class="Procon pc' + str(i) + '"]//img/@src')
        for j in range(len(result)):
            url = 'http://www.dfac.com' + result[j]
            r = requests.get(url)
            picture_name = url.replace('http://www.dfac.com/uploadfiles/', '').replace('2018/10/', '').replace('2018/09/', '')
            with open('F:\\Car\\DFAC\\' + Car_Type[i] + '\\' + picture_name, 'wb') as f:
                f.write(r.content)
            f.close()
            print(url)

