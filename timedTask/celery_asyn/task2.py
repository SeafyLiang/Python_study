#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   task2.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/6/29 09:36   SeafyLiang   1.0          None
"""
from timedTask.celery_asyn import app


@app.task
def multiply(x, y):
    print('Enter call function ...')
    return x * y
