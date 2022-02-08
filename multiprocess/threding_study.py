#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   threding_study.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/2/8 21:22   SeafyLiang   1.0       使用threading实现多线程
"""
import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.delay, 5)
        print("退出线程：" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")
