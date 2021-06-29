#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   result.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/6/29 09:36   SeafyLiang   1.0          根据反馈的id查询结果
"""
from celery.result import AsyncResult
from celery_asyn import app

async_result = AsyncResult(id="7628bc40-16df-4eee-b22e-fc1de9911513", app=app)

if async_result.successful():
    result = async_result.get()
    print(result)
    # result.forget() # 将结果删除
elif async_result.failed():
    print('执行失败')
elif async_result.status == 'PENDING':
    print('任务等待中被执行')
elif async_result.status == 'RETRY':
    print('任务异常后正在重试')
elif async_result.status == 'STARTED':
    print('任务已经开始被执行')
