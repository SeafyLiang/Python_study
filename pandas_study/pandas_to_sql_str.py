#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   pandas_to_sql_str.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/9/13 10:46   SeafyLiang   1.0          df转sql语句字符串
"""
import pandas as pd
import numpy as np

# 生成一个df
dates = pd.date_range('20210913', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

# 定义df输入源，以及目标表名
SOURCE = df
TARGET = 'table_name'


# 定义生成CREATE语句方法
def SQL_CREATE_STATEMENT_FROM_DATAFRAME(SOURCE, TARGET):
    # SQL_CREATE_STATEMENT_FROM_DATAFRAME(SOURCE, TARGET)
    # SOURCE: source dataframe
    # TARGET: target table to be created in database

    import pandas as pd
    sql_text = pd.io.sql.get_schema(SOURCE.reset_index(), TARGET)
    return sql_text


# 定义生成INSERT语句方法
def SQL_INSERT_STATEMENT_FROM_DATAFRAME(SOURCE, TARGET):
    sql_texts = []
    for index, row in SOURCE.iterrows():
        sql_texts.append(
            'INSERT INTO ' + TARGET + ' (' + str(', '.join(SOURCE.columns)) + ') VALUES ' + str(tuple(row.values)))
    return sql_texts


print(SQL_INSERT_STATEMENT_FROM_DATAFRAME(df, TARGET))
print(SQL_CREATE_STATEMENT_FROM_DATAFRAME(df, TARGET))

# 调用sql字符串批量插入数据
for sql in SQL_CREATE_STATEMENT_FROM_DATAFRAME(df, TARGET):
    execute_sql(sql)
