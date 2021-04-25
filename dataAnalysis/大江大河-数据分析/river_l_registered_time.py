import pandas
from pyecharts import Bar

df = pandas.read_csv('comments_douban_ll.csv', header=None, names=['user_name', 'user_url', 'registered_time', 'score', 'date', 'comment_time', 'useful_num', 'comment', 'score1', 'sentiment'])

years = []
for i in df['registered_time']:
    year = i.split('/')[0]
    if year == 'unknow':
        years.append(int('2019'))
    else:
        years.append(int(year))
df['years'] = years

date_message = df.groupby(['years'])
date_com = date_message['years'].agg(['count'])
date_com.reset_index(inplace=True)

attr = date_com['years']
v1 = date_com['count']

bar = Bar("全部差评-用户注册时间分布", title_pos='center', title_top='18', width=800, height=400)
bar.add("", attr, v1, is_stack=True, is_label_show=True)
bar.render("全部差评用户注册时间分布.html")