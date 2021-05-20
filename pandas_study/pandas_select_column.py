#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   pandas_select_column.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/5/20 14:52   SeafyLiang   1.0     pandas按数据类型选择列
"""
import pandas as pd
"""
pandas 的 df 提供了 select_dtypes 函数，可以按数据类型选择 df 的列。该函数包含 include 与 exclude 参数：

include 表示包含哪种类型，输出结果是包含该类型的 df；
exclude 表示排除哪种类型，输出结果是不包含该类型的 df；
包含或排除的类型可以是多种，用列表显示，如 include=['float64','int64']；
"""

"""
数据类型说明

选择所有数字类型的列，用 np.number 或 'number'
选择字符串类型的列，必须用 object，注意，这将返回所有数据类型为 object 的列
选择日期时间类型的列，用np.datetime64、'datetime' 或 'datetime64'
选择 timedelta 类型的列，用np.timedelta64、'timedelta' 或 'timedelta64'
选择 category 类型类别，用 'category'
选择 datetimetz 类型的列，用'datetimetz'或 'datetime64[ns, tz]'
"""
df = pd.DataFrame({'a': [1, 2] * 3,
                   'b': [True, False] * 3,
                   'c': [1.0, 2.0] * 3})
print('df:', df)

# 输出包含 bool 数据类型的列
print('输出包含 bool 数据类型的列:', df.select_dtypes(include='bool'))

# 输出包含小数数据类型的列
print('输出包含小数数据类型的列:', df.select_dtypes(include=['float64']))

# 输出排除整数的列
print('输出包含小数数据类型的列:', df.select_dtypes(exclude=['int64']))

