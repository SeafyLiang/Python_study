#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   pandas_visual_1&2d.py
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/1/12 14:47   SeafyLiang   1.0       pandas常用8种画图-1&2维
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mglearn


def dimensional_1(df):
    '''
    常用的一维画图：
    1、直方图
    2、密度图
    '''
    # 1、直方图（histogram）
    df.hist(bins=15, color='steelblue', edgecolor='black', linewidth=1.0,
            xlabelsize=8, ylabelsize=8, grid=False)
    plt.show()

    # 2、密度图（density）
    df[['c', 'd', 'f']].plot.density()
    plt.show()


def dimensional_2(df):
    '''
    常用的二维画图：
    1、相关矩阵热力图
    2、配对散点图
    3、平行坐标系图
    4、联合分布图
    5、箱线图
    6、小提琴图
    '''
    # 1、相关矩阵热力图
    # Correlation Matrix Heatmap
    f, ax = plt.subplots(figsize=(10, 6))
    corr = df.corr()
    hm = sns.heatmap(round(corr, 2), annot=True, ax=ax, cmap="coolwarm", fmt='.2f',
                     linewidths=.05)
    f.subplots_adjust(top=0.93)
    plt.suptitle('df Attributes Correlation Heatmap', fontsize=14)
    plt.show()

    # 2、配对散点图
    y = df['d']  # 目标值，散点图的颜色
    pd.plotting.scatter_matrix(df, marker='o', hist_kwds={'bins': 50}, s=1, c=y, cmap=mglearn.cm3)
    plt.suptitle('df Scatter Matrix')
    plt.show()

    # 3、平行坐标系图
    df.plot(x='c')
    plt.show()

    # 4、联合分布图
    # Joint Plot
    sns.jointplot(x='f', y='d', data=df, kind='reg')
    plt.show()

    # 5、箱型图
    df.boxplot()
    plt.show()

    # 6、小提琴图
    # Violin Plots
    f, (ax) = plt.subplots(1, 1, figsize=(12, 4))
    f.suptitle('d - f Content', fontsize=14)

    sns.violinplot(x="d", y="f", data=df, ax=ax)
    ax.set_xlabel("d", size=12, alpha=0.8)
    ax.set_ylabel("f", size=12, alpha=0.8)
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('data/od_test.csv')
    dimensional_1(df)
    dimensional_2(df)
