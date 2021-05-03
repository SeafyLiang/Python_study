from pyecharts import TreeMap
import pandas as pd
import psycopg2

conn = psycopg2.connect(database="lagou_job", user="postgres", password="774110919", host="127.0.0.1", port="5432")
cursor = conn.cursor()
sql = "select * from job"
df = pd.read_sql(sql, conn)

dom1 = []
for i in df['job_tips']:
    type1 = i.split(',')
    for j in range(len(type1)):
        if type1[j] in ['None', '大数据', '金融', '电商', '广告营销', '移动互联网']:
            continue
        else:
            if type1[j] in dom1:
                continue
            else:
                dom1.append(type1[j])
print(dom1)
dom2 = []
for item in dom1:
    num = 0
    for i in df['job_tips']:
        type2 = i.split(',')
        for j in range(len(type2)):
            if type2[j] in ['None', '大数据', '金融', '电商', '广告营销', '移动互联网']:
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

treemap = TreeMap("拉勾网数据挖掘岗—技能图", title_pos='center', title_top='5', width=800, height=400)
treemap.add('数据挖掘技能', dom3, is_label_show=True, label_pos='inside', is_legend_show=False)
treemap.render('拉勾网数据挖掘岗—技能图.html')