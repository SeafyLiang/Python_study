#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   pandas_datetime.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/4/28 15:33   SeafyLiang   1.0     Pandas DateTime 超强总结
"""
'''
参考资料：https://mp.weixin.qq.com/s/VVxm5TqHLagePGUzMdiXgw
在 Pandas 中处理日期和时间的多个方面，具体包含如下内容：
- Timestamp 和 Period 对象的功能
- 如何使用时间序列 DataFrames
- 如何对时间序列进行切片
- DateTimeIndex 对象及其方法
- 如何重新采样时间序列数据
'''
import pandas as pd
import numpy as np


# 1、探索 Pandas 时间戳和周期对象
def method1():
    print(pd.Timestamp(year=1982, month=9, day=4, hour=1, minute=35, second=10))
    print(pd.Timestamp('1982-09-04 1:35.18'))
    print(pd.Timestamp('Sep 04, 1982 1:35.18'))
    # 1982-09-04 01:35:10
    # 1982-09-04 01:35:10
    # 1982-09-04 01:35:10

    print(pd.Timestamp(5000))
    # 1970-01-01 00:00:00.000005

    time_stamp = pd.Timestamp('2022-02-09')
    print('{}, {} {}, {}'.format(time_stamp.day_name(), time_stamp.month_name(), time_stamp.day, time_stamp.year))
    # Wednesday, February 9, 2022

    year = pd.Period('2021')
    print(year)
    # 2021

    print('Start Time:', year.start_time)
    print('End Time:', year.end_time)
    # Start Time: 2021-01-01 00:00:00
    # End Time: 2021-12-31 23:59:59.999999999

    month = pd.Period('2022-01')
    print(month)
    print('Start Time:', month.start_time)
    print('End Time:', month.end_time)
    # 2022-01
    # Start Time: 2022-01-01 00:00:00
    # End Time: 2022-01-31 23:59:59.999999999

    day = pd.Period('2022-01', freq='D')
    print(day)
    print('Start Time:', day.start_time)
    print('End Time:', day.end_time)
    # 2022-01-01
    # Start Time: 2022-01-01 00:00:00
    # End Time: 2022-01-01 23:59:59.999999999

    hour = pd.Period('2022-02-09 16:00:00', freq='H')
    print(hour)
    print(hour + 2)
    print(hour - 2)
    # 2022-02-09 16:00
    # 2022-02-09 18:00
    # 2022-02-09 14:00

    print(hour + pd.offsets.Hour(+2))
    print(hour + pd.offsets.Hour(-2))
    # 2022-02-09 18:00
    # 2022-02-09 14:00

    week = pd.date_range('2022-2-7', periods=7)
    for day in week:
        print('{}-{}\t{}'.format(day.day_of_week, day.day_name(), day.date()))
    # 0-Monday	2022-02-07
    # 1-Tuesday	2022-02-08
    # 2-Wednesday	2022-02-09
    # 3-Thursday	2022-02-10
    # 4-Friday	2022-02-11
    # 5-Saturday	2022-02-12
    # 6-Sunday	2022-02-13


# 2、创建时间序列数据框
def method2():
    # 文件下载地址：https://raw.githubusercontent.com/m-mehdi/pandas_tutorials/main/server_util.csv
    df = pd.read_csv('data/server_util.csv')
    print(df.head())
    #               datetime  server_id  cpu_utilization  free_memory  session_count
    # 0  2019-03-06 00:00:00        100             0.40         0.54             52
    # 1  2019-03-06 01:00:00        100             0.49         0.51             58
    # 2  2019-03-06 02:00:00        100             0.49         0.54             53
    # 3  2019-03-06 03:00:00        100             0.44         0.56             49
    # 4  2019-03-06 04:00:00        100             0.42         0.52             54

    print(df.info())
    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 40800 entries, 0 to 40799
    # Data columns (total 5 columns):
    #  #   Column           Non-Null Count  Dtype
    # ---  ------           --------------  -----
    #  0   datetime         40800 non-null  object
    #  1   server_id        40800 non-null  int64
    #  2   cpu_utilization  40800 non-null  float64
    #  3   free_memory      40800 non-null  float64
    #  4   session_count    40800 non-null  int64
    # dtypes: float64(2), int64(2), object(1)
    # memory usage: 1.6+ MB
    # None

    df['datetime'] = pd.to_datetime(df['datetime'])
    print(df.info())
    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 40800 entries, 0 to 40799
    # Data columns (total 5 columns):
    #  #   Column           Non-Null Count  Dtype
    # ---  ------           --------------  -----
    #  0   datetime         40800 non-null  datetime64[ns]
    #  1   server_id        40800 non-null  int64
    #  2   cpu_utilization  40800 non-null  float64
    #  3   free_memory      40800 non-null  float64
    #  4   session_count    40800 non-null  int64
    # dtypes: datetime64[ns](1), float64(2), int64(2)
    # memory usage: 1.6 MB
    # None

    df = pd.read_csv('data/server_util.csv', parse_dates=['datetime'])
    print(df.info())
    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 40800 entries, 0 to 40799
    # Data columns (total 5 columns):
    #  #   Column           Non-Null Count  Dtype
    # ---  ------           --------------  -----
    #  0   datetime         40800 non-null  datetime64[ns]
    #  1   server_id        40800 non-null  int64
    #  2   cpu_utilization  40800 non-null  float64
    #  3   free_memory      40800 non-null  float64
    #  4   session_count    40800 non-null  int64
    # dtypes: datetime64[ns](1), float64(2), int64(2)
    # memory usage: 1.6 MB
    # None

    print(df.datetime.min())
    print(df.datetime.max())
    # 2019-03-06 00:00:00
    # 2019-04-08 23:00:00

    mask = (df.datetime >= pd.Timestamp('2019-03-06')) & (df.datetime < pd.Timestamp('2019-03-07'))
    print(df.loc[mask])
    #                  datetime  server_id  ...  free_memory  session_count
    # 0     2019-03-06 00:00:00        100  ...         0.54             52
    # 1     2019-03-06 01:00:00        100  ...         0.51             58
    # 2     2019-03-06 02:00:00        100  ...         0.54             53
    # 3     2019-03-06 03:00:00        100  ...         0.56             49
    # 4     2019-03-06 04:00:00        100  ...         0.52             54
    # ...                   ...        ...  ...          ...            ...
    # 40003 2019-03-06 19:00:00        149  ...         0.24             81
    # 40004 2019-03-06 20:00:00        149  ...         0.23             81
    # 40005 2019-03-06 21:00:00        149  ...         0.29             83
    # 40006 2019-03-06 22:00:00        149  ...         0.29             82
    # 40007 2019-03-06 23:00:00        149  ...         0.24             84
    #
    # [1200 rows x 5 columns]


# 3、切片时间序列
def method3():
    df = pd.read_csv('data/server_util.csv', parse_dates=['datetime'])
    df.set_index('datetime', inplace=True)
    print(df)
    #                      server_id  cpu_utilization  free_memory  session_count
    # datetime
    # 2019-03-06 00:00:00        100             0.40         0.54             52
    # 2019-03-06 01:00:00        100             0.49         0.51             58
    # 2019-03-06 02:00:00        100             0.49         0.54             53
    # 2019-03-06 03:00:00        100             0.44         0.56             49
    # 2019-03-06 04:00:00        100             0.42         0.52             54
    # ...                        ...              ...          ...            ...
    # 2019-04-08 19:00:00        149             0.73         0.20             81
    # 2019-04-08 20:00:00        149             0.75         0.25             83
    # 2019-04-08 21:00:00        149             0.80         0.26             82
    # 2019-04-08 22:00:00        149             0.75         0.29             82
    # 2019-04-08 23:00:00        149             0.75         0.24             80
    #
    # [40800 rows x 4 columns]

    print(df.loc['2019-03-07 02:00:00'].head(5))
    #                      server_id  cpu_utilization  free_memory  session_count
    # datetime
    # 2019-03-07 02:00:00        100             0.44         0.50             56
    # 2019-03-07 02:00:00        101             0.78         0.21             87
    # 2019-03-07 02:00:00        102             0.75         0.27             80
    # 2019-03-07 02:00:00        103             0.76         0.28             85
    # 2019-03-07 02:00:00        104             0.74         0.24             77

    print(df.loc['2019-03-07'].head(5))
    #                      server_id  cpu_utilization  free_memory  session_count
    # datetime
    # 2019-03-07 00:00:00        100             0.51         0.52             55
    # 2019-03-07 01:00:00        100             0.46         0.50             49
    # 2019-03-07 02:00:00        100             0.44         0.50             56
    # 2019-03-07 03:00:00        100             0.45         0.52             51
    # 2019-03-07 04:00:00        100             0.42         0.50             53

    print("df.loc['Apr 2019'].head(2):\n", df.loc['Apr 2019'].head(2))
    print("df.loc['8th April 2019'].head(2):\n", df.loc['8th April 2019'].head(2))
    print("df.loc['April 05, 2019 5pm'].head(2):\n", df.loc['April 05, 2019 5pm'].head(2))
    # df.loc['Apr 2019'].head(2):
    #                       server_id  cpu_utilization  free_memory  session_count
    # datetime
    # 2019-04-01 00:00:00        100             0.49         0.55             52
    # 2019-04-01 01:00:00        100             0.44         0.53             52
    # df.loc['8th April 2019'].head(2):
    #                       server_id  cpu_utilization  free_memory  session_count
    # datetime
    # 2019-04-08 00:00:00        100             0.43         0.54             51
    # 2019-04-08 01:00:00        100             0.49         0.49             51
    # df.loc['April 05, 2019 5pm'].head(2):
    #                       server_id  cpu_utilization  free_memory  session_count
    # datetime
    # 2019-04-05 17:00:00        100             0.53         0.51             48
    # 2019-04-05 17:00:00        101             0.82         0.20             88

    print(df.loc['03-04-2019':'04-04-2019'].head(2))
    # datetime
    # 2019-03-06 00:00:00        100             0.40         0.54             52
    # 2019-03-06 01:00:00        100             0.49         0.51             58
    # pandas_datetime.py:223: FutureWarning: Value based partial slicing on non-monotonic DatetimeIndexes with non-existing keys is deprecated and will raise a KeyError in a future Version.
    #   print(df.loc['03-04-2019':'04-04-2019'].head(2))
    print(df.sort_index().loc['03-04-2019':'04-04-2019'].head(2))
    #             server_id  cpu_utilization  free_memory  session_count
    # datetime
    # 2019-03-06        100              0.4         0.54             52
    # 2019-03-06        135              0.5         0.55             55


# 4、DateTimeIndex 方法
def method4():
    df = pd.read_csv('data/server_util.csv', parse_dates=['datetime'])
    df.set_index('datetime', inplace=True)
    print(type(df.index))
    # <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

    print(df.at_time('09:00').head(5))
    #                      server_id  cpu_utilization  free_memory  session_count
    # datetime
    # 2019-03-06 09:00:00        100             0.48         0.51             51
    # 2019-03-07 09:00:00        100             0.45         0.49             56
    # 2019-03-08 09:00:00        100             0.45         0.53             53
    # 2019-03-09 09:00:00        100             0.45         0.51             53
    # 2019-03-10 09:00:00        100             0.49         0.55             55

    print(df.between_time('00:00', '02:00').head(5))
    # datetime
    # 2019-03-06 00:00:00        100             0.40         0.54             52
    # 2019-03-06 01:00:00        100             0.49         0.51             58
    # 2019-03-06 02:00:00        100             0.49         0.54             53
    # 2019-03-07 00:00:00        100             0.51         0.52             55
    # 2019-03-07 01:00:00        100             0.46         0.50             49

    print(df.sort_index().first('5B'))
    #             server_id  cpu_utilization  free_memory  session_count
    # datetime
    # 2019-03-06        100             0.40         0.54             52
    # 2019-03-06        135             0.50         0.55             55
    # 2019-03-06        110             0.54         0.40             61
    # 2019-03-06        136             0.58         0.40             64
    # 2019-03-06        109             0.57         0.41             61
    # ...               ...              ...          ...            ...
    # 2019-03-12        134             0.53         0.45             61
    # 2019-03-12        144             0.68         0.31             73
    # 2019-03-12        113             0.76         0.24             83
    # 2019-03-12        114             0.58         0.48             67
    # 2019-03-12        131             0.58         0.42             67
    #
    # [7250 rows x 4 columns]
    print(df.sort_index().last('1W'))
    #                      server_id  cpu_utilization  free_memory  session_count
    # datetime
    # 2019-04-08 00:00:00        106             0.44         0.62             49
    # 2019-04-08 00:00:00        112             0.72         0.29             81
    # 2019-04-08 00:00:00        100             0.43         0.54             51
    # 2019-04-08 00:00:00        137             0.75         0.28             83
    # 2019-04-08 00:00:00        110             0.61         0.40             62
    # ...                        ...              ...          ...            ...
    # 2019-04-08 23:00:00        128             0.64         0.41             64
    # 2019-04-08 23:00:00        127             0.67         0.33             78
    # 2019-04-08 23:00:00        126             0.71         0.33             73
    # 2019-04-08 23:00:00        123             0.71         0.22             83
    # 2019-04-08 23:00:00        149             0.75         0.24             80
    #
    # [1200 rows x 4 columns]


# 5、重新采样时间序列数据
def method5():
    df = pd.read_csv('data/server_util.csv', parse_dates=['datetime'])
    df.set_index('datetime', inplace=True)
    print(df[df.server_id == 100].resample('D')['cpu_utilization', 'free_memory', 'session_count'].mean())
    #             cpu_utilization  free_memory  session_count
    # datetime
    # 2019-03-06         0.470417     0.535417      53.000000
    # 2019-03-07         0.455417     0.525417      53.666667
    # 2019-03-08         0.478333     0.532917      54.541667
    # 2019-03-09         0.472917     0.523333      54.166667
    # 2019-03-10         0.465000     0.527500      54.041667
    # 2019-03-11         0.469583     0.528750      53.916667
    # 2019-03-12         0.475000     0.533333      53.750000
    # 2019-03-13         0.462917     0.521667      52.541667
    # 2019-03-14         0.472083     0.532500      54.875000
    # 2019-03-15         0.470417     0.530417      53.500000
    # 2019-03-16         0.463750     0.530833      54.416667
    # 2019-03-17         0.472917     0.532917      52.041667
    # 2019-03-18         0.475417     0.535000      53.333333
    # 2019-03-19         0.460833     0.546667      54.791667
    # 2019-03-20         0.467083     0.529167      54.375000
    # 2019-03-21         0.465833     0.543333      54.375000
    # 2019-03-22         0.468333     0.528333      54.083333
    # 2019-03-23         0.462500     0.539167      53.916667
    # 2019-03-24         0.467917     0.537917      54.958333
    # 2019-03-25         0.461250     0.530000      54.000000
    # 2019-03-26         0.456667     0.531250      54.166667
    # 2019-03-27         0.466667     0.530000      53.291667
    # 2019-03-28         0.468333     0.532083      53.291667
    # 2019-03-29         0.472917     0.538750      53.541667
    # 2019-03-30         0.463750     0.526250      54.458333
    # 2019-03-31         0.465833     0.522500      54.833333
    # 2019-04-01         0.468333     0.527083      53.333333
    # 2019-04-02         0.464583     0.515000      53.708333
    # 2019-04-03         0.472500     0.533333      54.583333
    # 2019-04-04         0.472083     0.531250      53.291667
    # 2019-04-05         0.451250     0.540000      53.833333
    # 2019-04-06         0.464167     0.531250      53.750000
    # 2019-04-07         0.472500     0.530417      54.541667
    # 2019-04-08         0.464583     0.534167      53.875000

    print(df.groupby(df.server_id).resample('M')['cpu_utilization', 'free_memory'].max())
    #                       cpu_utilization  free_memory
    # server_id datetime
    # 100       2019-03-31             0.56         0.62
    #           2019-04-30             0.55         0.61
    # 101       2019-03-31             0.91         0.32
    #           2019-04-30             0.89         0.30
    # 102       2019-03-31             0.85         0.36
    # ...                               ...          ...
    # 147       2019-04-30             0.61         0.57
    # 148       2019-03-31             0.84         0.35
    #           2019-04-30             0.83         0.34
    # 149       2019-03-31             0.85         0.36
    #           2019-04-30             0.83         0.34
    #
    # [100 rows x 2 columns]

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(24, 8))
    df.groupby(df.server_id).resample('M')['cpu_utilization'].mean().plot.bar(color=['green', 'gray'], ax=ax,
                                                                              title='The Average Monthly CPU Utilization Comparison')
    plt.show()


if __name__ == '__main__':
    method1()  # Timestamp 和 Period 对象的功能
    method2()  # 如何使用时间序列 DataFrames
    method3()  # 如何对时间序列进行切片
    method4()  # DateTimeIndex 对象及其方法
    method5()  # 如何重新采样时间序列数据
