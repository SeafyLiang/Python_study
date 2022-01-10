#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   duplicates_and_fillNan.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/12/29 21:54   SeafyLiang   1.0      重复值和缺失值
"""
import pandas as pd
from scipy import stats
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier


# 重复值处理
def duplicates(df):
    # 重复的内容
    print(df[df.duplicated()])

    # 统计重复行的数量
    print(df.duplicated().sum())

    # 删除重复行
    r_df = df.drop_duplicates()
    print(r_df)

    # 按列去重
    r_df = df.drop_duplicates('a')
    print(r_df)


# 检索空值
def query_nan(df):
    # 查看空值
    print(df.isna())

    # 查看某列空值
    print(df['a'].isna())

    # 筛选出某列为空的行
    r_df = df[df['a'].isna()]
    print(r_df)


# 删除空值
def del_nan(df):
    # 1、删除‘age’列
    df.drop('age', axis=1, inplace=True)

    # 2、删除数据表中含有空值的行
    df.dropna()

    # 3、丢弃某几列有缺失值的行
    df.dropna(axis=0, subset=['a', 'b'], inplace=True)

    # 去掉缺失比例大于80%以上的变量
    df = df.dropna(thresh=len(df) * 0.2, axis=1)


# 固定值填充空值
def fixed_value_fill(df):
    # 均值填充
    df['col'] = df['col'].fillna(df['col'].means())
    # 中位数填充
    df['col'] = df['col'].fillna(df['col'].median())
    # 众数填充
    df['col'] = df['col'].fillna(stats.mode(df['col'])[0][0])


# 插值填充空值
def interpolate_fill(df):
    #  interpolate()插值法，缺失值前后数值的均值，但是若缺失值前后也存在缺失，则不进行计算插补。
    df['c'] = df['c'].interpolate()

    # 用前面的值替换, 当第一行有缺失值时，该行利用向前替换无值可取，仍缺失
    df.fillna(method='pad')

    # 用后面的值替换，当最后一行有缺失值时，该行利用向后替换无值可取，仍缺失
    df.fillna(method='backfill')  # 用后面的值替换


# 数据预处理，模型填充空值
def data_preprocess(df):
    # 需要先对d,e列数据做插值填充，后续作为训练数据
    df['d'] = df['d'].interpolate()
    df['e'] = df['e'].interpolate()
    print(df.info())
    # 拆分空数据和非空数据
    df_notnull = df[df['a'].notnull()]  # 非空数据
    df_null = df[df['a'].isnull()]  # 空数据
    x_train = df_notnull[['d', 'e']]  # 训练数据x， d,e列
    y_train = df_notnull['a']  # 训练数据y， a列（目标）
    test = df_null[['d', 'e']]  # 预测数据x, d,e列
    index, predict = knn_filled_func(x_train, y_train, test, 3, True)
    index, predict = RandomForest_filled_func(x_train, y_train, test, True)
    # 填充预测值
    df_null['a'] = predict
    # 回填到原始数据中
    df['a'] = df['a'].fillna(df_null[['a']].a)
    print(df.info())


# knn填充空值
def knn_filled_func(x_train, y_train, test, k=3, dispersed=True):
    # params: x_train 为目标列不含缺失值的数据（不包括目标列）
    # params: y_train 为不含缺失值的目标列
    # params: test 为目标列为缺失值的数据（不包括目标列）
    if dispersed:
        knn = KNeighborsClassifier(n_neighbors=k, weights="distance")
    else:
        knn = KNeighborsRegressor(n_neighbors=k, weights="distance")

    knn.fit(x_train, y_train.astype('int'))
    return test.index, knn.predict(test)


# 随机森林填充空值
def RandomForest_filled_func(x_train, y_train, test, dispersed=True):
    # params: x_train 为目标列不含缺失值的数据（不包括目标列）
    # params: y_train 为不含缺失值的目标列
    # params: test 为目标列为缺失值的数据（不包括目标列）
    if dispersed:
        rf = RandomForestRegressor()
    else:
        rf = RandomForestClassifier()

    rf.fit(x_train, y_train.astype('int'))
    return test.index, rf.predict(test)


if __name__ == '__main__':
    df = pd.read_csv('data/test_data.csv')
    print(df.head())
    data_preprocess(df)
