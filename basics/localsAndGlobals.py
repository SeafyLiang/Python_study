#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   localsAndGlobals.py
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/4/18 22:00   SeafyLiang   1.0        动态创建变量
"""

# 动态生成10个变量，如a1,a2,...,a10

# 使用的方法是Python内置函数locals()，它返回一个字典，记录着当前所有局部变量。动态生成10个变量a1,a2,...,a10，可以写为：
ld = locals()
for i in range(1, 11):
    ld['a' + str(i)] = i  # 默认值设置为i

print(a1)  # 1
print(a2)  # 2


# locals用于创建局部变量，如果想封装上面几行代码为一个函数，
# 使用locals动态创建变量后，只能在函数内部访问，外面就不能访问到了。
# 另外一个globals函数因为创建的是全局变量，所以得使用它。
def dynamic_variable(n, variable_prefix='a'):
    for i in range(1, n + 1):
        gd = globals()
        gd[variable_prefix + str(i)] = i  # 新创建的n个变量，初始值都设置为0


# 调用方法dynamic_variable(10,'v')后，我们便可以引用变量v1,v2,... v10：
dynamic_variable(10, 'v')
print(v6)  # 6
print(v10)  # 10
