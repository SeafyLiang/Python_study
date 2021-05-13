#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   pandasVSpolars.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/5/13 13:26   SeafyLiang   1.0       pandas对比polars
"""
import timeit
import pandas as pd
import polars as pl
"""
GitHub地址：
https://github.com/ritchie46/polars

使用文档：
https://ritchie46.github.io/polars-book/

Polars是通过Rust编写的一个库，Polars的内存模型是基于Apache Arrow。

Polars存在两种API，一种是Eager API，另一种则是Lazy API。

其中Eager API和Pandas的使用类似，语法差不太多，立即执行就能产生结果。

Lazy API就像Spark，首先将查询转换为逻辑计划，然后对计划进行重组优化，以减少执行时间和内存使用。

测试效果：
测试数据 [1383144 rows x 22 columns]
1. 数据排序（pandas）Time:  2.731423987
1. 数据排序（polars）Time:  0.48892446399999967
2. 数据整合（pandas）Time:  4.990813701999999
2. 数据整合（polars）Time:  0.7012950379999996
"""
# [1383144 rows x 22 columns]
filepath = 'df512.csv'

"""
1.比较两个库的排序算法用时
"""

start = timeit.default_timer()

df = pd.read_csv(filepath)
df.sort_values('coll_time', ascending=False)
stop = timeit.default_timer()

print('1. 数据排序（pandas）Time: ', stop - start)

# -------------------------
# Time:  2.484395734

start = timeit.default_timer()

df = pl.read_csv(filepath)
df.sort(by='coll_time', reverse=True)
stop = timeit.default_timer()

print('1. 数据排序（polars）Time: ', stop - start)

# -----------------------
# Time:  0.4715386539999997


"""
2. 比较数据整合的效果
"""
start = timeit.default_timer()

df_users = pd.read_csv(filepath)
df_fake = pd.read_csv(filepath)
df_users.append(df_fake, ignore_index=True)
stop = timeit.default_timer()

print('2. 数据整合（pandas）Time: ', stop - start)

# ------------------------
# Time:  5.0686382

start = timeit.default_timer()

df_users = pl.read_csv(filepath)
df_fake = pl.read_csv(filepath)
df_users.vstack(df_fake)
stop = timeit.default_timer()

print('2. 数据整合（polars）Time: ', stop - start)

# -----------------------
# Time:  1.0282350420000004
