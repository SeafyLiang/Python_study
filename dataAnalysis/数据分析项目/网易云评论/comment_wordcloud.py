from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import random
import jieba


# 设置文本随机颜色
def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h, s, l = random.choice([(188, 72, 53), (253, 63, 56), (12, 78, 69)])
    return "hsl({}, {}%, {}%)".format(h, s, l)


# 读取信息
df = pd.read_csv('comment_after.csv', header=None, names=['name', 'userid', 'age', 'gender', 'city', 'text', 'comment', 'commentid', 'praise', 'date'], encoding='utf-8-sig')
# 根据评论ID去重
df = df.drop_duplicates('commentid')
words = pd.read_csv('chineseStopWords.txt', encoding='gbk', sep='\t', names=['stopword'])
# 分词
text = ''
for line in df['comment']:
    text += ' '.join(jieba.cut(str(line), cut_all=False))
# 停用词
stopwords = set('')
stopwords.update(words['stopword'])
backgroud_Image = plt.imread('music.jpg')

wc = WordCloud(
    background_color='white',
    mask=backgroud_Image,
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
# img_colors = ImageColorGenerator(backgroud_Image)
# 看看词频高的有哪些
process_word = WordCloud.process_text(wc, text)
sort = sorted(process_word.items(), key=lambda e: e[1], reverse=True)
print(sort[:50])
plt.imshow(wc)
plt.axis('off')
wc.to_file("网易云音乐评论词云.jpg")
print('生成词云成功!')
