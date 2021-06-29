参考资料：https://www.pythonf.cn/read/129031


- 终端启动服务
celery -A task worker -l info
celery -A task worker -l info -P eventlet(会报错)
  
- 运行celery_test(app).py
- （可选）运行check验证这个id的值



- celery+flask 异步请求测试
    - celery -A task worker -l info
    - python3 celery_test.py
    - postman 多窗口 发请求 localhost:5000/celery_flask_test