参考资料：https://www.pythonf.cn/read/129031


- 终端启动服务
celery -A task worker -l info
celery -A task worker -l info -P eventlet(会报错)
  
- 运行celery_test(app).py
- （可选）运行check验证这个id的值
