from wordcloud import WordCloud, ImageColorGenerator
from pyecharts import Line, Bar, Geo
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import jieba

# 设置列名与数据对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
# 显示10行
pd.set_option('display.max_rows', 10)
# 读取数据
df = pd.read_csv('subway.csv', header=None, names=['city', 'line', 'station'], encoding='gbk')
# 各个城市地铁线路情况
df_line = df.groupby(['city', 'line']).count().reset_index()
print(df_line)


def create_map(df):
    # 绘制地图
    value = [i for i in df['line']]
    attr = [i for i in df['city']]
    geo = Geo("已开通地铁城市分布情况", title_pos='center', title_top='0', width=800, height=400, title_color="#fff", background_color="#404a59", )
    geo.add("", attr, value, is_visualmap=True, visual_range=[0, 25], visual_text_color="#fff", symbol_size=15)
    geo.render("已开通地铁城市分布情况.html")


def create_line(df):
    """
    生成城市地铁线路数量分布情况
    """
    title_len = df['line']
    bins = [0, 5, 10, 15, 20, 25]
    level = ['0-5', '5-10', '10-15', '15-20', '20以上']
    len_stage = pd.cut(title_len, bins=bins, labels=level).value_counts().sort_index()
    # 生成柱状图
    attr = len_stage.index
    v1 = len_stage.values
    bar = Bar("各城市地铁线路数量分布", title_pos='center', title_top='18', width=800, height=400)
    bar.add("", attr, v1, is_stack=True, is_label_show=True)
    bar.render("各城市地铁线路数量分布.html")


# 各个城市地铁线路数
df_city = df_line.groupby(['city']).count().reset_index().sort_values(by='line', ascending=False)
print(df_city)
create_map(df_city)
create_line(df_city)

# 哪个城市哪条线路地铁站最多
print(df_line.sort_values(by='station', ascending=False))

# 去除重复换乘站的地铁数据
df_station = df.groupby(['city', 'station']).count().reset_index()
print(df_station)

# 统计每个城市包含地铁站数(已去除重复换乘站)
print(df_station.groupby(['city']).count().reset_index().sort_values(by='station', ascending=False))


def create_wordcloud(df):
    """
    生成地铁名词云
    """
    # 分词
    text = ''
    for line in df['station']:
        text += ' '.join(jieba.cut(line, cut_all=False))
        text += ' '
    backgroud_Image = plt.imread('rocket.jpg')
    wc = WordCloud(
        background_color='white',
        mask=backgroud_Image,
        font_path='C:\Windows\Fonts\华康俪金黑W8.TTF',
        max_words=1000,
        max_font_size=150,
        min_font_size=15,
        prefer_horizontal=1,
        random_state=50,
    )
    wc.generate_from_text(text)
    img_colors = ImageColorGenerator(backgroud_Image)
    wc.recolor(color_func=img_colors)
    # 看看词频高的有哪些
    process_word = WordCloud.process_text(wc, text)
    sort = sorted(process_word.items(), key=lambda e: e[1], reverse=True)
    print(sort[:50])
    plt.imshow(wc)
    plt.axis('off')
    wc.to_file("地铁名词云.jpg")
    print('生成词云成功!')


# create_wordcloud(df_station)

words = []
for line in df['station']:
    for i in line:
        # 将字符串输出一个个中文
        words.append(i)


def all_np(arr):
    """
    统计单字频率
    """
    arr = np.array(arr)
    key = np.unique(arr)
    result = {}
    for k in key:
        mask = (arr == k)
        arr_new = arr[mask]
        v = arr_new.size
        result[k] = v
    return result


def create_word(word_message):
    """
    生成柱状图
    """
    attr = [j[0] for j in word_message]
    v1 = [j[1] for j in word_message]
    bar = Bar("中国地铁站最爱用的字", title_pos='center', title_top='18', width=800, height=400)
    bar.add("", attr, v1, is_stack=True, is_label_show=True)
    bar.render("中国地铁站最爱用的字.html")


word = all_np(words)
word_message = sorted(word.items(), key=lambda x: x[1], reverse=True)[:10]
create_word(word_message)

# 选取上海的地铁站
df1 = df_station[df_station['city'] == '上海']
print(df1)
# 选取上海地铁站名字包含路的数据
df2 = df1[df1['station'].str.contains('路')]
print(df2)

# 选取武汉的地铁站
df1 = df_station[df_station['city'] == '武汉']
print(df1)
# 选取武汉地铁站名字包含家的数据
df2 = df1[df1['station'].str.contains('家')]
print(df2)

# 选取重庆的地铁站
df1 = df_station[df_station['city'] == '重庆']
print(df1)
# 选取重庆地铁站名字包含家的数据
df2 = df1[df1['station'].str.contains('家')]
print(df2)


def create_door(door):
    """
    生成柱状图
    """
    attr = [j for j in door['city'][:3]]
    v1 = [j for j in door['line'][:3]]
    bar = Bar("地铁站最爱用“门”命名的城市", title_pos='center', title_top='18', width=800, height=400)
    bar.add("", attr, v1, is_stack=True, is_label_show=True, yaxis_max=40)
    bar.render("地铁站最爱用门命名的城市.html")


# 选取地铁站名字包含门的数据
df1 = df_station[df_station['station'].str.contains('门')]
# 对数据进行分组计数
df2 = df1.groupby(['city']).count().reset_index().sort_values(by='line', ascending=False)
print(df2)
create_door(df2)


# 选取北京的地铁站
df1 = df_station[df_station['city'] == '北京']
print(df1)
# 选取北京地铁站名字包含门的数据
df2 = df1[df1['station'].str.contains('门')]
print(df2)

# 选取南京的地铁站
df1 = df_station[df_station['city'] == '南京']
# 选取南京地铁站名字包含门的数据
df2 = df1[df1['station'].str.contains('门')]
print(df2)

# 选取西安的地铁站
df1 = df_station[df_station['city'] == '西安']
# 选取西安地铁站名字包含门的数据
df2 = df1[df1['station'].str.contains('门')]
print(df2)