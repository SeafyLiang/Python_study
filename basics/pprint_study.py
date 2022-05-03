#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   pprint_study.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/5/3 17:27   SeafyLiang   1.0        pprint模块-宽度&缩进
"""
'''
参考资料：https://mp.weixin.qq.com/s/dvyUkRWl70xME_cqVKNkxQ
'''
from pprint import pprint

d = {
    "apple": {"juice": 4, "pie": 5},
    "orange": {"juice": 6, "cake": 7},
    "pear": {"cake": 8, "pie": 9}
}
print(d)
# {'apple': {'juice': 4, 'pie': 5}, 'orange': {'juice': 6, 'cake': 7}, 'pear': {'cake': 8, 'pie': 9}}
for k, v in d.items():
    print(k, "->", v)
# apple -> {'juice': 4, 'pie': 5}
# orange -> {'juice': 6, 'cake': 7}
# pear -> {'cake': 8, 'pie': 9}
pprint(d)
# {'apple': {'juice': 4, 'pie': 5},
#  'orange': {'cake': 7, 'juice': 6},
#  'pear': {'cake': 8, 'pie': 9}}

d = {
    "apple": {
        "juice": {1: 2, 3: 4, 5: 6},
        "pie": {1: 3, 2: 4, 5: 7},
    },
    "orange": {
        "juice": {1: 5, 2: 3, 5: 6},
        "cake": {5: 4, 3: 2, 6: 5},
    },

    "pear": {
        "cake": {1: 6, 6: 1, 7: 8},
        "pie": {3: 5, 5: 3, 8: 7},
    }
}
# 设定输出宽度
pprint(d)
pprint(d, width=50)
pprint(d, width=30)

# 设定输出缩进
pprint(d, indent=4)
pprint(d, indent=8)
