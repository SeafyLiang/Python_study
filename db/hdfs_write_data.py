#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   hdfs_write_data.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/8/1 11:35   SeafyLiang   1.0       向hdfs写入数据表
"""
from hdfs import InsecureClient
import pandas as pd


def getHDFSConn():
    '''
    获取HDFS连接
    '''
    client = None
    url = "http://uuuuurrrrrllll:1234"
    user = 'username'
    try:
        client = InsecureClient(url, user)
    except Exception as e:
        print(e)
    return client


def appendWriteDFtoHDFS(client, hdfs_path, local_path_datasimba):
    '''
    追加DF数据到hdfs文件
    '''
    client.makedirs(hdfs_path)
    client.upload(hdfs_path, local_path_datasimba, cleanup=True)


df = pd.DataFrame({
    'column_a': [1, 2, 3],
    'column_b': [1, 2, 3]
})
# 压缩数据到本地二进制文件
df.to_parquet('data/00000_0')
# 获取hdfs连接
client = getHDFSConn()
hdfs_path = '/data/hive/warehouse/'
print(hdfs_path)
local_path_datasimba = 'data/00000_0'
# 写入hdfs文件
appendWriteDFtoHDFS(client, hdfs_path, local_path_datasimba)
