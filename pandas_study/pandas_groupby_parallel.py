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
from pandarallel import pandarallel
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
    time.sleep(1)
    # 处理数据,如果不加name，return的data没有group信息
    df['avg_b'] = df['b'].mean()
    return df


def mul_process(df):
    time.sleep(1)
    df['avg_b'] = df['b'].mean()
    return df


def applyParallel(dfGrouped, func):
    retLst = Parallel(n_jobs=6)(delayed(func)(group, name) for name, group in dfGrouped)
    return pd.concat(retLst)


@func_timer
def para(df):
    multi_res = applyParallel(df.groupby('c'), processParallel)
    print(multi_res.info())
    print(multi_res.head())


@func_timer
def single(df):
    sn_df = df.groupby("c")
    r_df = pd.DataFrame()
    for index, data in sn_df:
        time.sleep(1)
        data['avg_b'] = data['b'].mean()
        r_df = pd.concat([r_df, data])
    print(r_df.info())
    print(r_df.head())


@func_timer
def multi_para(df):
    '''
    推荐使用这个并行加速
    '''
    pandarallel.initialize()
    multi_res = df.groupby("c").parallel_apply(mul_process)
    print(multi_res.info())
    print(multi_res.head())


if __name__ == '__main__':
    # 测试数据
    # [Function: single finished, spent time: 200.72s]
    # [Function: para finished, spent time: 35.21s]
    # [Function: multi_para finished, spent time: 25.31s]
    df = pd.read_csv('data/od_test.csv')
    para(df)
    single(df)
    multi_para(df)
