#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   automation.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/3/30 22:31   SeafyLiang   1.0        10个常用的自动化
"""
import os

"""
一、遍历文件夹
批量操作的前提就是对文件夹进行遍历，使用os模块可以轻松的遍历文件夹，os.walk 遍历后产生三个参数：
“
当前文件夹路径
包含文件夹名称[列表形式]
包含文件名称[列表形式]
"""
for dirpath, dirnames, filenames in os.walk(
        r'/Users/seafyliang/DEV/Code_projects/Python_projects/Python_study_github/scriptPython'):
    print(f'打开文件夹{dirpath}')  # 当前文件夹路径
    if dirnames:
        print(dirnames)  # 包含文件夹名称[列表形式]
    if filenames:
        print(filenames)  # 包含文件名称[列表形式]
    print('-' * 10)

"""
二、 目标路径是否是文件
有时我们需要判断一个目录下是否存在文件也可以使用os模块。
给定一个目标路径 path ，通过一行代码就能够判断这是文件还是文件夹路径
"""
path = 'automation.py'
print(os.path.isfile(path))

"""
三、获取路径中的文件名
os.path.basename 可以直接从绝对路径中获取最后的文件名，当然如果用传统的字符串切割方式也可以，即 path.split('\\')[-1]
"""
path = 'automation.py'
print(os.path.basename)

"""
四、创建文件夹
创建文件夹的代码非常常用，因为往往生成的新文件都希望有个新的文件夹存储
"""
# dirpath = 'test'
# os.mkdir(dirpath)
"""
但是，如果希望创建的文件夹已经存在，再运行 os.mkdir() 则会报错而终止代码。为了避免这一情况的发生，可以在创建文件夹之前先判断文件夹是否存在。
用到的代码是 os.path.exists，只有当路径不存在（即  os.path.exists 返回的结果是 False 时），才会创建：
"""
dirpath = 'test'
if not os.path.exists(dirpath):
    os.mkdir(dirpath)

"""
五、获取桌面路径
获取桌面路径也是非常常用的操作，可以使用os.path.join(os.path.expanduser("~"), 'Desktop') 获取桌面的绝对路径。
这样做的好处是可以把数据放在桌面上，在不同的电脑上都能调用代码对数据进行处理。
如果是在一条电脑上把桌面路径固定在字符串中，则换一台电脑就必须修改桌面路径。
"""
desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')
print(desktop_path)


# 当然把上面的代码包装成一个函数 GetDesktopPath() 需要时调用它会更加方便
def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')


"""
六、重命名文件/文件夹
需要用到 os.rename() 方法，下面的代码示例中分别演示如何重命名文件和文件夹
"""
os.rename('practice.txt', 'practice.txt')  # 重命名文件
os.rename('test', 'test2')  # 重命名文件夹


"""
七、批处理文件 - 1
除了前面的 os.walk 之外，有其他的 os 模块下方法可完成获取指定路径的全部或符合条件的文件（非遍历各级文件夹的需求），
还可以使用下面两个代码 第一种用到的方法是os.scandir()
"""
path = '../'
for file in os.scandir(path):
    print(file.name, file.path)


"""
八、批处理文件 - 2
上面代码最后输出的是 给定路径下各内容的名字、绝对路径第二种方法使用 os.listdir()，
它比 os.scandir() 简单一些，可直接调用输出名称而非路径：
"""
path = '.'
for file in os.listdir(path):
    print(file)


"""
九、移动文件/文件夹
shutil也是经常出现在办公自动化场景中的模块，我常用的就是移动文件/文件夹。
需要用到shutil.move 方法，下面的代码示例中分别演示如何移动文件和文件夹：
"""
import shutil

shutil.move(r'./practice.txt', r'./test2/')
shutil.move(r'./practice.txt', r'./test/new.txt')
"""
注意到上面后两行代码的区别吗？前一行是将目标文件移动到目标文件夹里，而后一行，在将目标文件移动到目标文件夹里的同时，能够对其进行重命名
也就是说，如果我们需要移动某个或某些文件到新的文件夹，并且需重命名文件，
则我们并不需要用 os.rename 先命名文件再用 shutil.move 将其移动的指定文件夹，而是可以用 shutil.move 一步到位
"""


"""
十、批处理文件 - 3
最后要介绍的是glob模块，也是办公自动化必须要掌握的一个模块，同样可以用于批处理文件。
glob 最重要的功能就是搜索获取同一级或者各子级下符合条件的文件（绝对路径），非常适合写批处理的代码。
有时候我们需要对大量文件进行相同操作，在写完针对一份文件的操作后，只需要加上几行代码，就可以完成批处理全部文件的工作。
"""
import glob

for file in glob.glob('**/*', recursive=True):
    print(file)
"""
glob.glob() 是一个非常重要的方法，能够获取给定路径下文件的绝对路径，并且接受「通配符」搜索，大大拓宽了灵活程度，
* 表示任意字符长度，**/* 的使用表示用通配符指代给定路径下的任何一层，recursive 参数允许遍历搜索。
"""