#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   task1.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/6/29 09:35   SeafyLiang   1.0          None
"""
from timedTask.celery_asyn import app


# 加入装饰器变成异步的函数
@app.task
def add(x, y):
    print('Enter call function ...')
    return x + y
