#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   es_db_test.py
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/5/27 10:59   SeafyLiang   1.0          es_db_Test
"""
from elasticsearch import Elasticsearch

esclient = Elasticsearch(['localhost:9200'])
response = esclient.search(
    index='social-*',
    body={
        "query": {
            "match": {
                "message": "myProduct"
            }
        },
        "aggs": {
            "top_10_states": {
                "terms": {
                    "field": "state",
                    "size": 10
                }
            }
        }
    }
)
print(type(response))  # <class 'dict'>
print(response)  # {'took': 0, 'timed_out': False, '_shards': {'total': 0, 'successful': 0, 'skipped': 0, 'failed': 0}, 'hits': {'total': {'value': 0, 'relation': 'eq'}, 'max_score': 0.0, 'hits': []}}

