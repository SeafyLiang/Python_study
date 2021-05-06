import pandas as pd
from pyecharts import Bar

# 读取数据
# df = pd.read_csv('comment_before.csv', header=None, names=['name', 'userid', 'age', 'gender', 'city', 'text', 'comment', 'commentid', 'praise', 'date'], encoding='utf-8-sig')
df = pd.read_csv('comment_after.csv', header=None, names=['name', 'userid', 'age', 'gender', 'city', 'text', 'comment', 'commentid', 'praise', 'date'], encoding='utf-8-sig')
# 根据评论ID去重
df = df.drop_duplicates('commentid')
# 去除无年龄信息的
df = df[df.age != 0]

# 分组汇总
age_message = df.groupby(['age'])
age_com = age_message['age'].agg(['count'])
age_com.reset_index(inplace=True)

# 生成柱状图
attr = age_com['age']
v1 = age_com['count']
# bar = Bar("歌曲发布后评论用户的年龄分布", title_pos='center', title_top='18', width=800, height=400)
# bar.add("", attr, v1, is_stack=True, is_label_show=False)
# bar.render("歌曲发布后评论用户的年龄分布.html")
bar = Bar("歌曲被爆抄袭后评论用户的年龄分布", title_pos='center', title_top='18', width=800, height=400)
bar.add("", attr, v1, is_stack=True, is_label_show=False)
bar.render("歌曲被爆抄袭后评论用户的年龄分布.html")