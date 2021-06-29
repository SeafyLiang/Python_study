#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   celeryconfig.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/6/29 09:34   SeafyLiang   1.0          参数配置文件
"""
from datetime import timedelta
from celery.schedules import crontab

# 参数配置文件celeryconfig.py
BROKER_URL = 'redis://127.0.0.1:6379/1'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'
CELERY_TIMEZONE = "Asia/shanghai"  # 默认UTC
CELERY_RESULT_SERIALIZER = 'msgpack'

# 导入指定的任务模块
CELERY_IMPORTS = (
    'timedTask.celery_asyn.task1',
    'timedTask.celery_asyn.task2',
)

# 设置定时任务
CELERYBEAT_SCHEDULE = {
    # 每过10秒执行以下task1.add的定时任务
    'task1': {
        'task': 'timedTask.celery_asyn.task1.add',
        'schedule': timedelta(seconds=10),
        'args': (2, 8)
    },
    # 等到22点18分执行task2的multiply
    'task2': {
        'task': 'timedTask.celery_asyn.task2.multiply',
        'schedule': crontab(hour=22, minute=20),
        'args': (4, 5)
    }
}
