#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   single_od.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/12/28 16:48   SeafyLiang   1.0      基于标准差和箱体图的单指标异常点检测
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MinMaxScaler


def od_method(df, od_columns):
    df = df[od_columns]
    r_df = pd.DataFrame()
    # 循环每列进行异常点检测
    for od_column in od_columns:
        # 自定义规则
        # if od_column == 'age':
        #     iqr_lower = 0
        #     iqr_upper = 100

        total_num = df.index.size  # 总数据量
        column_count = df[od_column].count()  # 非空数据量
        null_num = total_num - column_count  # 空值数据量
        err_num = df.loc[df[od_column] == -99999].index.size  # 无效值数据量
        zero_num = df.loc[df[od_column] == 0].index.size  # 零值数据量
        column_max = df[od_column].max()  # 最大值
        column_min = df[od_column].min()  # 最小值

        df_notnull = df.dropna(axis=0, subset=[od_column])  # 取得非空数据
        s = df_notnull[(df_notnull[od_column] != -99999) & (df_notnull[od_column] != 0)][od_column]  # 在非空数据集中剔除掉无效值和零值

        # 结果表格列头
        df_columns = [
            'total_num',
            'column_count',
            'null_num',
            'err_num',
            'zero_num',
            'normal_mean',
            'normal_std',
            'std_lower',
            'std_upper',
            'iqr_lower',
            'iqr_upper',
            'std_od_num',
            'std_lower_od_num',
            'std_upper_od_num',
            'iqr_od_num',
            'iqr_lower_od_num',
            'iqr_upper_od_num',
            'max',
            'min',
            'normal_mean',
            'normal_std'
        ]
        df_temp = pd.DataFrame(columns=df_columns)
        df_temp.at['%s' % od_column, 'total_num'] = total_num
        df_temp.at['%s' % od_column, 'column_count'] = column_count
        df_temp.at['%s' % od_column, 'null_num'] = null_num
        df_temp.at['%s' % od_column, 'err_num'] = err_num
        df_temp.at['%s' % od_column, 'zero_num'] = zero_num
        df_temp.at['%s' % od_column, 'normal_mean'] = column_max
        df_temp.at['%s' % od_column, 'normal_std'] = column_min

        # 若非空数据集中剔除掉无效值和零值数量为0，则检测结果置空
        if len(s) == 0:
            err_value = np.nan
            df_temp.at['%s' % od_column, 'std_lower'] = err_value
            df_temp.at['%s' % od_column, 'std_upper'] = err_value
            df_temp.at['%s' % od_column, 'iqr_lower'] = err_value
            df_temp.at['%s' % od_column, 'iqr_upper'] = err_value
            df_temp.at['%s' % od_column, 'std_od_num'] = err_value
            df_temp.at['%s' % od_column, 'std_lower_od_num'] = err_value
            df_temp.at['%s' % od_column, 'std_upper_od_num'] = err_value
            df_temp.at['%s' % od_column, 'iqr_od_num'] = err_value
            df_temp.at['%s' % od_column, 'iqr_lower_od_num'] = err_value
            df_temp.at['%s' % od_column, 'iqr_upper_od_num'] = err_value
            df_temp.at['%s' % od_column, 'max'] = err_value
            df_temp.at['%s' % od_column, 'min'] = err_value
            df_temp.at['%s' % od_column, 'normal_mean'] = err_value
            df_temp.at['%s' % od_column, 'normal_std'] = err_value
            r_df = pd.concat([r_df, df_temp])
        else:
            # 1、箱体图四分位上下限计算
            q1 = s.quantile(0.25)
            q3 = s.quantile(0.75)
            iqr = q3 - q1

            iqr_lower = q1 - 1.5 * iqr
            iqr_upper = q3 + 1.5 * iqr

            # 2、标准差上下限计算
            normal_mean = s.mean()
            normal_std = s.std()
            std_lower = normal_mean - 3 * normal_std
            std_upper = normal_mean + 3 * normal_std

            std_od_num = df[(df[od_column] < std_lower) | (df[od_column] > std_upper)].index.size
            std_lower_od_num = df[df[od_column] < std_lower].index.size
            std_upper_od_num = df[df[od_column] > std_upper].index.size
            iqr_od_num = df[(df[od_column] < iqr_lower) | (df[od_column] > iqr_upper)].index.size
            iqr_lower_od_num = df[df[od_column] < iqr_lower].index.size
            iqr_upper_od_num = df[df[od_column] > iqr_upper].index.size

            df_temp.at['%s' % od_column, 'std_lower'] = std_lower
            df_temp.at['%s' % od_column, 'std_upper'] = std_upper
            df_temp.at['%s' % od_column, 'iqr_lower'] = iqr_lower
            df_temp.at['%s' % od_column, 'iqr_upper'] = iqr_upper
            df_temp.at['%s' % od_column, 'std_od_num'] = std_od_num
            df_temp.at['%s' % od_column, 'std_lower_od_num'] = std_lower_od_num
            df_temp.at['%s' % od_column, 'std_upper_od_num'] = std_upper_od_num
            df_temp.at['%s' % od_column, 'iqr_od_num'] = iqr_od_num
            df_temp.at['%s' % od_column, 'iqr_lower_od_num'] = iqr_lower_od_num
            df_temp.at['%s' % od_column, 'iqr_upper_od_num'] = iqr_upper_od_num
            df_temp.at['%s' % od_column, 'max'] = column_max
            df_temp.at['%s' % od_column, 'min'] = column_min
            df_temp.at['%s' % od_column, 'normal_mean'] = normal_mean
            df_temp.at['%s' % od_column, 'normal_std'] = normal_std
            r_df = pd.concat([r_df, df_temp])
    r_df.reset_index(inplace=True)
    return r_df


def model_rf_od(df):
    # 使用孤立森林算法进行异常值检测
    DetectionModel = IsolationForest()
    DetectionModel.fit(np.array(df['c']).reshape(-1, 1))

    # 得到检测值，其中1代表正常值，-1代表异常值
    DctectionValue = DetectionModel.predict(np.array(df['c']).reshape(-1, 1))

    df["DctectionValue"] = DctectionValue
    return df


def model_kmeans_od(df):
    # 使用kmeans算法检验异常值，首先使用轮廓系数法来确定k值
    ScoreList = []
    for i in range(3, 30):
        # 构建并训练模型
        kmeans = KMeans(n_clusters=i, random_state=123).fit(df)
        score = silhouette_score(df, kmeans.labels_)
        ScoreList.append(score)
    plt.figure(figsize=(30, 10))
    plt.tick_params(labelsize=30)
    plt.plot(range(3, 30), ScoreList, linewidth=1.5, linestyle="-")
    plt.show()
    # 构造kmeans算法，检测异常值，选择指定的labels即为异常值
    scale = MinMaxScaler().fit(df)
    DfDataScale = scale.transform(df)
    KmeansModel = KMeans(n_clusters=8).fit(DfDataScale)

    ClassNum = pd.Series(KmeansModel.labels_).value_counts()
    print(ClassNum)
    df["labels"] = KmeansModel.labels_
    return df


if __name__ == '__main__':
    df = pd.read_csv('data/od_test.csv')
    df.boxplot()
    plt.show()
    od_columns = ['a', 'b', 'c', 'd', 'e', 'f']
    r_df = od_method(df, od_columns)
    r_df.to_csv('data/od_result.csv', index=False)
    r_df = model_rf_od(df)
    r_df.to_csv('data/od_result_model_rf.csv', index=False)
    r_df = model_kmeans_od(df)
    r_df.to_csv('data/od_result_model_kmeans.csv', index=False)
