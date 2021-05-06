import pandas
from pyecharts import Pie

df = pandas.read_csv('comments_douban_al.csv', header=None, names=['user_name', 'user_url', 'registered_time', 'score', 'date', 'comment_time', 'useful_num', 'comment', 'score1', 'sentiment'])

sentiment_message = df.groupby(['sentiment'])
sentiment_com = sentiment_message['sentiment'].agg(['count'])
sentiment_com.reset_index(inplace=True)
sentiment_com_last = sentiment_com.sort_values('count', ascending=False)

attr = sentiment_com_last['sentiment']
v1 = sentiment_com_last['count']

pie = Pie("全部短评-500条评论情感分析情况", title_pos='center', title_top=0)
pie.add("", [2, -2, 1], v1, radius=[40, 75], label_text_color=None, is_label_show=True, legend_orient="vertical", legend_pos="left", legend_top="%10")
pie.render('全部短评情感分析情况.html')