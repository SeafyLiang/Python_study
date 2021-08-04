#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   kafka_producer_test.py
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/8/3 11:04   SeafyLiang   1.0          kafka生产者
"""
import datetime
import json
from kafka import KafkaProducer
from kafka.errors import KafkaError
import time


class Kafka_producer():
    def __init__(self, bootstrapServers, kafkaTopic):
        self.bootstrapServers = bootstrapServers
        self.kafkaTopic = kafkaTopic
        self.producer = KafkaProducer(bootstrap_servers=self.bootstrapServers)

    def sendjsondata(self, params):
        try:
            parmas_message = json.dumps(params)
            producer = self.producer
            future = producer.send(self.kafkaTopic, parmas_message.encode('utf-8'))
            producer.flush()
            recordMetadata = future.get(timeout=10)
            print(recordMetadata, datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        except KafkaError as e:
            print(e)


if __name__ == '__main__':
    bootstrapServers = ['192.168.10.62:9092']
    topicStr = 'test_topic_name'

    print('-' * 20)
    print('生产者')
    print('-' * 20)

    producer = Kafka_producer(bootstrapServers, topicStr)
    for id in range(10000):
        params = {'demo01': 'hhh'}
        producer.sendjsondata(params)
        time.sleep(0.005)
    print('end')
