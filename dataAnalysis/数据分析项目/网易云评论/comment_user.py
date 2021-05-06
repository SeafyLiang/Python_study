import pandas as pd

# 读取数据
df = pd.read_csv('comment_after.csv', header=None, names=['name', 'userid', 'age', 'gender', 'city', 'text', 'comment', 'commentid', 'praise', 'date'], encoding='utf-8-sig')
# 根据评论ID去重
df = df.drop_duplicates('commentid')
# 分组汇总
user_message = df.groupby(['userid'])
user_com = user_message['userid'].agg(['count'])
user_com.reset_index(inplace=True)
user_com_last = user_com.sort_values('count', ascending=False)[0:10]
print(user_com_last)