#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   with.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/4/22 11:14   SeafyLiang   1.0       with语句在进行异常处理时代码简洁很多
"""
"""
with语句处理异常
    我们知道使用try-except-finally语句可以处理异常，接下来我们介绍使用with语句处理与异常相关的工作
    with语句支持创建资源，抛出异常，释放资源等操作，并且代码简洁。
with语句格式
    with 上下文表达式 [as 资源对象]： 对象操作 说明：
        上下文表达式，返回一个上下文管理对象
        如果指定了as语句，该对象并不赋值给as子句中的资源对象，而是将上下文管理器的__enter__()方法的返回值赋值给了资源对象。
        资源对象可以是单变量，也可以是元组。
使用with语句操作文件对象
"""
with open("test.txt") as file:
    for aline in file:
        print(aline)

"""
解释说明： 这段代码使用with语句打开文件，如果顺利打开，则将文件对象赋值给file，然后用for语句遍历打印文件的每一行。
当文件操作结束后，with语句关闭文件。如果这段代码运行过程中发生异常，with也会将文件关闭。

这段代码使用finally语句实现如下:
"""
try:
    file = open("test.txt")
    try:
        for aline in file:
            print(aline)
    except Exception as error:
        print(error)
    finally:
        file.close()
except FileNotFoundError as err:
    print(err)
"""
我们也可以给with语句加上异常处理：
"""
try:
    with open("test.txt") as file:
        for aline in file:
            print(aline)
except Exception as error:
    print(error)
"""
通过对比可以发现：with语句在进行异常处理时代码简洁很多
特别说明：
    不是所有的对象都可以使用with语句，只有支持上下文管理协议的对象才可以。目前支持上下文管理协议的对象如下：
"""
# file
# decimal.Context
# thread.LockType
# threading.BoundedSemaphore
# threading.Condition
# threading.Lock
# threading.RLock
# threading.Semaphore
