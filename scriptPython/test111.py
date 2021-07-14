#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test111.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/7/1 16:56   SeafyLiang   1.0          None
"""

import os

for dirpath, dirnames, filenames in os.walk(
        r'/Users/seafyliang/DEV/FaceDetect'):
    # print(f'打开文件夹{dirpath}')  # 当前文件夹路径
    os.chdir("/Users/seafyliang/DEV/FaceDetect")
    if dirnames:
        print(dirnames)  # 包含文件夹名称[列表形式]
    if filenames:
        for i in filenames:
            print(i)  # 包含文件名称[列表形式]

            dirname = str(i).split('.')[0]
            os.mkdir(dirname)
            os.system('mv %s %s ' % (i, dirname))

    print('-' * 10)
