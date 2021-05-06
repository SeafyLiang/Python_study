import pandas as pd
from pyecharts import Line

# 读取数据
# df = pd.read_csv('comment_before.csv', header=None, names=['name', 'userid', 'age', 'gender', 'city', 'text', 'comment', 'commentid', 'praise', 'date'], encoding='utf-8-sig')
df = pd.read_csv('comment_after.csv', header=None, names=['name', 'userid', 'age', 'gender', 'city', 'text', 'comment', 'commentid', 'praise', 'date'], encoding='utf-8-sig')
# 根据评论ID去重
df = df.drop_duplicates('commentid')
# 获取时间
df['time'] = [int(i.split(' ')[1].split(':')[0]) for i in df['date']]

# 分组汇总
date_message = df.groupby(['time'])
date_com = date_message['time'].agg(['count'])
date_com.reset_index(inplace=True)

# 绘制走势图
attr = date_com['time']
v1 = date_com['count']
# line = Line("歌曲发布后-评论的时间分布", title_pos='center', title_top='18', width=800, height=400)
# line.add("", attr, v1, is_smooth=True, is_fill=True, area_color="#000", is_xaxislabel_align=True, xaxis_min="dataMin", area_opacity=0.3, mark_point=["max"], mark_point_symbol="pin", mark_point_symbolsize=55)
# line.render("歌曲发布后-评论的时间分布.html")
line = Line("歌曲被爆抄袭后-评论的时间分布", title_pos='center', title_top='18', width=800, height=400)
line.add("", attr, v1, is_smooth=True, is_fill=True, area_color="#000", is_xaxislabel_align=True, xaxis_min="dataMin", area_opacity=0.3, mark_point=["max"], mark_point_symbol="pin", mark_point_symbolsize=55)
line.render("歌曲被爆抄袭后-评论的时间分布.html")
