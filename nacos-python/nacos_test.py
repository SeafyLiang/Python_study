#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   nacos_test.py    
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/12 13:59   SeafyLiang   1.0      flask服务注册到nacos
"""
from flask import Flask
import nacos
import time
# 定时任务
from apscheduler.schedulers.background import BackgroundScheduler

SERVER_ADDRESSES = "192.168.10.35:8848"
NAMESPACE = "public"
# no auth mode
client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE)

"""初始化flask设置"""
app = Flask(__name__)


def regis_server_to_nacos():
    # auth mode
    # client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE, username="nacos", password="nacos")
    # get config
    data_id = "nacos.cfg.dataId"
    group = "test"
    print(client.get_config(data_id, group))
    client.add_naming_instance("algorithm", "192.168.10.35:8848", "5002")


def job():
    """
    定时任务，每隔20s向nacos发送消息
    @return:
    """
    client.send_heartbeat("algorithm", "192.168.10.35:8848", "5002")
    print('heart_nacos', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


def heart_nacos():
    """
    nacos心跳函数，防止nacos注册失效
    @return:
    """
    # BackgroundScheduler: 适合于要求任何在程序后台运行的情况，当希望调度器在应用后台执行时使用。
    scheduler = BackgroundScheduler()
    # 采用非阻塞的方式
    # 采用固定时间间隔（interval）的方式，每隔20秒钟执行一次
    scheduler.add_job(job, 'interval', seconds=20)
    # 这是一个独立的线程
    scheduler.start()


@app.route('/test')
def test():
    print("test ok!")


if __name__ == '__main__':
    """
    启动函数
    """
    regis_server_to_nacos()
    heart_nacos()
    app.run(debug=True, port=5001)
