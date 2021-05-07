import os
import requests
from lxml import etree

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
for j in ['car', 'suv', 'mpv']:
    folder_path = "F:/Car/Gac_Motor/" + j + "/"
    os.makedirs(folder_path)
    url = 'https://www.gacmotor.com/Home/Models/' + j + '.html'
    response = requests.get(url=url, headers=headers, verify=False)
    html = etree.HTML(response.text)
    result = html.xpath('//div[@class="moNav"]//img/@src')
    ids = list(set(result))
    for i in range(len(ids)):
        url = 'https://www.gacmotor.com' + ids[i]
        r = requests.get(url, headers=headers, verify=False)
        picture_name = url.replace('https://www.gacmotor.com/Public/Home/img/', '')
        with open('F:\\Car\\Gac_Motor\\' + j + '\\' + picture_name, 'wb') as f:
            f.write(r.content)
        f.close()
        print(url)
