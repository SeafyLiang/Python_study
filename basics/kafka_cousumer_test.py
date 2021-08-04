#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   kafka_cousumer_test.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/8/3 13:25   SeafyLiang   1.0          kafka消费者
"""
import json
from kafka import KafkaProducer
from kafka import KafkaConsumer
import time

topicName = 'test_topic_name'
service = '192.168.10.62:9092'


def kafka_cousumer_test():
    consumer = KafkaConsumer(topicName, bootstrap_servers=[service])
    print(consumer)
    for msg in consumer:
        recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
        print(recv)


if __name__ == '__main__':
    kafka_cousumer_test()
