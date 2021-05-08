#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   progressBar.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/4/27 09:08   SeafyLiang   1.0         进度条
"""
from progress.bar import Bar
import time

bar = Bar('Processing', max=2000)
for i in range(2000):
    # time.sleep(100)
    # Do some work
    bar.next()
bar.finish()