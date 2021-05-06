import pandas
from pyecharts import Line

df = pandas.read_csv('comments_douban_al.csv', header=None, names=['user_name', 'user_url', 'registered_time', 'score', 'date', 'comment_time', 'useful_num', 'comment', 'score1', 'sentiment'])
date_message = df.groupby(['date'])
date_com = date_message['date'].agg(['count'])
date_com.reset_index(inplace=True)

attr = date_com['date']
v1 = date_com['count']
line = Line("全部短评-500条评论日期分布", title_pos='center', title_top='18', width=800, height=400)
line.add("", attr, v1, xaxis_interval=2, is_smooth=True, is_fill=True, area_color="#000", is_xaxislabel_align=True, xaxis_min="dataMin", area_opacity=0.3, mark_point=["max"], mark_point_symbol="pin", mark_point_symbolsize=45)
line.render("全部短评日期分布.html")