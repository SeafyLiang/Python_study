#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   pyAutoGUI_test.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/6/22 16:41   SeafyLiang   1.0          pyautogui自动化操作
"""
import pyautogui as pag

"""
参考资料：
https://mp.weixin.qq.com/s/nLYFXn59xa4h7dykzT_pYw
https://blog.csdn.net/qq_43017750/article/details/90575240
"""

"""
first try
"""
# # 定义每步骤暂停时间为1.5s
# pag.PAUSE = 1.5
# # 在屏幕左上（500，500）像素位置点击
# pag.click(500, 500)

"""
1. 获取坐标系
"""
import os

try:
    while True:
        os.system('cls')
        x, y = pag.position()
        print("当前鼠标的X轴的位置为：{}，Y轴的位置为：{}".format(x, y))
        x, y = pag.size()
        print("当前屏幕的分辨率是{}*{}".format(x, y))

except Exception as e:
    print(e)

"""
2. 点击
    其中x，y是坐标，clicks 是点击次数，interval 是点击间隔，button 指代三个鼠标按钮的哪一个，duiation 是点击之间的间隔。
"""
# pag.click(x=None, y=None, clicks=1, interval=0.0, button='left', duration=0.0)

"""
3. 输入
    输入 ASCII 字符和键盘击键、热键分别如下：
    输入 ASCII 字符串是typewrite(message='test message.',interval=0.5)
    击键是press('esc')
    按下是KeyDown('ctrl')
    松开是KeyUp('ctrl')
    组合键是hotkey('ctrl','v')。
    至于汉字，稍微复杂点。
"""

"""
4. 汉字输入
    涉及汉字，无法用 ASCII 方案解决，需要导入包 pyperclip ，这个包封装了系统剪贴板
"""
# import pyperclip
#
# # 以下读入内容，就是把内容存入剪贴板。
# pyperclip.copy('需要输入的汉字')
# # 以下输出内容，就是粘贴。
# pag.hotkey('command', 'v')

"""
5. 集成
    根据 to 列表内容，把操作分解为点击和粘贴，实现了自动化操作的目的。大部分编码都很好理解，能跟鼠标操作一一对应起来。可能存在难度的是数据源的问题
"""
import pyautogui as pag
import pyperclip

pag.PAUSE = 1.5
pag.FAILSAFE = True

to = ['测试任务1', '测试任务2', '测试任务3', '测试任务4', '测试任务5', \
      '测试任务6', '测试任务7', '测试任务8', '测试任务9', '测试任务10']

for t in to:
    pag.click(63, 191)
    pyperclip.copy(t)
    pag.hotkey('command', 'v')
    pag.click(328, 191)
    pag.click(384, 461)
    pag.click(374, 191)

"""
6. 数据源
    相较于复杂的现实数据源，最好的方式就是把数据转成 csv 文件。这样许多 Excel 都可以另存成这个文件，其本身又是基于文本的，可读可写，比较方便。其他诸如 SQL 数据库、 XML 数据也可以导出转换为 csv 文件。
假设现在有了 csv 格式数据源 data.csv ,需要这样操作。
    以下代码比较简单，把 csv 中存成的数据存储到 to 这个数组里，每行数据都是一个元组，调用的时候，如4.6部分代码所示，使用 for 循环加上元组下标即可。
"""
# to = []
#
# with open('data.csv')as f:
#     lines = f.readlines()
#
# for line in lines:
#     to.append(tuple(line.split(',')))
