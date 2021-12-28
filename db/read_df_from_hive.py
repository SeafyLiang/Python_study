#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   read_df_from_hive.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/12/27 17:39   SeafyLiang   1.0       pyhive读取hive数据，存成df
"""
from pyhive import hive
import pandas as pd


def read_test_10w():
    '''
    测试10W条数据读取
    pyhive：
    耗时：38.48s；内存使用：16.8+ MB
    datagrip：execution: 1 s 15 ms, fetching: 600 ms

    测试100W条数据读取
    耗时：365.06s
    内存使用：167.8+ MB
    :return:
    '''
    conn = hive.Connection(host='hmaster-1',
                           port=10000,
                           auth="CUSTOM",
                           database='default',
                           username='hive',
                           password='hive')
    cursor = conn.cursor()
    cursor.execute('select * from table_name limit 1000')

    name_list = ['id', 'timestamp', 'name']
    tuple_all = tuple(cursor.fetchall())
    r_df = pd.DataFrame(list(tuple_all), columns=name_list)
    print(r_df)
    print(r_df.info())

    cursor.close()
    conn.close()


def read_from_hive(data_sql, columns_list):
    '''
    从hive库读取数据，存成df
    :param data_sql: 查询的sql语句
    :param columns_list: 表头
    :return: pandas.dataframe对象
    '''
    print("data_sql：", data_sql)

    conn = hive.Connection(host='hmaster-1',
                           port=10000,
                           auth="CUSTOM",
                           database='default',
                           username='hive',
                           password='hive')
    print("hive connection")
    cursor = conn.cursor()
    print("hive exec sql... ...")
    cursor.execute(data_sql)
    print("hive exec fetchall data... ...")
    tuple_all = tuple(cursor.fetchall())
    print("正在合成DataFrame... ...")
    df = pd.DataFrame(list(tuple_all), columns=columns_list)
    print(df.info())
    print(df.head())

    cursor.close()
    conn.close()
    print("hive disconnected")
    return df


if __name__ == '__main__':
    # uvicorn test_demo:app --host '0.0.0.0' --port 8000 --reload
    # /docs
    # /redoc
    read_test_10w()

    # 封装好的方法
    data_sql = '''
    select * from table_name limit 1000
    '''
    columns_list = ['id', 'timestamp', 'name']
    read_from_hive(data_sql, columns_list)

