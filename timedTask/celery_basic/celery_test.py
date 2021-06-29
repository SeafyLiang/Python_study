#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   celery_test.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/6/29 09:13   SeafyLiang   1.0          python使用celery
"""
from task import add

if __name__ == '__main__':
    print("Start Task ...")
    result = add.delay(2, 8)
    print("result:", result)  # 存到redis之后，返回的id
    print("result_id:", result.id)  # 存到redis之后，返回的id
    print("result:", result.get())  # 方法返回值
    print("End Task ...")

# celery -A task worker -l info
