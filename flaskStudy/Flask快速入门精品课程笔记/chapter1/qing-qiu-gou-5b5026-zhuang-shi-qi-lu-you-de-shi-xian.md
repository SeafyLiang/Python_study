# 请求钩子

在客户端和服务器交互的过程中，有些准备工作或扫尾工作需要处理，比如：在请求开始时，建立数据库连接；在请求结束时，指定数据的交互格式。为了让每个视图函数避免编写重复功能的代码，Flask提供了通用设施的功能，即请求钩子。

请求钩子是通过装饰器的形式实现，类似于Django的中间件. Flask支持如下四种请求钩子：
- before_first_request：在处理第一个请求前运行。
- before_request：在每次请求前运行。
- after_request：如果没有未处理的异常抛出，在每次请求后运行。
- teardown_request：在每次请求后运行，即使有未处理的异常抛出。


```python
@app.route('/')
def hello_world():
    print '这里正在执行处理逻辑'
    return 'Hello World!'


# 在处理第一个请求前运行. 应用场景: 比如连接数据库操作
@app.before_first_request
def before_first_request():
    print 'before_first_request'

# 在每次请求前运行。应用场景: 比如对数据做效验. 如果数据有问题, 可以直接返回. 就不会再去执行对应的视图函数
@app.before_request
def before_request():
    print 'before_request'
    # return 'hehe'

# 如果没有未处理的异常抛出, 在每次请求后运行。应用场景: 比如拼接响应头信息. 让所有json.dumps()的数据, 统一增加Content-Type为application/json
@app.after_request
def after_request(response):
    print 'after_request'
    response.headers['Content-Type'] = 'application/json'
    return response


# 在每次请求最后运行，即使有未处理的异常抛出。 可以捕获到异常信息
@app.teardown_request
def teardown_request(e):
    print 'teardown_request %s' % e
```
