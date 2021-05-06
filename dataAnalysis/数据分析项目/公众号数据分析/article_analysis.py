from wordcloud import WordCloud, ImageColorGenerator
from pyecharts import Line, Bar
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import jieba

# 设置列名与数据对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
# 显示4列
pd.set_option('display.max_columns', 4)
# 显示10行
pd.set_option('display.max_rows', 10)
# 设置显示宽度为200,这样就不会在IDE中换行了
pd.set_option('display.width', 200)

# 读取数据并清洗
df = pd.read_csv('article.csv', header=None, names=['title', 'digest', 'article_url', 'date'], encoding='gbk')
# 将时间戳转换为北京时间
df['date'] = pd.to_datetime(df.date.values, unit='s', utc=True).tz_convert('Asia/Shanghai')
df_date = df['date'].astype(str).str.split(' ', expand=True)
# 获取年份及月份数据
df_year_month = df_date[0].astype(str).str.split('-', expand=True)
df['year'] = df_year_month[0]
df['month'] = df_year_month[1]
# 获取小时数据
df2 = df_date[1].astype(str).str.split(':', expand=True)
df['hour'] = df2[0]
# 获取标题长度
df['title_len'] = df['title'].map(len)
print(df)


def create_year(df):
    """
    生成年份分布情况
    """
    year_message = df.groupby(['year'])
    year_com = year_message['year'].agg(['count'])
    year_com.reset_index(inplace=True)
    # 生成折线图
    attr = ["{}".format(str(i) + '年') for i in year_com['year']]
    v1 = year_com['count']
    line = Line("公众号文章各年份发布数量走势图", title_pos='center', title_top='18', width=800, height=400)
    line.add("", attr, v1, xaxis_interval=0, yaxis_max=300, is_smooth=True, is_fill=True, area_color="#000", is_xaxislabel_align=True, xaxis_min="dataMin", area_opacity=0.3, mark_point=["max"], mark_point_symbol="pin", mark_point_symbolsize=45)
    line.render("公众号文章各年份发布数量走势图.html")


def create_month(df):
    """
    生成月份分布情况(总的)
    """
    month_message = df.groupby(['month'])
    month_com = month_message['month'].agg(['count'])
    month_com.reset_index(inplace=True)
    # 生成折线图
    attr = ["{}".format(str(i) + '月') for i in month_com['month']]
    v1 = month_com['count']
    line = Line("公众号文章月份发布数量走势图", title_pos='center', title_top='18', width=800, height=400)
    line.add("", attr, v1, xaxis_interval=0, yaxis_max=120, is_smooth=True, is_fill=True, area_color="#000", is_xaxislabel_align=True, xaxis_min="dataMin", area_opacity=0.3, mark_point=["max"], mark_point_symbol="pin", mark_point_symbolsize=45)
    line.render("公众号文章月份发布数量走势图.html")


def create_month_year(df):
    """
    生成每年各月份分布情况
    """
    v = []
    # 生成每年的月份情况
    for i in ['2014', '2015', '2016', '2017', '2018']:
        dom = df[df['year'] == i]
        dom_message = dom.groupby(['month'])
        dom_com = dom_message['month'].agg(['count'])
        dom_com.reset_index(inplace=True)
        v1 = np.array(dom_com['count'])
        v1 = ["{}".format(int(i)) for i in v1]
        attr = dom_com['month']
        v.append(v1)

    # 生成折线图
    attr = ["{}".format(str(i) + '月') for i in attr]
    line = Line("公众号文章每年各月份发布数量走势图", title_pos='center', title_top='0', width=800, height=400)
    line.add("2015", attr, v[1], line_color='red', legend_top='8%')
    line.add("2016", attr, v[2], line_color='purple', legend_top='8%')
    line.add("2017", attr, v[3], line_color='green', legend_top='8%')
    line.add("2018", attr, v[4], line_color='orange', legend_top='8%')
    line.render("公众号文章每年各月份发布数量走势图.html")


def create_hour(df):
    """
    生成小时分布情况
    """
    hour_message = df.groupby(['hour'])
    hour_com = hour_message['hour'].agg(['count'])
    hour_com.reset_index(inplace=True)
    hour_com_last = hour_com.sort_index()
    # 生成柱状图
    attr = hour_com_last['hour']
    v1 = np.array(hour_com_last['count'])
    bar = Bar("公众号具体发文时间分布", title_pos='center', title_top='18', width=800, height=400)
    bar.add("", attr, v1, is_stack=True, is_label_show=True)
    bar.render("公众号具体发文时间分布.html")


def create_title_len(df):
    """
    生成文章标题长度情况
    """
    title_len = df['title_len']
    bins = [0, 5, 10, 15, 20, 25, 30]
    level = ['0-5', '5-10', '10-15', '15-20', '25-30', '30以上']
    len_stage = pd.cut(title_len, bins=bins, labels=level).value_counts().sort_index()
    # 生成柱状图
    attr = len_stage.index
    v1 = len_stage.values
    bar = Bar("文章标题长度分布情况", title_pos='center', title_top='18', width=800, height=400)
    bar.add("", attr, v1, is_stack=True, is_label_show=True)
    bar.render("文章标题长度分布情况.html")


def create_wordcloud(df):
    """
    生成标题以及摘要词云
    """
    words = pd.read_csv('chineseStopWords.txt', encoding='gbk', sep='\t', names=['stopword'])
    # 分词
    text = ''
    # for line in df['title']:
    for line in df['digest']:
        text += ' '.join(jieba.cut(str(line), cut_all=False))
    # 停用词
    stopwords = set('')
    stopwords.update(words['stopword'])
    backgroud_Image = plt.imread('article.jpg')
    wc = WordCloud(
        background_color='white',
        mask=backgroud_Image,
        font_path='C:\Windows\Fonts\华康俪金黑W8.TTF',
        max_words=2000,
        max_font_size=150,
        min_font_size=15,
        prefer_horizontal=1,
        random_state=50,
        stopwords=stopwords
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
    wc.to_file("文章摘要词云.jpg")
    # wc.to_file("文章标题词云.jpg")
    print('生成词云成功!')


if __name__ == '__main__':
    create_hour(df)
    create_year(df)
    create_month(df)
    create_title_len(df)
    create_wordcloud(df)
    create_month_year(df)