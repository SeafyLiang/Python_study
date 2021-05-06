import pandas
from pyecharts import Line

df = pandas.read_csv('comments_douban_ll.csv', header=None, names=['user_name', 'user_url', 'registered_time', 'score', 'date', 'comment_time', 'useful_num', 'comment', 'score1', 'sentiment'])
hours = []
for i in df['comment_time']:
    hour = i.split(':')[0]
    hours.append(int(hour))
df['hours'] = hours

date_message = df.groupby(['hours'])
date_com = date_message['hours'].agg(['count'])
date_com.reset_index(inplace=True)

attr = date_com['hours']
v1 = date_com['count']
line = Line("全部差评-500条评论时间分布", title_pos='center', title_top='18', width=800, height=400)
line.add("", attr, v1, xaxis_interval=0, is_smooth=True, xaxis_max=23, is_fill=True, area_color="#000", is_xaxislabel_align=True, area_opacity=0.3, mark_point=["max"], mark_point_symbol="pin", mark_point_symbolsize=45)
line.render("全部差评时间分布.html")