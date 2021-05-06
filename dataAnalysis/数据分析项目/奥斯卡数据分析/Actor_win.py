import pandas
from pyecharts import Bar

df1 = pandas.read_csv('Best_Actor_LR.csv', header=None, names=['year', 'win', 'nomination'], encoding='gbk')
df2 = pandas.read_csv('Best_Actor_SR.csv', header=None, names=['year', 'win', 'nomination'], encoding='gbk')
df = pandas.concat([df1, df2])

win_message = df.groupby(['win'])
win_com = win_message['win'].agg(['count'])
win_com.reset_index(inplace=True)
win_com_last = win_com.sort_index()
win_com = win_com.sort_values('count', ascending=False)[0:15]

attr = win_com['win']
v1 = win_com['count']

bar = Bar("奥斯卡男演员-获奖统计", title_pos='center', title_top='18', width=800, height=400)
bar.add("", attr, v1, is_stack=True, is_label_show=True, xaxis_rotate=30, yaxis_force_interval=1, yaxis_max=4)
bar.render("奥斯卡男演员-获奖统计.html")