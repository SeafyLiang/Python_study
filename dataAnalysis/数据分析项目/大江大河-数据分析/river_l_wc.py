from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import pandas
import random
import jieba


# 设置文本随机颜色
def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h, s, l = random.choice([(188, 72, 53), (253, 63, 56), (12, 78, 69)])
    return "hsl({}, {}%, {}%)".format(h, s, l)


# 绘制圆形
x, y = np.ogrid[:1500,:1500]
mask = (x - 700) ** 2 + (y - 700) ** 2 > 700 ** 2
mask = 255 * mask.astype(int)
# 读取信息
df = pandas.read_csv('comments_douban_ll.csv', header=None, names=['user_name', 'user_url', 'registered_time', 'score', 'date', 'comment_time', 'useful_num', 'comment', 'score1', 'sentiment'])
words = pandas.read_csv('chineseStopWords.txt', encoding='gbk', sep='\t', names=['stopword'])
# 分词
text = ''
for line in df['comment']:
    text += ' '.join(jieba.cut(str(line), cut_all=False))
# 停用词
stopwords = set('')
stopwords.update(words['stopword'])

wc = WordCloud(
    background_color='white',
    mask=mask,
    font_path='C:\Windows\Fonts\华康俪金黑W8.TTF',
    max_words=2000,
    max_font_size=250,
    min_font_size=15,
    color_func=random_color_func,
    prefer_horizontal=1,
    random_state=50,
    stopwords=stopwords
)

wc.generate_from_text(text)
# 看看词频高的有哪些
process_word = WordCloud.process_text(wc, text)
sort = sorted(process_word.items(), key=lambda e:e[1], reverse=True)
print(sort[:50])
plt.imshow(wc)
plt.axis('off')
wc.to_file("豆瓣差评词云.jpg")
print('生成词云成功!')
