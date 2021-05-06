import pandas
from pyecharts import Pie

df = pandas.read_csv('comments_douban_ll.csv', header=None, names=['user_name', 'user_url', 'registered_time', 'score', 'date', 'comment_time', 'useful_num', 'comment', 'score1', 'sentiment'])

score_message = df.groupby(['score'])
score_com = score_message['score'].agg(['count'])
score_com.reset_index(inplace=True)
score_com_last = score_com.sort_values('count', ascending=False)

attr = score_com_last['score']
v1 = score_com_last['count']

pie = Pie("全部差评-500条评论评分情况", title_pos='center', title_top=0)
pie.add("", attr, v1, radius=[40, 75], label_text_color=None, is_label_show=True, legend_orient="vertical", legend_pos="left", legend_top="%10")
pie.render('全部差评评分情况.html')