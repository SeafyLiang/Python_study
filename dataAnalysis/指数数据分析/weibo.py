import re
import time
import json
import requests
import datetime


# 请求头信息
headers = """accept: application/json
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
content-length: 50
content-type: application/x-www-form-urlencoded
cookie: 你的cookie
origin: https://data.weibo.com
referer: https://data.weibo.com/index/newindex?visit_type=trend&wid=1011224685661
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1
x-requested-with: XMLHttpRequest"""

# 将请求头字符串转化为字典
headers = dict([line.split(": ",1) for line in headers.split("\n")])
print(headers)

# 数据接口
url = 'https://data.weibo.com/index/ajax/newindex/getchartdata'


# 获取时间列表
def get_date_list(begin_date, end_date):
    dates = []
    dt = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    date = begin_date[:]
    while date <= end_date:
        dates.append(date)
        dt += datetime.timedelta(days=1)
        date = dt.strftime("%Y-%m-%d")
    return dates


# 相关信息
names = ['汤唯', '朱亚文', '邓家佳', '乔振宇', '王学圻', '张艺兴', '俞灏明', '吴越', '梁冠华', '李昕亮', '苏可', '孙骁骁', '赵韩樱子', '孙耀琦', '魏巍']


# 获取微指数数据
for name in names:
    try:
        # 获取关键词ID
        url_id = 'https://data.weibo.com/index/ajax/newindex/searchword'
        data_id = {
            'word': name
        }
        html_id = requests.post(url=url_id, data=data_id, headers=headers)
        pattern = re.compile(r'li wid=\\\"(.*?)\\\" word')
        id = pattern.findall(html_id.text)[0]


        # 接口参数
        data = {
            'wid': id,
            'dateGroup': '1month'
        }
        time.sleep(2)
        # 请求数据
        html = requests.post(url=url, data=data, headers=headers)
        result = json.loads(html.text)
        # 处理数据
        if result['data']:
            values = result['data'][0]['trend']['s']
            startDate = '2019-01-01'
            endDate = '2020-01-01'
            dates = result['data'][0]['trend']['x']
            # 保存数据
            for value, date in zip(values, dates):
                print(name, value, date)
                with open('weibo.csv', 'a+', encoding='utf-8') as f:
                    f.write(name + ',' + str(value) + ',' + date + '\n')
    except:
        pass