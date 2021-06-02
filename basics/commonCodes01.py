#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   commonCodes01.py
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/6/2 10:16   SeafyLiang   1.0          20个常用代码案例1-10
"""
# 1、合并两个字典
"""
Python3.5之后，合并字典变得容易起来。我们可以通过**符号解压字典，并将多个字典传入{}中，实现合并。
"""


def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


# 两个字典
dict1 = {"name": "Joy", "age": 25}
dict2 = {"name": "Joy", "city": "New York"}
dict3 = Merge(dict1, dict2)
print("1、合并两个字典：", dict3)
# 2、链式比较
"""
python有链式比较的机制，在一行里支持多种运算符比较。相当于拆分多个逻辑表达式，再进行逻辑与操作。
"""
a = 5

print("2、链式比较：", 2 < a < 8)
print("2、链式比较：", 1 == a < 3)
# 3、重复打印字符串
"""
将一个字符串重复打印多次，一般使用循环实现，但有更简易的方式可以实现。
"""
n = 5
string = "Hello!"

print("3、重复打印字符串：", string * n)

# 4、检查文件是否存在
"""
我们知道Python有专门处理系统交互的模块-os，它可以处理文件的各种增删改查操作。
那如何检查一个文件是否存在呢？os模块可以轻松实现。
"""
from os import path


def check_for_file():
    print("4、检查文件是否存在：", "Does file exist:", path.exists("data.csv"))


check_for_file()
# 5、检索列表最后一个元素
"""
在使用列表的时候，有时会需要取最后一个元素，有下面几种方式可以实现。
"""
my_list = ['banana', 'apple', 'orange', 'pineapple']

# 索引方法
last_element = my_list[-1]

# pop方法
last_element = my_list.pop()

print("5、检索列表最后一个元素：", "last_element:%s, last_element:%s" % (last_element, last_element))

# 6、列表推导式
"""
列表推导式是for循环的简易形式，可以在一行代码里创建一个新列表，同时能通过if语句进行判断筛选
"""


def get_vowels(string):
    return [vowel for vowel in string if vowel in 'aeiou']


print("6、列表推导式：", "Vowels are:", get_vowels('This is some random string'))
# 7、计算代码执行时间
"""
python中time模块提供了时间处理相关的各种函数方法，我们可以使用它来计算代码执行的时间。
"""
import time

start_time = time.time()

total = 0
for i in range(10):
    total += i
print("7、计算代码执行时间：", "Sum:", total)

end_time = time.time()
time_taken = end_time - start_time
print("7、计算代码执行时间：", "Time: ", time_taken)
# 8、查找出现次数最多的元素
"""
使用max方法找出列表中出现次数最多的元素。
"""


def most_frequent(list):
    return max(set(list), key=list.count)


mylist = [1, 1, 2, 3, 4, 5, 6, 6, 2, 2]
print("8、查找出现次数最多的元素：", "出现次数最多的元素是:", most_frequent(mylist))
# 9、将两个列表转换为字典
"""
有两个列表，将列表A里的元素作为键，将列表B里的对应元素作为值，组成一个字典。
"""


def list_to_dictionary(keys, values):
    return dict(zip(keys, values))


list1 = [1, 2, 3]
list2 = ['one', 'two', 'three']

print("9、将两个列表转换为字典：", list_to_dictionary(list1, list2))
# 10、异常处理
"""
Python提供了try...except...finally的方式来处理代码异常，当然还有其他组合的方式。
"""
a, b = 1, 0

try:
    print("10、异常处理：", a / b)
except ZeroDivisionError:
    print("10、异常处理：", "Can not divide by zero")
finally:
    print("10、异常处理：", "Executing finally block")
