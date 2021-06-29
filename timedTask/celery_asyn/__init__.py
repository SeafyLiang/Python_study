#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/6/29 09:52   SeafyLiang   1.0          None
"""
from celery import Celery

app = Celery('demo')

app.config_from_object('celery_asyn.celeryconfig')  # 通过celery 实例加载配置文件
