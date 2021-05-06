from pyecharts import TreeMap
import pandas as pd
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='774110919', port=3306, db='lagou_job', charset='utf8mb4')
cursor = conn.cursor()
sql = "select * from job"
df = pd.read_sql(sql, conn)

dom1 = []
for i in df['job_tips']:
    type1 = i.split(',')
    for j in range(len(type1)):
        if type1[j] in ['None', '大数据', '移动互联网', '金融', '电商', '商业', '游戏', '广告营销', '互联网金融']:
            continue
        else:
            if type1[j] in dom1:
                continue
            else:
                dom1.append(type1[j])

dom2 = []
for item in dom1:
    num = 0
    for i in df['job_tips']:
        type2 = i.split(',')
        for j in range(len(type2)):
            if type2[j] in ['None', '大数据', '移动互联网', '金融', '电商', '商业', '游戏', '广告营销', '互联网金融']:
                continue
            else:
                if type2[j] == item:
                    num += 1
                else:
                    continue
    dom2.append(num)


def message():
    for k in range(len(dom2)):
        data = {}
        data['name'] = dom1[k] + ' ' + str(dom2[k])
        data['value'] = dom2[k]
        yield data


data1 = message()
dom3 = []
for item in data1:
    dom3.append(item)

treemap = TreeMap("拉勾网数据分析岗—技能图", title_pos='center', title_top='5', width=800, height=400)
treemap.add('数据分析技能', dom3, is_label_show=True, label_pos='inside', is_legend_show=False)
treemap.render('拉勾网数据分析岗—技能图.html')