#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   lock_test_demo01.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/7/14 15:02   SeafyLiang   1.0          python中的锁
"""
"""
线程安全问题

关于线程安全，有一个经典的“银行取钱”问题。从银行取钱的基本流程基本上可以分为如下几个步骤：
用户输入账户、密码，系统判断用户的账户、密码是否匹配。
用户输入取款金额。
系统判断账户余额是否大于取款金额。
如果余额大于取款金额，则取款成功；如果余额小于取款金额，则取款失败。

乍一看上去，这确实就是日常生活中的取款流程，这个流程没有任何问题。但一旦将这个流程放在多线程并发的场景下，就有可能出现问题。注意，此处说的是有可能，并不是说一定。也许你的程序运行了一百万次都没有出现问题，但没有出现问题并不等于没有问题！

按照上面的流程编写取款程序，井使用两个线程来模拟模拟两个人使用同一个账户井发取钱操作。此处忽略检查账户和密码的操作，仅仅模拟后面三步操作。下面先定义一个账户类，该账户类封装了账户编号和余额两个成员变量。
"""
import threading
import time


class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号、账户余额的两个成员变量
        self.account_no = account_no
        self.balance = balance

    """
    接下来程序会定义一个模拟取钱的函数，该函数根据执行账户、取钱数量进行取钱操作，取钱的逻辑是当账户余额不足时无法提取现金，当余额足够时系统吐出钞票，余额减少。
    
    程序的主程序非常简单，仅仅是创建一个账户，并启动两个线程从该账户中取钱。程序如下：
    """


# 定义一个函数来模拟取钱操作
def draw(account, draw_amount):
    # 账户余额大于取钱数目
    if account.balance >= draw_amount:
        # 吐出钞票
        print(threading.current_thread().name \
              + "取钱成功！吐出钞票:" + str(draw_amount))
        #        time.sleep(0.001)
        # 修改余额
        account.balance -= draw_amount
        print("\t余额为: " + str(account.balance))
    else:
        print(threading.current_thread().name \
              + "取钱失败！余额不足！")


# 创建一个账户
acct = Account("1234567", 1000)
# 模拟两个线程对同一个账户取钱
threading.Thread(name='甲', target=draw, args=(acct, 800)).start()
threading.Thread(name='乙', target=draw, args=(acct, 800)).start()
"""
多次运行会出现结果：
甲取钱成功！吐出钞票:800
乙取钱成功！吐出钞票:800
	余额为: 200	余额为: -600
"""


# 同步锁（Lock）
class AccountNew:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号、账户余额的两个成员变量
        self.account_no = account_no
        self._balance = balance
        self.lock = threading.RLock()

    # 因为账户余额不允许随便修改，所以只为self._balance提供getter方法
    def getBalance(self):
        return self._balance

    # 提供一个线程安全的draw()方法来完成取钱操作
    def draw(self, draw_amount):
        # 加锁
        self.lock.acquire()
        try:
            # 账户余额大于取钱数目
            if self._balance >= draw_amount:
                # 吐出钞票
                print(threading.current_thread().name \
                      + "取钱成功！吐出钞票:" + str(draw_amount))
                time.sleep(0.001)
                # 修改余额
                self._balance -= draw_amount
                print("\t余额为: " + str(self._balance))
            else:
                print(threading.current_thread().name \
                      + "取钱失败！余额不足！")
        finally:
            # 修改完成，释放锁
            self.lock.release()


# 定义一个函数来模拟取钱操作
def drawnew(account, draw_amount):
    # 直接调用account对象的draw()方法来执行取钱操作
    account.draw(draw_amount)


# 创建一个账户
acct = AccountNew("1234567", 1000)

print("\n同步锁（lock）#######")
# 模拟两个线程对同一个账户取钱
threading.Thread(name='甲', target=drawnew, args=(acct, 800)).start()
threading.Thread(name='乙', target=drawnew, args=(acct, 800)).start()
