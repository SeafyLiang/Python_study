import os
import re
import requests
import demjson

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'http://www.gwm.com.cn/statics/gwm-cn/js/carModel.js'
response = requests.get(url=url, headers=headers)
res = response.text[45:-3]
message = res.replace('\r','').replace('\n','').replace('\t','')
result = re.findall('(.*?);_CIACarTypeAttributeSet', message)
data = demjson.decode(result[0])
folder_path = "F:/Car/Great_Wall_Automobile/Great_Wall/"
os.makedirs(folder_path)
for item in data:
    try:
        url = 'http://www.gwm.com.cn' + item['Pics']['F']
    except:
        continue
    r = requests.get(url)
    picture_name = url[-20:]
    with open('F:\\Car\\Great_Wall_Automobile\\Great_Wall\\' + picture_name, 'wb') as f:
        f.write(r.content)
    f.close()
    print(url)
