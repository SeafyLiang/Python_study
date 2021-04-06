#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   commonFunctions.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/4/6 21:49   SeafyLiang   1.0          5个常用函数
"""

"""
01
Lambda 函数
Lambda 函数是一种比较小的匿名函数——匿名是指它实际上没有函数名。
Python 函数通常使用 def a_function_name() 样式来定义，但对于 lambda 函数，我们根本没为它命名。这是因为 lambda 函数的功能是执行某种简单的表达式或运算，而无需完全定义函数。
lambda 函数可以使用任意数量的参数，但表达式只能有一个。
"""
x = lambda a, b: a * b
print(x(5, 6))  # prints  30

x = lambda a: a * 3 + 3
print(x(3))  # prints  12

"""
02
Map 函数
Map() 是一种内置的 Python 函数，它可以将函数应用于各种数据结构中的元素，如列表或字典。
对于这种运算来说，这是一种非常干净而且可读的执行方式。
"""


def square_it_func(a):
    return a * a


x = map(square_it_func, [1, 4, 7])
print(x)  # prints  [1, 16, 47]


def multiplier_func(a, b):
    return a * b


x = map(multiplier_func, [1, 4, 7], [2, 5, 8])
print(x)  # prints  [2, 20, 56] 看看上面的示例！可以将函数应用于单个或多个列表。实际上，你可以使用任何 Python 函数作为 map 函数的输入，只要它与你正在操作的序列元素是兼容的。

"""
03 filter函数
filter 内置函数与 map 函数非常相似，它也将函数应用于序列结构（列表、元组、字典）。
二者的关键区别在于 filter() 将只返回应用函数返回 True 的元素。

"""
# Our numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


# Function that filters out all numbers which are odd
def filter_odd_numbers(num):
    if num % 2 == 0:
        return True
    else:
        return False


filtered_numbers = filter(filter_odd_numbers, numbers)

print(filtered_numbers)
# filtered_numbers = [2, 4, 6, 8, 10, 12, 14]

"""
04
Itertools 模块
Python 的 Itertools 模块是处理迭代器的工具集合。迭代器是一种可以在 for 循环语句（包括列表、元组和字典）中使用的数据类型。
使用 Itertools 模块中的函数让你可以执行很多迭代器操作，这些操作通常需要多行函数和复杂的列表理解。
"""
from itertools import count

"""
无穷的迭代器 count(start,[step])
count()接受两个参数
start:循环开始的数字
step:循环中的间隔
"""
c = count(0, 2)
v = next(c)
while v < 10:
    v = next(c)
    print(v, end=',')

"""
无穷迭代器 cycle() 
cycle就是一while True，无限循环里面的数字。
"""
from itertools import cycle

c = cycle('ABCD')
for i in range(10):
    print(next(c), end=',')

"""
无穷迭代器 repeat(elem,[n])
重复迭代elem，n次
"""
from itertools import repeat

r = repeat(1, 3)
for i in range(3):
    print(next(r), end=',')

"""
05
Generator 函数
Generator 函数是一个类似迭代器的函数，即它也可以用在 for 循环语句中。这大大简化了你的代码，而且相比简单的 for 循环，它节省了很多内存。
生成器
在 Python 中，使用了 yield 的函数被称为生成器（generator）。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
调用一个生成器函数，返回的是一个迭代器对象。
以下实例使用 yield 实现斐波那契数列：
"""
import sys


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
