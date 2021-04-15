#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   pyquery_study.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/4/15 11:05   SeafyLiang   1.0          None
"""
from pyquery import PyQuery as pq

# PyQuery是强大而又灵活的网页解析库，如果你觉得正则写起来太麻烦，如果你觉得BeautifulSoup语法太难记，如果你熟悉jQuery的语法
# 那么，PyQuery就是你绝佳的选择。

# 1. 初始化方式，有三种，可以传入字符串，传入url，传入文件。
# 1.1 字符串初始化
html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

doc = pq(html)  # 声明pq对象
print('1.1 字符串初始化:', doc('li'))  # 用css选择器来实现，如果要选id前面加#，如果选class，前面加.，如果选标签名，什么也不加

# 1.2 URL初始化
# 也可以直接传入URL，进行URL初始化，程序会自动请求URL，获得html并返回要查找的字符串
doc = pq(url='http://www.baidu.com')  # 程序会自动请求url
print('1.2 URL初始化:', doc('head'))  # 返回head标签

# 1.3 文件初始化
doc = pq(filename='demo.html')  # 直接传入文件名称及路径，程序会自动寻找并请求
print('1.3 文件初始化:', doc('li'))

# 2.基本css选择器
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
doc = pq(html)
print('2.基本css选择器:', doc('#container .list li'))  # 会查找id为container class为list，标签为li的对象，只是层级关系，没有后者一定是前者的子对象

# 查找元素

# 2.1子元素
items = doc('.list')  # 拿到items
print('2.1子元素:', type(items))
print('2.1子元素:', items)
lis = items.find('li')  # 利用find方法，查找items里面的li标签，得到的lis也可以继续调用find方法往下查找，层层剥离
print('2.1子元素:', type(lis))
print('2.1子元素:', lis)

# 2.2 也可以用.children()查找直接子元素
lis = items.children()
print('2.2 也可以用.children()查找直接子元素:', type(lis))
print('2.2 也可以用.children()查找直接子元素:', lis)
lis = items.children('.active')
print('2.2 也可以用.children()查找直接子元素:', lis)

# 2.3 父元素
items = doc('.list')
container = items.parent()  # .parent()查找对象的父元素
print('2.3 父元素:', type(container))
print('2.3 父元素:', container)

# 2.4 祖先节点
parents = items.parents()  # .parents（）祖先节点
parent = items.parents('.wrap')  # 当然也可以传入参数
print('2.4 祖先节点:', parent)

# 2.5 兄弟元素
li = doc('.list .item-0.active')  # 空格表示里面，没有空格表示整体
print('2.5 兄弟元素:', li.siblings())  # .siblings()兄弟元素，即同级别的元素，不包括自己

# 3. 遍历
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
lis = doc('li').items()  # .items会是一个生成器
print('3. 遍历:', type(lis))
for li in lis:
    print('3. 遍历:', li)

# 4. 获取信息
# 4.1 获取属性
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
a = doc('.item-0.active a')
print('4.1 获取属性:', a)
# 定义a标签的href属性用于指定超链接目标的URL。
# 如果用户选择了a标签中的内容，那么浏览器会尝试检索并显示href属性指定的URL所表示的文档，或者执行JavaScript表达式、方法和函数的列表。
print('4.1 获取属性:', a.attr('href'))
print('4.1 获取属性:', a.attr.href)

# 4.2 获取文本
a = doc('.item-0.active a')
print('4.2 获取文本:', a)
print('4.2 获取文本:', a.text())  # .text()获取文本信息

# 4.3 获取html
li = doc('.item-0.active')
print('4.3 获取html:', li)
print('4.3 获取html:', li.html())  # .html（）获取所在html


# 5. DOM操作

# 5.1 addClass、removeClass
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
li = doc('.item-0.active')
print('5.1 addClass、removeClass:', li)
li.removeClass('active')  # 删除
print('5.1 addClass、removeClass:', li)
li.addClass('active')  # 增加
print('5.1 addClass、removeClass:', li)

# 5.2 attr、css
li = doc('.item-0.active')
print('5.2 attr、css:', li)
li.attr('name', 'link')  # 增加一个属性
print('5.2 attr、css:', li)
li.css('font-size', '14px')  # 增加一个css
print('5.2 attr、css:', li)

# 5.3 remove
html = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
 </div>
'''
doc = pq(html)
wrap = doc('.wrap')
print('5.3 remove:', wrap.text())
wrap.find('p').remove()  # 找到p标签然后删除
print('5.3 remove:', wrap.text())

