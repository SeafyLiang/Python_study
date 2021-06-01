#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   codeOptimization02.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021-06-01 16:55:47   SeafyLiang   1.0          代码优化05-08
"""
"""
5. 利用if条件的短路特性
"""
# 不推荐写法，代码耗时：0.05秒
from typing import List


def concatString(string_list: List[str]) -> str:
    abbreviations = {'cf.', 'e.g.', 'ex.', 'etc.', 'flg.', 'i.e.', 'Mr.', 'vs.'}
    abbr_count = 0
    result = ''
    for str_i in string_list:
        if str_i in abbreviations:
            result += str_i
    return result


def main():
    for _ in range(10000):
        string_list = ['Mr.', 'Hat', 'is', 'Chasing', 'the', 'black', 'cat', '.']
        result = concatString(string_list)


main()


# 推荐写法，代码耗时：0.03秒

def concatString(string_list: List[str]) -> str:
    abbreviations = {'cf.', 'e.g.', 'ex.', 'etc.', 'flg.', 'i.e.', 'Mr.', 'vs.'}
    abbr_count = 0
    result = ''
    for str_i in string_list:
        if str_i[-1] == '.' and str_i in abbreviations:  # 利用 if 条件的短路特性
            result += str_i
    return result


def main():
    for _ in range(10000):
        string_list = ['Mr.', 'Hat', 'is', 'Chasing', 'the', 'black', 'cat', '.']
        result = concatString(string_list)


main()

"""
6. 循环优化
"""
"""
6.1 用for循环代替while循环
"""


# 不推荐写法。代码耗时：6.7秒
def computeSum(size: int) -> int:
    sum_ = 0
    i = 0
    while i < size:
        sum_ += i
        i += 1
    return sum_


def main():
    size = 10000
    for _ in range(size):
        sum_ = computeSum(size)


main()


# 推荐写法。代码耗时：4.3秒
def computeSum(size: int) -> int:
    sum_ = 0
    for i in range(size):  # for 循环代替 while 循环
        sum_ += i
    return sum_


def main():
    size = 10000
    for _ in range(size):
        sum_ = computeSum(size)


main()

"""
6.2 使用隐式for循环代替显式for循环
"""


# 推荐写法。代码耗时：1.7秒
def computeSum(size: int) -> int:
    return sum(range(size))  # 隐式 for 循环代替显式 for 循环


def main():
    size = 10000
    for _ in range(size):
        sum = computeSum(size)


main()
"""
6.3 减少内层for循环的计算
"""
# 不推荐写法。代码耗时：12.8秒
import math


def main():
    size = 10000
    sqrt = math.sqrt
    for x in range(size):
        for y in range(size):
            z = sqrt(x) + sqrt(y)


main()


# 推荐写法。代码耗时：7.0秒

def main():
    size = 10000
    sqrt = math.sqrt
    for x in range(size):
        sqrt_x = sqrt(x)  # 减少内层 for 循环的计算
        for y in range(size):
            z = sqrt_x + sqrt(y)


main()

"""
7. 使用numba.jit
关于numba的更多信息见下面的主页：http://numba.pydata.org/numba.pydata.org
"""
# 推荐写法。代码耗时：0.62秒
import numba


@numba.jit
def computeSum(size: float) -> int:
    sum = 0
    for i in range(size):
        sum += i
    return sum


def main():
    size = 10000
    for _ in range(size):
        sum = computeSum(size)


main()

"""
8. 选择合适的数据结构

Python 内置的数据结构如str, tuple, list, set, dict底层都是 C 实现的，速度非常快，自己实现新的数据结构想在性能上达到内置的速度几乎是不可能的。

list类似于 C++ 中的std::vector，是一种动态数组。其会预分配一定内存空间，当预分配的内存空间用完，又继续向其中添加元素时，会申请一块更大的内存空间，然后将原有的所有元素都复制过去，之后销毁之前的内存空间，再插入新元素。

删除元素时操作类似，当已使用内存空间比预分配内存空间的一半还少时，会另外申请一块小内存，做一次元素复制，之后销毁原有大内存空间。

因此，如果有频繁的新增、删除操作，新增、删除的元素数量又很多时，list的效率不高。此时，应该考虑使用collections.deque。collections.deque是双端队列，同时具备栈和队列的特性，能够在两端进行 O(1) 复杂度的插入和删除操作。

list的查找操作也非常耗时。当需要在list频繁查找某些元素，或频繁有序访问这些元素时，可以使用bisect维护list对象有序并在其中进行二分查找，提升查找的效率。

另外一个常见需求是查找极小值或极大值，此时可以使用heapq模块将list转化为一个堆，使得获取最小值的时间复杂度是 O(1)。

下面的网页给出了常用的 Python 数据结构的各项操作的时间复杂度：https://wiki.python.org/moin/TimeComplexity
"""
