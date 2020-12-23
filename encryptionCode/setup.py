# coding=utf-8
# @Time : 2020/12/23 10:21 
# @Author : SeafyLiang 
# @Version：V 0.1
# @File : setup.py
# @desc :


from distutils.core import setup
from Cython.Build import cythonize

setup(name='Hello World app',
     ext_modules=cythonize('hello.py'))