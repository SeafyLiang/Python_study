from pyecharts import Boxplot
import pandas as pd
import psycopg2

conn = psycopg2.connect(database="lagou_job", user="postgres", password="774110919", host="127.0.0.1", port="5432")
cursor = conn.cursor()
sql = "select * from job"
df = pd.read_sql(sql, conn)
dom22 = []
for i in df['job_experience']:
    if i in dom22:
        continue
    else:
        dom22.append(i)

dom = df[['job_experience', 'job_salary']]
data = [[], [], [], [], [], [], []]
dom1, dom2, dom3, dom4, dom5, dom6, dom7 = data
for i, j in zip(dom['job_experience'], dom['job_salary']):
    j = ((float(j.split('-')[0].replace('k', '').replace('K', '')) + float(j.split('-')[1].replace('k', '').replace('K', ''))) / 2) * 1000
    if i in ['不限']:
        dom1.append(j)
    elif i in ['应届毕业生']:
        dom2.append(j)
    elif i in ['1-3年']:
        dom4.append(j)
    elif i in ['3-5年']:
        dom5.append(j)
    else:
        dom6.append(j)

boxplot = Boxplot("拉勾网数据挖掘岗—工作经验薪水图(元/月)", title_pos='center', title_top='18', width=800, height=400)
x_axis = ['经验不限', '应届生', '1-3年', '3-5年', '5-10年']
y_axis = [dom1, dom2, dom4, dom5, dom6]
_yaxis = boxplot.prepare_data(y_axis)
boxplot.add("", x_axis, _yaxis)
boxplot.render("拉勾网数据挖掘岗—工作经验薪水图.html")