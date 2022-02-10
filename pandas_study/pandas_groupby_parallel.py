#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   pandas_groupby_parallel.py
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/2/10 17:41   SeafyLiang   1.0       pandas-groupby并行加速
"""

from joblib import Parallel, delayed
import pandas as pd

from functools import wraps
import time


def func_timer(function):
    '''
    用装饰器实现函数计时
    :param function: 需要计时的函数
    :return: None
    '''

    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print('[Function: {name} finished, spent time: {time:.2f}s]'.format(name=function.__name__, time=t1 - t0))
        return result

    return function_timer


def processParallel(df, name):
    # 处理数据,如果不加name，return的data没有group信息
    df['avg_col'] = df['col'].mean()
    return df


def applyParallel(dfGrouped, func):
    retLst = Parallel(n_jobs=6)(delayed(func)(group, name) for name, group in dfGrouped)
    return pd.concat(retLst)


@func_timer
def para(df):
    multi_res = applyParallel(df.groupby('data_index'), processParallel)
    print(multi_res.info())
    print(multi_res.head())


@func_timer
def single(df):
    sn_df = df.groupby("data_index")
    r_df = pd.DataFrame()
    for index, data in sn_df:
        data['avg_col'] = data['col'].mean()
        r_df = pd.concat([r_df, data])
    print(r_df.info())
    print(r_df.head())


if __name__ == '__main__':
    # 测试数据 440030数据量 7.11s -> 2.27s
    df = pd.read_csv('test.csv')
    para(df)
    single(df)
