#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   check.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/6/29 09:30   SeafyLiang   1.0          None
"""
from celery.result import AsyncResult
from task import app

async_result = AsyncResult(id="40d01758-32df-4f6a-ab83-32a7cf076bf0", app=app)

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
