#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   numba_speedup.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/4/4 22:48   SeafyLiang   1.0        numba加速python代码
"""
from numba import jit, njit, prange
import random
import numpy as np
import numba
import math
import time
"""
Numba 是一个开源的即时编译器（JIT compiler），可将 Python 和 NumPy 的代码的转换为快速的机器码，
从而提升运行速度。可以达到 C 或 FORTRAN 的速度。
只需将 Numba 提供的装饰器放在 Python 函数上面就行，剩下的就交给 Numba 完成。举个简单的例子：
"""


@jit(nopython=True)
def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples


"""
Numba 是专为科学计算而设计的，在与 NumPy 一起使用时，Numba 会为不同的数组数据类型生成专门的代码，以优化性能：
"""


@numba.jit(nopython=True, parallel=True)
def logistic_regression(Y, X, w, iterations):
    for i in range(iterations):
        w -= np.dot(((1.0 /
                      (1.0 + np.exp(-Y * np.dot(X, w)))
                      - 1.0) * Y), X)
    return w


"""
同样的代码，使用 Numba 前后与 C++ 的性能对比。比如说我们要找出 1000 万以内所有的素数，代码的算法逻辑是相同的：
"""


def is_prime1(num):
    if num == 2:
        return True
    if num <= 1 or not num % 2:
        return False
    for div in range(3, int(math.sqrt(num) + 1), 2):
        if not num % div:
            return False
    return True


def run_program1(N):
    total = 0
    for i in range(N):
        if is_prime1(i):
            total += 1
    return total


# 加速前
def before_speedup():
    """
    total prime num is 664579
    cost 50.615642070770264s
    """
    N = 10000000
    start = time.time()
    total = run_program1(N)
    end = time.time()
    print(f"total prime num is {total}")
    print(f"cost {end - start}s")


"""
现在我们使用 Numba 来加速一下，操作很简单，不需要改动原有的代码，先导入 Numba 的 njit，再在函数上方放个装饰器 @njit 即可，其他保持不变
"""


# @njit 相当于 @jit(nopython=True)
@njit
def is_prime2(num):
    if num == 2:
        return True
    if num <= 1 or not num % 2:
        return False
    for div in range(3, int(math.sqrt(num) + 1), 2):
        if not num % div:
            return False
    return True


@njit
def run_program2(N):
    total = 0
    for i in range(N):
        if is_prime2(i):
            total += 1
    return total


# 使用numba代码加速（未使用并行计算）
def after_speedup_one():
    """
    total prime num is 664579
    cost 2.849954128265381s
    """
    N = 10000000
    start = time.time()
    total = run_program2(N)
    end = time.time()
    print(f"total prime num is {total}")
    print(f"cost {end - start}s")


"""
相比 C++ 的 2.3 秒还是有一点慢,还有优化的空间，就是 Python 的 for 循环，
那可是 1000 万的循环，对此，Numba 提供了 prange 参数来并行计算，从而并发处理循环语句，
只需要将 range 修改为 prange，装饰器传个参数：parallel = True，其他不变
"""


@njit
def is_prime3(num):
    if num == 2:
        return True
    if num <= 1 or not num % 2:
        return False
    for div in range(3, int(math.sqrt(num) + 1), 2):
        if not num % div:
            return False
    return True


@njit(parallel=True)
def run_program3(N):
    total = 0
    for i in prange(N):
        if is_prime3(i):
            total += 1
    return total


# 使用numba代码加速（for循环使用并行计算优化）
def after_speedup_final():
    """
    total prime num is 664579
    cost 1.0952420234680176s
    """
    N = 10000000
    start = time.time()
    total = run_program3(N)
    end = time.time()
    print(f"total prime num is {total}")
    print(f"cost {end - start}s")


"""
Numba 如何做到的呢？官方文档这样介绍：它读取装饰函数的 Python 字节码，并将其与有关函数输入参数类型的信息结合起来，
分析和优化代码，最后使用编译器库（LLVM）针对你的 CPU 生成量身定制的机器代码。每次调用函数时，都会使用此编译版本
"""

if __name__ == '__main__':
    print("c++费时2.3s")
    print("未优化版本：")
    before_speedup()
    print("优化版本1.0（未使用并行计算）:")
    after_speedup_one()
    print("优化最终版本（使用并行计算）:")
    after_speedup_final()
    """
    c++费时2.3s
    未优化版本：
    total prime num is 664579
    cost 49.31721901893616s
    优化版本1.0（未使用并行计算）:
    total prime num is 664579
    cost 2.8343091011047363s
    优化最终版本（使用并行计算）:
    total prime num is 664579
    cost 0.8934330940246582s
    """
