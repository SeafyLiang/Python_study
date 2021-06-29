#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   produce.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/6/29 09:37   SeafyLiang   1.0          执行任务
"""
from task1 import add  # 在这里我只调用了task1

if __name__ == '__main__':
    print("Start Task ...")
    re = add.delay(7, 5)
    print(re.id)
    print(re.status)
    print(re.get())
    print("End Task ...")
