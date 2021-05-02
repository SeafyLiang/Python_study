from pyecharts import Boxplot
import pandas as pd
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='774110919', port=3306, db='lagou_job', charset='utf8mb4')
cursor = conn.cursor()
sql = "select * from job"
df = pd.read_sql(sql, conn)
dom22 = []
for i in df['job_education']:
    if i in dom22:
        continue
    else:
        dom22.append(i)

dom = df[['job_education', 'job_salary']]
data = [[], [], [], [], []]
dom1, dom2, dom3, dom4, dom5 = data
for i, j in zip(dom['job_education'], dom['job_salary']):
    j = ((float(j.split('-')[0].replace('k', '').replace('K', '')) + float(j.split('-')[1].replace('k', '').replace('K', ''))) / 2) * 1000
    if i in ['不限']:
        dom1.append(j)
    elif i in ['大专']:
        dom2.append(j)
    elif i in ['本科']:
        dom3.append(j)
    else:
        dom4.append(j)

boxplot = Boxplot("拉勾网数据分析岗—学历薪水图(元/月)", title_pos='center', title_top='18', width=800, height=400)
x_axis = ['学历不限', '大专', '本科', '硕士']
y_axis = [dom1, dom2, dom3, dom4]
_yaxis = boxplot.prepare_data(y_axis)
boxplot.add("", x_axis, _yaxis)
boxplot.render("拉勾网数据分析岗—学历薪水图.html")
