#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   timedTask_test.py    
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/12 13:45   SeafyLiang   1.0         定时任务测试
"""
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler


def job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


def method1():
    # 该示例代码生成了一个BlockingScheduler调度器，使用了默认的任务存储MemoryJobStore，以及默认的执行器ThreadPoolExecutor，并且最大线程数为10。

    # BlockingScheduler：在进程中运行单个任务，调度器是唯一运行的东西
    scheduler = BlockingScheduler()
    # 采用阻塞的方式

    # 采用固定时间间隔（interval）的方式，每隔5秒钟执行一次
    scheduler.add_job(job, 'interval', seconds=5)

    scheduler.start()


def method2():
    # BlockingScheduler：在进程中运行单个任务，调度器是唯一运行的东西
    scheduler = BlockingScheduler()
    # 采用阻塞的方式

    # 采用date的方式，在特定时间只执行一次
    scheduler.add_job(job, 'date', run_date='2018-09-21 15:30:00')

    scheduler.start()


def method3():
    # BackgroundScheduler: 适合于要求任何在程序后台运行的情况，当希望调度器在应用后台执行时使用。
    scheduler = BackgroundScheduler()
    # 采用非阻塞的方式

    # 采用固定时间间隔（interval）的方式，每隔3秒钟执行一次
    scheduler.add_job(job, 'interval', seconds=3)
    # 这是一个独立的线程
    scheduler.start()

    # 其他任务是独立的线程
    while True:
        print('main-start:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        time.sleep(2)
        print('main-end:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


def method4():
    # BackgroundScheduler: 适合于要求任何在程序后台运行的情况，当希望调度器在应用后台执行时使用。
    scheduler = BackgroundScheduler()
    # 采用非阻塞的方式

    # 采用date的方式，在特定时间里执行一次
    scheduler.add_job(job, 'date', run_date='2018-09-21 15:53:00')
    # 这是一个独立的线程
    scheduler.start()

    # 其他任务是独立的线程
    while True:
        print('main-start:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        time.sleep(2)
        print('main-end:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


def method5():
    # BackgroundScheduler: 适合于要求任何在程序后台运行的情况，当希望调度器在应用后台执行时使用
    scheduler = BackgroundScheduler()
    # 采用非阻塞的方式

    # 采用corn的方式
    scheduler.add_job(job, 'cron', day_of_week='fri', second='*/5')
    '''
    year (int|str) – 4-digit year
    month (int|str) – month (1-12)
    day (int|str) – day of the (1-31)
    week (int|str) – ISO week (1-53)
    day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
    hour (int|str) – hour (0-23)
    minute (int|str) – minute (0-59)
    econd (int|str) – second (0-59)

    start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
    end_date (datetime|str) – latest possible date/time to trigger on (inclusive)
    timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)

    *    any    Fire on every value
    */a    any    Fire every a values, starting from the minimum
    a-b    any    Fire on any value within the a-b range (a must be smaller than b)
    a-b/c    any    Fire every c values within the a-b range
    xth y    day    Fire on the x -th occurrence of weekday y within the month
    last x    day    Fire on the last occurrence of weekday x within the month
    last    day    Fire on the last day within the month
    x,y,z    any    Fire on any matching expression; can combine any number of any of the above expressions
    '''
    scheduler.start()

    # 其他任务是独立的线程
    while True:
        print('main-start:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        time.sleep(2)
        print('main-end:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


def method6():
    # BackgroundScheduler: 适合于要求任何在程序后台运行的情况，当希望调度器在应用后台执行时使用
    scheduler = BackgroundScheduler()
    # 采用阻塞的方式

    # 采用corn的方式
    scheduler.add_job(job, 'cron', day_of_week='fri', second='*/5')
    '''
    year (int|str) – 4-digit year
    month (int|str) – month (1-12)
    day (int|str) – day of the (1-31)
    week (int|str) – ISO week (1-53)
    day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
    hour (int|str) – hour (0-23)
    minute (int|str) – minute (0-59)
    econd (int|str) – second (0-59)

    start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
    end_date (datetime|str) – latest possible date/time to trigger on (inclusive)
    timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)

    *    any    Fire on every value
    */a    any    Fire every a values, starting from the minimum
    a-b    any    Fire on any value within the a-b range (a must be smaller than b)
    a-b/c    any    Fire every c values within the a-b range
    xth y    day    Fire on the x -th occurrence of weekday y within the month
    last x    day    Fire on the last occurrence of weekday x within the month
    last    day    Fire on the last day within the month
    x,y,z    any    Fire on any matching expression; can combine any number of any of the above expressions
    '''

    scheduler.start()


if __name__ == '__main__':
    method3()
