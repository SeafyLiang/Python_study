from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import pandas as pd
import pymysql
import jieba

conn = pymysql.connect(host='localhost', user='root', password='774110919', port=3306, db='lagou_job', charset='utf8mb4')
cursor = conn.cursor()
sql = "select * from job"
df = pd.read_sql(sql, conn)

text = ''
for line in df['job_welfare']:
    text += ' '.join(jieba.cut(line, cut_all=False))
backgroud_Image = plt.imread('job.jpg')

wc = WordCloud(
    background_color='white',
    mask=backgroud_Image,
    font_path='C:\Windows\Fonts\STZHONGS.TTF',
    max_words=2000,
    max_font_size=150,
    random_state=30,
)
wc.generate_from_text(text)
img_colors = ImageColorGenerator(backgroud_Image)
wc.recolor(color_func=img_colors)
plt.imshow(wc)
plt.axis('off')
wc.to_file("福利.jpg")
print('生成词云成功!')

