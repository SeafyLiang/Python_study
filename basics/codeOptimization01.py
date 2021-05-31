#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   codeOptimization01.py
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/5/31 15:11   SeafyLiang   1.0         代码优化01-04
"""

"""
1. 避免全局变量
"""
# 不推荐写法。代码耗时：26.8秒
import math

size = 10000
for x in range(size):
    for y in range(size):
        z = math.sqrt(x) + math.sqrt(y)


# 推荐写法。代码耗时：20.6秒
def main():  # 定义到函数中，以减少全部变量使用
    size = 10000
    for x in range(size):
        for y in range(size):
            z = math.sqrt(x) + math.sqrt(y)


main()

"""
2. 避免.
"""
"""
2.1 避免模块和函数属性访问
"""


# 不推荐写法。代码耗时：14.5秒

def computeSqrt(size: int):
    result = []
    for i in range(size):
        result.append(math.sqrt(i))
    return result


def main():
    size = 10000
    for _ in range(size):
        result = computeSqrt(size)


main()

# 第一次优化写法。代码耗时：10.9秒
from math import sqrt


def computeSqrt(size: int):
    result = []
    for i in range(size):
        result.append(sqrt(i))  # 避免math.sqrt的使用
    return result


def main():
    size = 10000
    for _ in range(size):
        result = computeSqrt(size)


main()


# 第二次优化写法。代码耗时：9.9秒

def computeSqrt(size: int):
    result = []
    sqrt = math.sqrt  # 赋值给局部变量
    for i in range(size):
        result.append(sqrt(i))  # 避免math.sqrt的使用
    return result


def main():
    size = 10000
    for _ in range(size):
        result = computeSqrt(size)


main()


# 推荐写法。代码耗时：7.9秒

def computeSqrt(size: int):
    result = []
    append = result.append
    sqrt = math.sqrt  # 赋值给局部变量
    for i in range(size):
        append(sqrt(i))  # 避免 result.append 和 math.sqrt 的使用
    return result


def main():
    size = 10000
    for _ in range(size):
        result = computeSqrt(size)


main()

"""
2.2 避免类内属性访问
"""
# 不推荐写法。代码耗时：10.4秒
from typing import List


class DemoClass:
    def __init__(self, value: int):
        self._value = value

    def computeSqrt(self, size: int) -> List[float]:
        result = []
        append = result.append
        sqrt = math.sqrt
        for _ in range(size):
            append(sqrt(self._value))
        return result


def main():
    size = 10000
    for _ in range(size):
        demo_instance = DemoClass(size)
        result = demo_instance.computeSqrt(size)


main()


# 推荐写法。代码耗时：8.0秒


class DemoClass:
    def __init__(self, value: int):
        self._value = value

    def computeSqrt(self, size: int) -> List[float]:
        result = []
        append = result.append
        sqrt = math.sqrt
        value = self._value
        for _ in range(size):
            append(sqrt(value))  # 避免 self._value 的使用
        return result


def main():
    size = 10000
    for _ in range(size):
        demo_instance = DemoClass(size)
        demo_instance.computeSqrt(size)


main()

"""
3. 避免不必要的抽象
"""


# 不推荐写法，代码耗时：0.55秒
class DemoClass:
    def __init__(self, value: int):
        self.value = value

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, x: int):
        self._value = x


def main():
    size = 1000000
    for i in range(size):
        demo_instance = DemoClass(size)
        value = demo_instance.value
        demo_instance.value = i


main()


# 推荐写法，代码耗时：0.33秒
class DemoClass:
    def __init__(self, value: int):
        self.value = value  # 避免不必要的属性访问器


def main():
    size = 1000000
    for i in range(size):
        demo_instance = DemoClass(size)
        value = demo_instance.value
        demo_instance.value = i


main()

"""
4. 避免数据复制
"""
"""
4.1 避免无意义的数据复制
"""


# 不推荐写法，代码耗时：6.5秒
def main():
    size = 10000
    for _ in range(size):
        value = range(size)
        value_list = [x for x in value]
        square_list = [x * x for x in value_list]


main()


# 推荐写法，代码耗时：4.8秒
def main():
    size = 10000
    for _ in range(size):
        value = range(size)
        square_list = [x * x for x in value]  # 避免无意义的复制


main()

"""
4.2 交换值时不使用中间变量
"""


# 不推荐写法，代码耗时：0.07秒
def main():
    size = 1000000
    for _ in range(size):
        a = 3
        b = 5
        temp = a
        a = b
        b = temp


main()


# 推荐写法，代码耗时：0.06秒
def main():
    size = 1000000
    for _ in range(size):
        a = 3
        b = 5
        a, b = b, a  # 不借助中间变量


main()

"""
4.3 字符串拼接用join而不是+
"""
# 不推荐写法，代码耗时：2.6秒
import string
from typing import List


def concatString(string_list: List[str]) -> str:
    result = ''
    for str_i in string_list:
        result += str_i
    return result


def main():
    string_list = list(string.ascii_letters * 100)
    for _ in range(10000):
        result = concatString(string_list)


main()


# 推荐写法，代码耗时：0.3秒

def concatString(string_list: List[str]) -> str:
    return ''.join(string_list)  # 使用 join 而不是 +


def main():
    string_list = list(string.ascii_letters * 100)
    for _ in range(10000):
        result = concatString(string_list)


main()
