#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   logUseTest.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/3/30 22:50   SeafyLiang   1.0         日志使用
"""
import logging
import logging.handlers


def method1():
    """
    方法1：配置并输出日志到标准输出
    """
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

    logging.info("清空重建表")
    # > 2021-03-30 22:54:36,937 - INFO - 清空重建表


def method2():
    """
    方法2：配置输出到日志文件
    日志文件，会每天备份一个文件，并且只保留7天的日志
    """
    LOG_FILE = "test_log.log"
    logging.basicConfig(filename=LOG_FILE,
                        filemode="w",
                        format="[%(levelname)s] %(asctime)s [%(filename)s:%(lineno)d, %(funcName)s] %(message)s",
                        level=logging.INFO)
    time_hdls = logging.handlers.TimedRotatingFileHandler(LOG_FILE, when='D', interval=1, backupCount=7)
    logging.getLogger().addHandler(time_hdls)

    logging.info("hello world")
    # > [INFO] 2021-03-30 22:52:50,440 [logUseTest.py:35, <module>] hello world


if __name__ == '__main__':
    method2()
