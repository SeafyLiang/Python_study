#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   except_handle.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/12/27 16:59   SeafyLiang   1.0        python异常处理
"""
"""
Python的异常处理可以向用户准确反馈出错信息，所有异常都是基类Exception的子类。
自定义异常都是从基类Exception中继承，Python自动将所有内建的异常放到内建命名空间中
所以程序不必导入exceptions模块即可使用异常。
需要查看详细的错误信息需导入import traceback模块
"""
import traceback
import sys


# # 1、捕获所有异常
# try:
#     1 / 0
# except Exception:
#     print (Exception)
# """输出异常类<class 'Exception'>"""
#
# # 2、采用traceback模块查看异常，需要导入traceback模块，这个方法会打印出异常代码的行号
# try:
#     1 / 0
# except:
#     traceback.print_exc()
# """输出：
# Traceback (most recent call last):
#   File "C:/Users/Administrator/Desktop/demo04.py", line 123, in <module>
#     1/0
# ZeroDivisionError: division by zero
# """
#
# # 3、采用sys模块回溯最后的异常
# try:
#     1 / 0
# except:
#     info = sys.exc_info()
#     print(info)
#     print(info[0])
#     print(info[1])
#
# """输出
# (<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero',), <traceback object at 0x000001D3E9FF62C8>)
# <class 'ZeroDivisionError'>
# division by zero
# """

# 获取函数名和行号
def get_cur_info():
    """Return the frame object for the caller's stack frame."""
    try:
        raise Exception
    except:
        f = sys.exc_info()[2].tb_frame.f_back
    return f.f_code.co_name, f.f_lineno


# 获取异常信息
def get_exception_info():
    try:
        1 / 0
    except Exception, e:
        print 'str(Exception):\t', str(Exception)
        print 'str(e):\t\t', str(e)
        print 'repr(e):\t', repr(e)
        print 'e.message:\t', e.message
        print 'traceback.print_exc():'
        traceback.print_exc()
        print 'traceback.format_exc():\n%s' % traceback.format_exc()


def callfunc():
    # print(get_cur_info())
    get_exception_info()


if __name__ == '__main__':
    callfunc()
