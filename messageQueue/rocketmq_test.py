#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   rocketmq_test.py    
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/11 14:15   SeafyLiang   1.0          None
"""

# rocketmq==0.4.4
from rocketmq.client import Producer, Message
import time
from rocketmq.client import PushConsumer
from rocketmq.client import PullConsumer
import json

con_str = '192.168.10.35:9876'
msg = Message('test')  # topic


def produce_msg():
    """
    推送消息
    """
    producer = Producer('PID-001')  # 随便
    producer.set_namesrv_addr(con_str)  # ip和端口
    # 推送消息的时候，如果消息所占字节太长，需要手动设置size，代码中设置的是1M。
    # producer = Producer('PID-001', max_message_size=1024 * 1024)
    producer.start()
    msg.set_keys('2020-12-15')
    msg.set_tags('explain')
    msg.set_body('{"key":"value"}')
    """
    1、同步发送
    Producer 向 broker 发送消息，阻塞当前线程等待 broker 响应 发送结果。
    2、异步发送
    Producer 首先构建一个向 broker 发送消息的任务，把该任务提交给线程池，等执行完该任务时，回调用户自定义的回调函数，执行处理结果。
    3、Oneway 发送
    Oneway 方式只负责发送请求，不等待应答，Producer 只负责把请求发出去，而不处理响应结果。
    """
    ret = producer.send_sync(msg)
    print(ret.status, ret.msg_id, ret.offset)
    producer.shutdown()


def consume_msg_global():
    """
    消费方式PullConsumer（全部消费）（可重复消费）
    """
    consumer = PullConsumer('PID-001')
    consumer.set_namesrv_addr(con_str)
    consumer.start()
    for msg in consumer.pull('test'):
        print(msg.tags)
        print(msg.keys)
        print(msg.id, msg.body)
        print(msg.topic)
        print(msg)
        data = json.loads(str(msg))  # dict
    consumer.shutdown()


def consume_msg_once():
    """
    消费方式PushConsumer（即时消费）（不可重复消费）
    """
    def callback(msg):
        print(msg)
    consumer = PushConsumer('PID-001')
    consumer.set_namesrv_addr(con_str)
    consumer.subscribe("test", callback)
    consumer.start()
    while True:
        time.sleep(30)
    consumer.shutdown()


if __name__ == '__main__':
    # produce_msg()
    # consume_msg_global()
    consume_msg_once()