# 获取请求中的数据

flask中代表当前请求的是request对象：

常用的属性如下：

| 属性 | 说明 | 类型 |
| :--- | :--- | :--- |
| method | 记录请求使用的HTTP方法 | GET/POST |
| headers | 记录请求中的报文头 | EnvironHeaders |
| url | 记录请求的URL地址 | string |
| cookies | 记录请求中的cookie信息 | Dict |
| args | 记录请求中的查询参数 | MultiDict |
| form | 记录请求中的表单数据 | MultiDict |
| data | 记录请求的数据，并转换为字符串 | \* |
| files | 记录请求上传的文件 | \* |



```python
# -*- coding:utf-8 -*-
from flask import Flask, request

@app.route('/', methods=['GET', 'POST'])
def hello_world():

    print 'method: %s' % request.method
    print 'headers: %s' % request.headers
    print 'url: %s' % request.url
    print 'cookies: %s' % request.cookies

    print 'args: %s' % request.args.get('name')
    print 'form: %s' % request.form.get('name')

    return 'Hello World!'
```
