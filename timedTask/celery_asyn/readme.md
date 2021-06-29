参考资料：https://www.pythonf.cn/read/129031


- 启动服务(需要把timedTask.去掉才能启动成功)
celery -A celery_asyn worker -l info
celery -A celery_asyn worker -l info -P eventlet（会报错）

- 然后运行 produce.py 文件 
