import pandas as pd
import requests
import pdfkit
import os
import re

# 读取数据并清洗
df = pd.read_csv('article.csv', header=None, names=['title', 'digest', 'article_url', 'date'], encoding='gbk')
df['date'] = pd.to_datetime(df.date.values, unit='s', utc=True).tz_convert('Asia/Shanghai')
df_date = df['date'].astype(str).str.split(' ', expand=True)
df['day'] = df_date[0]
# 获取目录的绝对路径
fileDir = os.path.abspath(os.path.dirname('F:\\article_pdf'))

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.901.400 QQBrowser/9.0.2524.400",
}

proxies = {
    "https": None,
    "http": None,
}

# 设置转PDF参数
options = {
        "page-size": "Letter",
        "encoding": "UTF-8",
        "custom-header": [
            ("Accept-Encoding", "gzip")
        ]
    }

# 调用wkhtmltopdf
# confg = pdfkit.configuration(wkhtmltopdf=r"C:\Users\Administrator\wkhtmltox-0.12.5-1.mxe-cross-win64\wkhtmltox\bin\wkhtmltopdf.exe")

for title, url, date in zip(df['title'], df['article_url'], df['day']):
    print(title, url, date)
    # 替换特殊符号
    title = re.sub('[\/:：*?"<>|]', '', title)
    title = title.replace('\\', '_')
    # html文件名
    html_name = '{}/{}.html'.format('F:\\article_pdf', date + '_' + title)
    res = requests.get(url, headers=headers, proxies=proxies, timeout=3)
    html = res.text
    # 用?来控制正则贪婪和非贪婪匹配;(.*?) 小括号来控制是否包含匹配的关键字
    pattern = re.compile(r'data-src=\"http.*?\"')
    result = pattern.findall(html)
    picCnt = 0
    for i in result:
        picCnt = picCnt + 1
        url = re.findall(r'\"(.*?)\"', i)[0]
        # 图片名
        picture_name = '{}/{}.png'.format('F:\\article_pdf', str(picCnt))
        # 调用本地图片
        html = html.replace(url, picture_name)
        # 获取图片内容
        r = requests.get(url)
        with open(picture_name, "wb+") as f:
            f.write(r.content)
        # 保存html文件
        html = html.replace('data-src', 'src')
        fd = open(html_name, 'w', encoding="utf-8")
        fd.write(html)
        fd.close()

    pdf_name = '{}/{}.pdf'.format('F:\\article_pdf', date + '_' + title)
    try:
        # html转pdf
        pdfkit.from_file(html_name, pdf_name, options=options)
    except:
        pass