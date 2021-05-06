import json
import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


def get_message(ID, cityname, name):
    """
    地铁线路信息获取
    """
    url = 'http://map.amap.com/service/subway?_1555502190153&srhdata=' + ID + '_drw_' + cityname + '.json'
    response = requests.get(url=url, headers=headers)
    html = response.text
    result = json.loads(html)
    for i in result['l']:
        for j in i['st']:
            # 判断是否含有地铁分线
            if len(i['la']) > 0:
                print(name, i['ln'] + '(' + i['la'] + ')', j['n'])
                with open('subway.csv', 'a+', encoding='gbk') as f:
                    f.write(name + ',' + i['ln'] + '(' + i['la'] + ')' + ',' + j['n'] + '\n')
            else:
                print(name, i['ln'], j['n'])
                with open('subway.csv', 'a+', encoding='gbk') as f:
                    f.write(name + ',' + i['ln'] + ',' + j['n'] + '\n')


def get_city():
    """
    城市信息获取
    """
    url = 'http://map.amap.com/subway/index.html?&1100'
    response = requests.get(url=url, headers=headers)
    html = response.text
    # 编码
    html = html.encode('ISO-8859-1')
    html = html.decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    # 城市列表
    res1 = soup.find_all(class_="city-list fl")[0]
    res2 = soup.find_all(class_="more-city-list")[0]
    for i in res1.find_all('a'):
        # 城市ID值
        ID = i['id']
        # 城市拼音名
        cityname = i['cityname']
        # 城市名
        name = i.get_text()
        get_message(ID, cityname, name)
    for i in res2.find_all('a'):
        # 城市ID值
        ID = i['id']
        # 城市拼音名
        cityname = i['cityname']
        # 城市名
        name = i.get_text()
        get_message(ID, cityname, name)


if __name__ == '__main__':
    get_city()
