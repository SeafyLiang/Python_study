#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   task.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/6/29 09:14   SeafyLiang   1.0          None
"""
import time
from celery import Celery

# 实例化一个Celery
# broker = 'redis://localhost:6379/1'
# backend = 'redis://localhost:6379/2'

# 假如本地有redis，那就localhost，
# 假如没有，我提供我服务器的redis
# 请各位好汉，不要暴力刷数据。。。
broker = 'redis://127.0.0.1:6379/1'
backend = 'redis://127.0.0.1:6379/2'

# 参数1 自动生成任务名的前缀
# 参数2 broker 是我们的redis的消息中间件
# 参数3 backend 用来存储我们的任务结果的
app = Celery('my_task', broker=broker, backend=backend)


# 加入装饰器变成异步的函数
@app.task
def add(x, y):
    print('Enter call function ...')
    time.sleep(4)
    return x + y


if __name__ == '__main__':
    # 这里生产的任务不可用，导入的模块不能包含task任务。会报错
    print("Start Task ...")
    result = add.delay(2, 8)
    print("result:", result)
    print("End Task ...")
