#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   pandas_datetime2.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/5/20 10:52   SeafyLiang   1.0       Pandas时间序列-15个常用操作
"""
import pandas as pd
import numpy as np
from datetime import datetime

'''
参考资料：
https://mp.weixin.qq.com/s?__biz=Mzk0NzI3ODMyMA==&mid=2247489105&idx=1&sn=674ea85b9cc7bcfa516e66478c92ae55&chksm=c3780ecef40f87d83c430e380062652ae3fa376164133e8f664cd424a934cb8796956a9d166e&scene=21#wechat_redirect
https://mp.weixin.qq.com/s/ZFOqojafwTiwYWKExENqnw
'''
# 1.创建一个时间戳
pd.to_datetime('2021-05-20')  # output: Timestamp('2021-05-20 00:00:00')
pd.Timestamp('2021-05-20')  # output: Timestamp('2021-05-20 00:00:00')

# 2.访问时间信息
# 查看一下这个时间戳所代表的年、月、日等信息
a = pd.Timestamp('2021-10-01')
a.day_name()  # Friday，看来今年的10月1日是周五哈？
a.month_name()  # October 十月份
print(a.day, a.month, a.year)  # 1, 10, 2021，查看年月日等信息

# 3.数据格式转化为时间序列
df = pd.DataFrame({"time_frame": ["2021-01-01", "2021-01-02", "2021-01-03", "2021-01-04", "2021-01-05"]})
df['time_frame'] = pd.to_datetime(df['time_frame'])
print(df.info())
# #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   time_frame  5 non-null      datetime64[ns]

# 4.字符串转化成时间格式
date_string = [str(x) for x in df['time_frame'].tolist()]
print(date_string)
# ['2021-01-01 00:00:00', '2021-01-02 00:00:00', '2021-01-03 00:00:00', '2021-01-04 00:00:00', '2021-01-05 00:00:00']
# 从字符串转换回去时间序列的数据
time_string = ['2021-02-14 00:00:00', '2021-02-14 01:00:00', '2021-02-14 02:00:00', '2021-02-14 03:00:00',
               '2021-02-14 04:00:00', '2021-02-14 05:00:00', '2021-02-14 06:00:00']
pd.to_datetime(time_string, infer_datetime_format=True)
print(time_string)
# ['2021-02-14 00:00:00', '2021-02-14 01:00:00', '2021-02-14 02:00:00', '2021-02-14 03:00:00', '2021-02-14 04:00:00', '2021-02-14 05:00:00', '2021-02-14 06:00:00']
# 另外一种方式
import datetime

text_1 = "2021-02-14"
datetime.datetime.strptime(text_1, '%Y-%m-%d')
print(text_1)
# 2021-02-14

# 5.提取时间格式背后的信息
# 在时间序列的数据处理过程当中，我们可能需要经常来实现下面的需求
#   求某个日期对应的星期数（2021-06-22是第几周）
#   判断一个日期是周几（2021-02-14是周几）
#   判断某一日期是第几季度，等等
# 当数据集中的某一列已经转化为是“datetime64”的格式时，仅需要用到“dt”的方法，就可以快速得到相应的结果，例如
df = pd.DataFrame({"time_frame": ["2021-01-01", "2021-01-02", "2021-01-03", "2021-01-04", "2021-01-05", "2021-01-06",
                                  "2021-01-07", "2021-01-08"]})
df["time_frame"] = pd.to_datetime(df["time_frame"])
# 一周中的第几天
print(df.time_frame.dt.dayofweek[0])
# 4
# 返回对应额日期
print(df.time_frame.dt.date[0])
# 2021-01-01
# 返回一周中的第几天，0对应周一，1对应周二
print(df.time_frame.dt.weekday[0])
# 4
'''
常用参数：
dayofyear   一年中的第几天
weekofyear  一年中的第几周
weekday     一周中的第几天，0对应周一
quarter     处于第几个季度
is_leap_yaer    判断是否处于闰年
'''

# 6.创建时间索引
# 6.1 关于date_range函数
# 可用于创建时间索引，并且时间频率可以灵活调整，参数“freq”就是用来调整时间频率的，“M”代表月份，“D”就代表的是天数了
print(pd.date_range(start='2021-02-14', periods=10, freq='M'))
# DatetimeIndex(['2021-02-28', '2021-03-31', '2021-04-30', '2021-05-31',
#                '2021-06-30', '2021-07-31', '2021-08-31', '2021-09-30',
#                '2021-10-31', '2021-11-30'],
#               dtype='datetime64[ns]', freq='M')
# 6.2 period_range和timedelta_range函数
print(pd.period_range('2021', periods=10, freq='M'))
# PeriodIndex(['2021-01', '2021-02', '2021-03', '2021-04', '2021-05', '2021-06',
#              '2021-07', '2021-08', '2021-09', '2021-10'],
#             dtype='period[M]')
print(pd.timedelta_range(start='0', periods=24, freq='H'))
# TimedeltaIndex(['0 days 00:00:00', '0 days 01:00:00', '0 days 02:00:00',
#                 '0 days 03:00:00', '0 days 04:00:00', '0 days 05:00:00',
#                 '0 days 06:00:00', '0 days 07:00:00', '0 days 08:00:00',
#                 '0 days 09:00:00', '0 days 10:00:00', '0 days 11:00:00',
#                 '0 days 12:00:00', '0 days 13:00:00', '0 days 14:00:00',
#                 '0 days 15:00:00', '0 days 16:00:00', '0 days 17:00:00',
#                 '0 days 18:00:00', '0 days 19:00:00', '0 days 20:00:00',
#                 '0 days 21:00:00', '0 days 22:00:00', '0 days 23:00:00'],
#                dtype='timedelta64[ns]', freq='H')

# 7.重采样resample
# 我们也可以对时间序列的数据集进行重采样，重采样就是将时间序列从一个频率转换到另一个频率的处理过程，主要分为降采样和升采样，将高频率、间隔短的数据聚合到低频率、间隔长的过程称为是降采样，反之则是升采样.
#
# 我们先来创建一个包含30个值和一个时间序列索引的数据集
A = pd.date_range('2021-01-01', periods=30, freq='D')
values = np.random.randint(10, size=30)
S = pd.Series(values, index=A)
# 返回5天时间内的数据加总
print(S.resample('5D').sum())
# 2021-01-01    26
# 2021-01-06    16
# 2021-01-11    17
# 2021-01-16    25
# 2021-01-21    24
# 2021-01-26    28
# Freq: 5D, dtype: int64

# 8.关于滑动窗口“rolling”和“expanding”
# 因此便就有了滑动窗口这一个概念，简而言之就是将某个时点的数据衍生到包含这个时点的一段时间内做一个数据统计。首先我们先来创建需要用到的数据集
index = pd.date_range('2021-01-01', periods=30)
data = pd.DataFrame(np.arange(len(index)), index=index, columns=['test'])
# 主要有“rolling”方法和“expanding”方法，“rolling”方法考虑的是一定的时间段内的数据，而“expanding”考虑的则是之前所有的数据，例如
# 移动3个值，进行求和
data['sum'] = data.test.rolling(3).sum()
print(data.head())
#             test  sum
# 2021-01-01     0  NaN
# 2021-01-02     1  NaN
# 2021-01-03     2  3.0
# 2021-01-04     3  6.0
# 2021-01-05     4  9.0
# 移动3个值，进行求平均数
data['mean'] = data.test.rolling(3).mean()
print(data.head())
#             test  sum  mean
# 2021-01-01     0  NaN   NaN
# 2021-01-02     1  NaN   NaN
# 2021-01-03     2  3.0   1.0
# 2021-01-04     3  6.0   2.0
# 2021-01-05     4  9.0   3.0
# 我们发现数据集中有一些缺失值，我们这里就可以使用“pandas”中特有的方法来进行填充，例如
data['mean'].fillna(method='backfill', inplace=True)
print(data.head())
#             test  sum  mean
# 2021-01-01     0  NaN   1.0
# 2021-01-02     1  NaN   1.0
# 2021-01-03     2  3.0   1.0
# 2021-01-04     3  6.0   2.0
# 2021-01-05     4  9.0   3.0

# 9.查找特定日期的某一天的名称
day = pd.Timestamp('2021/1/5')
print(day.day_name())
# Tuesday

# 10.执行算数计算
day = pd.Timestamp('2021/1/5')
day1 = day + pd.Timedelta("3 day")
# "Timedelta"功能允许输入任何天单位（天、小时、分钟、秒）的时差。
print(day1.day_name())
# Friday

day2 = day1 + pd.offsets.BDay()
print(day2.day_name())
# 使用"offsets.BDay()"函数来显示下一个工作日。换句话说，这意味着在星期五之后，下一个工作日是星期一。
# Monday

# 11.使用时区信息来操作转换日期时间
# 获取时区信息
dat_ran = pd.date_range(start='1/1/2021', end='1/5/2021', freq='Min')
dat_ran = dat_ran.tz_localize("UTC")
print(dat_ran)
# DatetimeIndex(['2021-01-01 00:00:00+00:00', '2021-01-01 00:01:00+00:00',
#                '2021-01-01 00:02:00+00:00', '2021-01-01 00:03:00+00:00',
#                '2021-01-01 00:04:00+00:00', '2021-01-01 00:05:00+00:00',
#                '2021-01-01 00:06:00+00:00', '2021-01-01 00:07:00+00:00',
#                '2021-01-01 00:08:00+00:00', '2021-01-01 00:09:00+00:00',
#                ...
#                '2021-01-04 23:51:00+00:00', '2021-01-04 23:52:00+00:00',
#                '2021-01-04 23:53:00+00:00', '2021-01-04 23:54:00+00:00',
#                '2021-01-04 23:55:00+00:00', '2021-01-04 23:56:00+00:00',
#                '2021-01-04 23:57:00+00:00', '2021-01-04 23:58:00+00:00',
#                '2021-01-04 23:59:00+00:00', '2021-01-05 00:00:00+00:00'],
#               dtype='datetime64[ns, UTC]', length=5761, freq='T')
# 转换为美国时区
dat_ran = dat_ran.tz_convert("US/Pacific")
print(dat_ran)
# DatetimeIndex(['2020-12-31 16:00:00-08:00', '2020-12-31 16:01:00-08:00',
#                '2020-12-31 16:02:00-08:00', '2020-12-31 16:03:00-08:00',
#                '2020-12-31 16:04:00-08:00', '2020-12-31 16:05:00-08:00',
#                '2020-12-31 16:06:00-08:00', '2020-12-31 16:07:00-08:00',
#                '2020-12-31 16:08:00-08:00', '2020-12-31 16:09:00-08:00',
#                ...
#                '2021-01-04 15:51:00-08:00', '2021-01-04 15:52:00-08:00',
#                '2021-01-04 15:53:00-08:00', '2021-01-04 15:54:00-08:00',
#                '2021-01-04 15:55:00-08:00', '2021-01-04 15:56:00-08:00',
#                '2021-01-04 15:57:00-08:00', '2021-01-04 15:58:00-08:00',
#                '2021-01-04 15:59:00-08:00', '2021-01-04 16:00:00-08:00'],
#               dtype='datetime64[ns, US/Pacific]', length=5761, freq='T')

# 12.使用日期时间戳
dat_ran = pd.date_range(start='1/1/2021', end='1/5/2021', freq='Min')
print(type(dat_ran[110]))
# <class 'pandas._libs.tslibs.timestamps.Timestamp'>

# 13.创建日期系列
dat_ran = pd.date_range(start='1/1/2021', end='1/5/2021', freq='Min')
print(dat_ran)
# DatetimeIndex(['2021-01-01 00:00:00', '2021-01-01 00:01:00',
#                '2021-01-01 00:02:00', '2021-01-01 00:03:00',
#                '2021-01-01 00:04:00', '2021-01-01 00:05:00',
#                '2021-01-01 00:06:00', '2021-01-01 00:07:00',
#                '2021-01-01 00:08:00', '2021-01-01 00:09:00',
#                ...
#                '2021-01-04 23:51:00', '2021-01-04 23:52:00',
#                '2021-01-04 23:53:00', '2021-01-04 23:54:00',
#                '2021-01-04 23:55:00', '2021-01-04 23:56:00',
#                '2021-01-04 23:57:00', '2021-01-04 23:58:00',
#                '2021-01-04 23:59:00', '2021-01-05 00:00:00'],
#               dtype='datetime64[ns]', length=5761, freq='T')

# 14.操作日期序列
dat_ran = pd.date_range(start='1/1/2019', end='1/08/2019', freq='Min')
df = pd.DataFrame(dat_ran, columns=['date'])
df['data'] = np.random.randint(0, 100, size=(len(dat_ran)))
print(df.head(5))
#                  date  data
# 0 2019-01-01 00:00:00    94
# 1 2019-01-01 00:01:00    99
# 2 2019-01-01 00:02:00    50
# 3 2019-01-01 00:03:00    22
# 4 2019-01-01 00:04:00    50
# 使用"DataFrame"函数将字符串类型转换为dataframe。最后"np.random.randint()"函数是随机生成一些假定的数据。

# 15.使用时间戳数据对数据进行切片
df = pd.DataFrame(dat_ran, columns=['date'])
df['data'] = np.random.randint(0, 100, size=(len(dat_ran)))
string_data = [str(x) for x in dat_ran]

print(string_data[1:5])
# ['2019-01-01 00:01:00', '2019-01-01 00:02:00', '2019-01-01 00:03:00', '2019-01-01 00:04:00']
# 在创建dataframe并将其映射到随机数后，对列表进行切片。
