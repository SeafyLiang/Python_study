from pyecharts import Geo
import pandas as pd
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='774110919', port=3306, db='boss_job', charset='utf8mb4')
cursor = conn.cursor()
sql = "select * from job"
df = pd.read_sql(sql, conn)

city_message = df.groupby(['job_city'])
city_com = city_message['job_city'].agg(['count'])
city_com.reset_index(inplace=True)
city_com_last = city_com.sort_index()

geo = Geo("BOSS直聘数据分析岗—城市分布图", title_pos='center', title_top='0', width=800, height=400, title_color="#fff", background_color="#404a59",)
attr = city_com_last['job_city']
value = city_com_last['count']
geo.add("", attr, value, is_visualmap=True, visual_range=[0, 60], visual_text_color="#fff", symbol_size=15)
geo.render("BOSS直聘数据分析岗—城市分布图.html")
