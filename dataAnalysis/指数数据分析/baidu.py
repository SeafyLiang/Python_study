import time
import json
import execjs
import datetime
import requests
from urllib.parse import urlencode


def get_data(keywords, startDate, endDate, area):
    """
    获取加密的参数数据
    """
    # data_url = "http://index.baidu.com/api/SearchApi/index?area=0&word=[[%7B%22name%22:%22%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80%22,%22wordType%22:1%7D]]&startDate=2020-10-01&endDate=2020-10-10"
    params = {
        'word': json.dumps([[{'name': keyword, 'wordType': 1}] for keyword in keywords]),
        'startDate': startDate,
        'endDate': endDate,
        'area': area
    }
    data_url = 'http://index.baidu.com/api/SearchApi/index?' + urlencode(params)
    # print(data_url)
    headers = {
        # 复制登录后的cookie
        "Cookie": '你的cookie',
        "Referer": "http://index.baidu.com/v2/main/index.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }

    # 获取data和uniqid
    res = requests.get(url=data_url, headers=headers).json()
    data = res["data"]["userIndexes"][0]["all"]["data"]
    uniqid = res["data"]["uniqid"]

    # 获取js函数中的参数t = "ev-fxk9T8V1lwAL6,51348+.9270-%"
    t_url = "http://index.baidu.com/Interface/ptbk?uniqid={}".format(uniqid)
    rep = requests.get(url=t_url, headers=headers).json()
    t = rep["data"]
    return {"data": data, "t": t}


def get_search_index(word, startDate, endDate, area):
    """
    获取最终数据
    """
    word = word
    startDate = startDate
    endDate = endDate
    # 调用get_data获取data和uniqid
    res = get_data(word, startDate, endDate, area)
    e = res["data"]
    t = res["t"]

    # 读取js文件
    with open('parsing_data_function.js', encoding='utf-8') as f:
        js = f.read()

    # 通过compile命令转成一个js对象
    docjs = execjs.compile(js)

    # 调用function方法,得到指数数值
    res = docjs.call('decrypt', t, e)
    # print(res)
    return res


def get_date_list(begin_date, end_date):
    """
    获取时间列表
    """
    dates = []
    dt = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    date = begin_date[:]
    while date <= end_date:
        dates.append(date)
        dt += datetime.timedelta(days=1)
        date = dt.strftime("%Y-%m-%d")
    return dates


def get_area():
    areas = {"901": "山东", "902": "贵州", "903": "江西", "904": "重庆", "905": "内蒙古", "906": "湖北", "907": "辽宁", "908": "湖南", "909": "福建", "910": "上海", "911": "北京", "912": "广西", "913": "广东", "914": "四川", "915": "云南", "916": "江苏", "917": "浙江", "918": "青海", "919": "宁夏", "920": "河北", "921": "黑龙江", "922": "吉林", "923": "天津", "924": "陕西", "925": "甘肃", "926": "新疆", "927": "河南", "928": "安徽", "929": "山西", "930": "海南", "931": "台湾", "932": "西藏", "933": "香港", "934": "澳门"}
    for value in areas.keys():
        try:
            word = ['王者荣耀']
            time.sleep(1)
            startDate = '2020-10-01'
            endDate = '2020-10-10'
            area = value
            res = get_search_index(word, startDate, endDate, area)
            result = res.split(',')
            dates = get_date_list(startDate, endDate)
            for num, date in zip(result, dates):
                print(areas[value], num, date)
                with open('area.csv', 'a+', encoding='utf-8') as f:
                    f.write(areas[value] + ',' + str(num) + ',' + date + '\n')
        except:
            pass


def get_word():
    words = ['诸葛大力', '张伟', '胡一菲', '吕子乔', '陈美嘉', '赵海棠', '咖喱酱', '曾小贤', '秦羽墨']
    for word in words:
        try:
            time.sleep(2)
            startDate = '2020-10-01'
            endDate = '2020-10-10'
            area = 0
            res = get_search_index(word, startDate, endDate, area)
            result = res.split(',')
            dates = get_date_list(startDate, endDate)
            for num, date in zip(result, dates):
                print(word, num, date)
                with open('word.csv', 'a+', encoding='utf-8') as f:
                    f.write(word + ',' + str(num) + ',' + date + '\n')
        except:
            pass


get_area()
get_word()
