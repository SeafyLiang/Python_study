from pyecharts import Boxplot
import pandas as pd
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='774110919', port=3306, db='boss_job', charset='utf8mb4')
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
data = [[], [], [], [], [], []]
dom1, dom2, dom3, dom4, dom5, dom6 = data
for i, j in zip(dom['job_experience'], dom['job_salary']):
    j = ((float(j.split('-')[0].replace('k', '')) + float(j.split('-')[1].replace('k', ''))) / 2) * 1000
    if i in ['经验不限']:
        dom1.append(j)
    elif i in ['应届生']:
        dom2.append(j)
    elif i in ['1年以内']:
        dom3.append(j)
    elif i in ['1-3年']:
        dom4.append(j)
    elif i in ['3-5年']:
        dom5.append(j)
    else:
        dom6.append(j)

boxplot = Boxplot("BOSS直聘数据分析岗—工作经验薪水图(元/月)", title_pos='center', title_top='18', width=800, height=400)
x_axis = ['经验不限', '应届生', '1年以内', '1-3年', '3-5年', '5-10年']
y_axis = [dom1, dom2, dom3, dom4, dom5, dom6]
_yaxis = boxplot.prepare_data(y_axis)
boxplot.add("", x_axis, _yaxis)
boxplot.render("BOSS直聘数据分析岗—工作经验薪水图.html")