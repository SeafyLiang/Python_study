#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   multiprocess_study.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/2/8 17:37   SeafyLiang   1.0        python多线程学习
"""
import urllib.request
from multiprocessing.dummy import Pool as ThreadPool

from functools import wraps
import time


def func_timer(function):
    '''
    用装饰器实现函数计时
    :param function: 需要计时的函数
    :return: None
    '''

    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print('[Function: {name} finished, spent time: {time:.2f}s]'.format(name=function.__name__, time=t1 - t0))
        return result

    return function_timer


urls = [
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com',

    # etc..
]


@func_timer
def singleThread():
    results = []
    for url in urls:
        result = urllib.request.urlopen(url)
        results.append(result)
    print('Thread-single')


@func_timer
def pool(n):
    pool = ThreadPool(n)
    # Open the urls in their own threads
    # and return the results
    results = pool.map(urllib.request.urlopen, urls)
    print('Thread-%s' % str(n))


if __name__ == '__main__':
    singleThread()
    pool(4)
    pool(8)
    pool(12)
