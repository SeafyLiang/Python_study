from pyecharts import Boxplot
import pandas as pd
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='774110919', port=3306, db='lagou_job', charset='utf8mb4')
cursor = conn.cursor()
sql = "select * from job"
df = pd.read_sql(sql, conn)
dom22 = []
for i in df['company_status']:
    if i in dom22:
        continue
    else:
        dom22.append(i)

dom = df[['company_status', 'job_salary']]
data = [[], [], [], [], [], [], [], []]
dom1, dom2, dom3, dom4, dom5, dom6, dom7, dom8 = data
for i, j in zip(dom['company_status'], dom['job_salary']):
    j = ((float(j.split('-')[0].replace('k', '').replace('K', '')) + float(j.split('-')[1].replace('k', '').replace('K', ''))) / 2) * 1000
    if i in ['天使轮']:
        dom1.append(j)
    elif i in ['A轮']:
        dom2.append(j)
    elif i in ['B轮']:
        dom3.append(j)
    elif i in ['C轮']:
        dom4.append(j)
    elif i in ['D轮及以上']:
        dom5.append(j)
    elif i in ['上市公司']:
        dom6.append(j)
    elif i in ['未融资']:
        dom7.append(j)
    else:
        dom8.append(j)

boxplot = Boxplot("拉勾网数据分析岗—公司状态薪水图(元/月)", title_pos='center', title_top='18', width=800, height=400)
x_axis = ['天使轮', 'A轮', 'B轮', 'C轮', 'D轮及以上', '上市公司', '未融资', '不需要融资']
y_axis = [dom1, dom2, dom3, dom4, dom5, dom6, dom7, dom8]
_yaxis = boxplot.prepare_data(y_axis)
boxplot.add("", x_axis, _yaxis)
boxplot.render("拉勾网数据分析岗—公司状态薪水图.html")