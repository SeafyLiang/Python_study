import pandas as pd
from pyecharts import Pie

# 读取数据
# df = pd.read_csv('comment_before.csv', header=None, names=['name', 'userid', 'age', 'gender', 'city', 'text', 'comment', 'commentid', 'praise', 'date'], encoding='utf-8-sig')
df = pd.read_csv('comment_after.csv', header=None, names=['name', 'userid', 'age', 'gender', 'city', 'text', 'comment', 'commentid', 'praise', 'date'], encoding='utf-8-sig')
# 根据评论ID去重
df = df.drop_duplicates('commentid')
# 去除无性别信息的
df = df[df.gender != 0]
df = df[df.gender != 3]

# 分组汇总
gender_message = df.groupby(['gender'])
gender_com = gender_message['gender'].agg(['count'])
gender_com.reset_index(inplace=True)

# 生成饼图
attr = ['男', '女']
v1 = gender_com['count']
# pie = Pie("歌曲发布后评论用户的性别情况", title_pos='center', title_top=0)
# pie.add("", attr, v1, radius=[40, 75], label_text_color=None, is_label_show=True, legend_orient="vertical", legend_pos="left", legend_top="%10")
# pie.render("歌曲发布后评论用户的性别情况.html")
pie = Pie("歌曲被爆抄袭后评论用户的性别情况", title_pos='center', title_top=0)
pie.add("", attr, v1, radius=[40, 75], label_text_color=None, is_label_show=True, legend_orient="vertical", legend_pos="left", legend_top="%10")
pie.render("歌曲被爆抄袭后评论用户的性别情况.html")