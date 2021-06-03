#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   commonCodes02.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/6/2 10:29   SeafyLiang   1.0          20个常用代码案例11-20
"""
# 11、反转字符串
"""
使用切片操作对字符串进行反转，这是比较直接有效的方式。这也可以用来检测回文数。
"""
str = "Hello World"

print("11、反转字符串：", "反转后字符串是:", str[::-1])

# 12、字符串列表组成单个字符串
"""
使用join方法将字符串列表组成单个字符串。
"""

list = ["Hello", "world", "Ok", "Bye!"]
combined_string = " ".join(list)

print("12、字符串列表组成单个字符串：", combined_string)

# 13、返回字典缺失键的默认值
"""
字典中的get方法用于返回指定键的值，如果键不在字典中返回默认值 None 或者设置的默认值。
"""

dict = {1: 'one', 2: 'two', 4: 'four'}

# returning three as default value
print(dict.get(3, 'three'))

print("13、返回字典缺失键的默认值：", "原始字典:", dict)
# 14、交换两个变量的值
"""
在不使用临时变量的前提下，交换两个变量的值。
"""
a, b = 5, 10

# 方法1
a, b = b, a


# 方法2
def swap(a, b):
    return b, a


swap(a, b)
# 15、正则表达式
"""
正则表达式用来匹配处理字符串，python中的re模块提供了全部的正则功能。
"""

import re

text = "The rain in spain"
result = re.search("rain", text)

print("15、正则表达式：", True if result else False)
# 16、筛选值
"""
python中的filter方法可以用来进行值的筛选。
"""
my_list = [0, 1, 2, 3, 6, 7, 9, 11]

result = filter(lambda x: x % 2 != 0, my_list)

# print("16、筛选值：", my_list(result))
# 17、统计字频
"""
判断字符串每个元素出现的次数，可以用collections模块中的Counter方法来实现，非常简洁。
"""
from collections import Counter

result = Counter('banana')
print("17、统计字频：", result)
# 18、变量的内存占用
"""
如何输出python中变量的内存占用大小，可以通过sys模块来实现。
"""
import sys

var1 = 15
list1 = [1, 2, 3, 4, 5]

print("18、变量的内存占用：", sys.getsizeof(var1))
print("18、变量的内存占用：", sys.getsizeof(list1))

# 19、链式函数调用
"""
在一行代码中调用多个函数。
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


a, b = 5, 10

print("19、链式函数调用：", (add if b > a else subtract)(a, b))
# 20、从列表中删除重复项
"""
删除列表中重复项一般可以通过遍历来筛选去重，或者直接使用集合方法。
"""

list1 = [1, 2, 3, 3, 4, 'John', 'Ana', 'Mark', 'John']


# 方法1
# def remove_duplicate(list_value):
#     return list(set(list_value))


# print("20、从列表中删除重复项：", remove_duplicate(list1))

# 方法2
result = []
[result.append(x) for x in list1 if x not in result]
print("20、从列表中删除重复项：", result)
