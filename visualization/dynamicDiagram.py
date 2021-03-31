#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   dynamicDiagram.py
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/3/31 21:19   SeafyLiang   1.0    动态可视化比特币数据
"""

# 1.获取数据
# 比特币数据很多网站都有，并且也有很多成熟的API，所以取数据非常简单，直接调用API接口即可
import requests
import json
import csv
import time

time_stamp = int(time.time())
url = f"https://web-api.coinmarketcap.com/v1/cryptocurrency/ohlcv/historical?convert=USD&slug=bitcoin&time_end={time_stamp}&time_start=1367107200"
rd = requests.get(url=url)
# 返回的数据是 JSON 格式，使用 json 模块解析
co = json.loads(rd.content)
list1 = co['data']['quotes']

with open('data/BTC.csv', 'w', encoding='utf8', newline='') as f:
    csvi = csv.writer(f)
    csv_head = ["date", "price", "volume"]
    csvi.writerow(csv_head)

    for i in list1:
        quote_date = i["time_open"][:10]
        quote_price = "{:.2f}".format(i["quote"]["USD"]["close"])
        quote_volume = "{:.2f}".format(i["quote"]["USD"]["volume"])
        csvi.writerow([quote_date, quote_price, quote_volume])

# 2.动态可视化BTC价格变化
import pandas as pd
import matplotlib as mpl
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML
from datetime import datetime

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 设置显示中文
plt.rcParams['axes.unicode_minus'] = False
plt.rc('axes', axisbelow=True)  # 设置外观要求，即坐标轴置底
mpl.rcParams['animation.embed_limit'] = 2 ** 128  # 为了生成动画而用的，由于动画默认的最大体积为20971520.字节

# 3.读取数据
df = pd.read_csv('data/BTC.csv')
df['date'] = [datetime.strptime(d, '%Y-%m-%d').date() for d in df['date']]

# 4.绘图
# 4.1 静态单色面积图
Span = 180
N_Span = 0
df_temp = df.loc[N_Span * Span:(N_Span + 1) * Span, :]
df_temp.head(5)
fig = plt.figure(figsize=(6, 4), dpi=100)
plt.subplots_adjust(top=1, bottom=0, left=0, right=0.9, hspace=0, wspace=0)
plt.fill_between(df_temp.date.values, y1=df_temp.price.values, y2=0, alpha=0.75, facecolor='r', linewidth=1,
                 edgecolor='none', zorder=1)
plt.plot(df_temp.date, df_temp.price, color='k', zorder=2)
plt.scatter(df_temp.date.values[-1], df_temp.price.values[-1], color='white', s=150, edgecolor='k', linewidth=2,
            zorder=3)
plt.text(df_temp.date.values[-1], df_temp.price.values[-1] * 1.18, s=np.round(df_temp.price.values[-1], 1), size=10,
         ha='center', va='top')
plt.ylim(0, df_temp.price.max() * 1.68)
plt.xticks(ticks=df_temp.date.values[0:Span + 1:30], labels=df_temp.date.values[0:Span + 1:30], rotation=0)
plt.margins(x=0.01)
ax = plt.gca()  # 获取边框
ax.spines['top'].set_color('none')  # 设置上‘脊梁’为无色
ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
ax.spines['left'].set_color('none')  # 设置上‘脊梁’为无色
plt.grid(axis="y", c=(217 / 256, 217 / 256, 217 / 256), linewidth=1)  # 设置网格线
plt.show()
"""
Span设定的是多少天的价格，这里使用200天。N_Span代表权重；
df_temp=df.loc[N_Span*Span:(N_Span+1)*Span,:]代表的是选择到179行为止的数据，即180天。
plt.fill_between()是使用单色--红色填充，
"""
# 4.2 渐变颜色面积图
Span_Date = 180
Num_Date = 360  # 终止日期
df_temp = df.loc[Num_Date - Span_Date: Num_Date, :]  # 选择从Num_Date-Span_Date开始到Num_Date的180天的数据
colors = cm.Spectral_r(df_temp.price / float(max(df_temp.price)))
fig = plt.figure(figsize=(6, 4), dpi=100)
plt.subplots_adjust(top=1, bottom=0, left=0, right=0.9, hspace=0, wspace=0)
plt.bar(df_temp.date.values, df_temp.price.values, color=colors, width=1, align="center", zorder=1)
plt.plot(df_temp.date, df_temp.price, color='k', zorder=2)
plt.scatter(df_temp.date.values[-1], df_temp.price.values[-1], color='white', s=150, edgecolor='k', linewidth=2,
            zorder=3)
plt.text(df_temp.date.values[-1], df_temp.price.values[-1] * 1.18, s=np.round(df_temp.price.values[-1], 1), size=10,
         ha='center', va='top')
plt.ylim(0, df_temp.price.max() * 1.68)
plt.xticks(ticks=df_temp.date.values[0: Span_Date + 1:30], labels=df_temp.date.values[0: Span_Date + 1:30], rotation=0)
plt.margins(x=0.01)
ax = plt.gca()  # 获取边框
ax.spines['top'].set_color('none')  # 设置上‘脊梁’为无色
ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
ax.spines['left'].set_color('none')  # 设置上‘脊梁’为无色
plt.grid(axis="y", c=(217 / 256, 217 / 256, 217 / 256), linewidth=1)  # 设置网格线
plt.show()

"""
使用plt.bar()函数实现Spectral_r颜色映射。
Span_Date设置初始时间，这里设置为180即从起始日开始算的180天。
Num_Date设置的是终止时间。
df_temp=df.loc[Num_Date-Span_Date: Num_Date,:]则是用loc函数筛选从180天到终止日期的数据。
"""


# 4.3 动态可视化
def draw_areachart(Num_Date):
    Span_Date = 180
    ax.clear()
    if Num_Date < Span_Date:
        df_temp = df.loc[0:Num_Date, :]
        df_span = df.loc[0:Span_Date, :]
        colors = cm.Spectral_r(df_span.price.values / float(max(df_span.price.values)))
        plt.bar(df_temp.date.values, df_temp.price.values, color=colors, width=1.5, align="center", zorder=1)
        plt.plot(df_temp.date, df_temp.price, color='k', zorder=2)
        plt.scatter(df_temp.date.values[-1], df_temp.price.values[-1], color='white', s=150, edgecolor='k', linewidth=2,
                    zorder=3)
        plt.text(df_temp.date.values[-1], df_temp.price.values[-1] * 1.18, s=np.round(df_temp.price.values[-1], 1),
                 size=10, ha='center', va='top')
        plt.ylim(0, df_span.price.max() * 1.68)
        plt.xlim(df_span.date.values[0], df_span.date.values[-1])
        plt.xticks(ticks=df_span.date.values[0:Span_Date + 1:30], labels=df_span.date.values[0:Span_Date + 1:30],
                   rotation=0, fontsize=9)
    else:
        df_temp = df.loc[Num_Date - Span_Date:Num_Date, :]
        colors = cm.Spectral_r(df_temp.price / float(max(df_temp.price)))
        plt.bar(df_temp.date.values[:-2], df_temp.price.values[:-2], color=colors[:-2], width=1.5, align="center",
                zorder=1)
        plt.plot(df_temp.date[:-2], df_temp.price[:-2], color='k', zorder=2)
        plt.scatter(df_temp.date.values[-4], df_temp.price.values[-4], color='white', s=150, edgecolor='k', linewidth=2,
                    zorder=3)
        plt.text(df_temp.date.values[-1], df_temp.price.values[-1] * 1.18, s=np.round(df_temp.price.values[-1], 1),
                 size=10, ha='center', va='top')
        plt.ylim(0, df_temp.price.max() * 1.68)
        plt.xlim(df_temp.date.values[0], df_temp.date.values[-1])
        plt.xticks(ticks=df_temp.date.values[0:Span_Date + 1:30], labels=df_temp.date.values[0:Span_Date + 1:30],
                   rotation=0, fontsize=9)

    plt.margins(x=0.2)
    ax.spines['top'].set_color('none')  # 设置上‘脊梁’为红色
    ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
    ax.spines['left'].set_color('none')  # 设置上‘脊梁’为无色
    plt.grid(axis="y", c=(217 / 256, 217 / 256, 217 / 256), linewidth=1)  # 设置网格线
    plt.text(0.01, 0.95, "BTC平均价格($)", transform=ax.transAxes, size=10, weight='light', ha='left')
    ax.text(-0.07, 1.03, '2013年到2021年的比特币BTC价格变化情况', transform=ax.transAxes, size=17, weight='light', ha='left')


fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
plt.subplots_adjust(top=1, bottom=0.1, left=0.1, right=0.9, hspace=0, wspace=0)
draw_areachart(150)
"""
使用matplotlib包的animation.FuncAnimation()函数，之后调用上述编写的draw_areachart(Num_Date)函数。
其中输入的参数Num_Date是如静态可视化中提及的日期作用一样，赋值为np.arange(0,df.shape[0],1)。
最后使用Ipython包的HTML()函数将动画转换成动画页面的形式演示。
"""
import matplotlib.animation as animation
from IPython.display import HTML

fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
plt.subplots_adjust(left=0.12, right=0.98, top=0.85, bottom=0.1, hspace=0, wspace=0)
animator = animation.FuncAnimation(fig, draw_areachart, frames=np.arange(0, df.shape[0], 1), interval=100)
HTML(animator.to_jshtml())
"""
FuncAnimation(fig,func,frames,init_func,interval,blit)是绘制动图函数，参数如下：
- fig 表示绘制动图的画布名称(figure)；
- func为自定义绘图函数，如draw_barchart()函数；
- frames为动画长度，一次循环包含的帧数，在函数运行时，其值会传递给函数draw_barchart (year)的形参“year”；
- init_func为自定义开始帧可省略；
- interval表示更新频率，计量单位为ms；
- blit表示选择更新所有点，还是仅更新产生变化的点，应选择为True，但mac电脑用户应选择False，否则无法显示。
"""
