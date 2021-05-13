#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   pandas_sort.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/5/12 16:28   SeafyLiang   1.0       pandas_排序
"""
import pandas as pd

sales = pd.read_excel("sort_data.xlsx", index_col="序号")
print("原始数据：", sales)

reorder = [4, 8, 9, 1, 5, 7, 2, 6, 3]
print("1.自定义索引排序：", sales.reindex(reorder))

sales['分公司'] = pd.Categorical(sales['分公司'], categories=[
    '北京', '上海', '广州', '深圳'], ordered=True)
print("2.自定义列值排序：", sales.sort_values(by='分公司'))

# branch = sales[['分公司代码']]
# department = sales[['门店代码']]
#
# sales = pd.merge(sales, branch, on="分公司代码", how="left")
# sales = pd.merge(sales, department, on="门店代码", how="left")

print("3. 利用辅助列实现自定义列值排序：", sales.sort_values(by=['分公司代码', '门店代码'], inplace=True))

sales.sort_index(axis='columns', ascending=True)
sales = sales[['分公司代码', '分公司', '门店代码', '门店', '销售额']]
# 删掉没用的列
del sales['分公司代码'], sales['门店代码']
# 重置索引
sales.reset_index(drop=True, inplace=True)
print("4. 自定义列序：", sales)
