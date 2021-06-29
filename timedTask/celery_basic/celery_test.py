#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   celery_test.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/6/29 09:13   SeafyLiang   1.0          python使用celery
"""
from task import add
from flask import Flask

app = Flask(__name__)  # __name__ 表示对应程序名称


@app.route("/celery_flask_test")
def index():
    print("Start Task ...")
    result = add.delay(2, 8)
    print("result:", result)  # 存到redis之后，返回的id
    print("result_id:", result.id)  # 存到redis之后，返回的id
    print("result:", result.get())  # 方法返回值
    print("End Task ...")
    return "celery flask test ok!"


if __name__ == '__main__':
    app.run()

# celery -A task worker -l info
# python3 celery_test.py
# postman 多窗口 发请求 localhost:5000/celery_flask_test
