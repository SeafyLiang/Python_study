#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   EDA_report.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/6/18 16:06   SeafyLiang   1.0          3种生成eda报告方式
"""
import seaborn as sns

mpg = sns.load_dataset('mpg')
mpg.head()

"""
参考自：https://mp.weixin.qq.com/s/CIZjJg1sEsbkToYjSlRaUQ

<结论>
Pandas Profiling、Sweetviz和PandasGUI都很不错，旨在简化我们的EDA处理。在不同的工作流程中，每个都有自己的优势和适用性，三个工具具体优势如下：
    * Pandas Profiling 适用于快速生成单个变量的分析。
    * Sweetviz 适用于数据集之间和目标变量之间的分析。
    * PandasGUI适用于具有手动拖放功能的深度分析。
"""

'''
1. pandas_profiling
这个属于三个中最轻便、简单的了。它可以快速生成报告，一览变量概况。总共提供了六个部分：概述、变量、交互、相关性，缺失值和样本。
参考资料:https://zhuanlan.zhihu.com/p/85967505
'''
from pandas_profiling import ProfileReport

profile = ProfileReport(mpg, title='MPG Pandas Profiling Report', explorative=True)
profile.to_file('pandas_profiling_report.html')


'''
2. Sweetviz
Sweetviz是另一个Python的开源代码包，仅用一行代码即可生成漂亮的EDA报告。与Pandas Profiling的区别在于它输出的是一个完全独立的HTML应用程序。
Sweetviz的一些优势在于：
    分析有关目标值的数据集的能力
    两个数据集之间的比较能力

但也有一些缺点：
    变量之间没有可视化，例如散点图
    报告在另一个标签中打开

个人是比较喜欢Sweetviz的。
'''
import sweetviz as sv

# 可以选择目标特征
my_report = sv.analyze(mpg, target_feat='mpg')
my_report.show_html()
# Sweetviz的优势不在于单个数据集上的EDA报告，而在于数据集的比较。
# 可以通过两种方式比较数据集：将其拆分（例如训练和测试数据集），或者使用一些过滤器对总体进行细分。
# 设置需要分析的变量
my_report = sv.compare_intra(mpg, mpg["origin"] == "usa", ["USA", "NOT-USA"], target_feat='mpg')
my_report.show_html()

'''
3. pandasgui
mac使用有报错
PandasGUI与前面的两个不同，PandasGUI不会生成报告，而是生成一个GUI（图形用户界面）的数据框，我们可以使用它来更详细地分析我们的Dataframe。
pandasGUI的一些优势在于：
    可以拖拽
    快速过滤数据
    快速绘图

缺点在于：
    没有完整的统计信息
    不能生成报告
'''
from pandasgui import show
# 部署GUI的数据集
gui = show(mpg)