# 状态保持

- 因为http是一种无状态协议，不会保持某一次请求所产生的信息，如果想实现状态保持，在开发中解决方式有：
    - cookie：数据存储在客户端，节省服务器空间，但是不安全
    - session：会话，数据存储在服务器端
    
> 无状态协议：
> 1. 协议对于事务处理没有记忆能力
> 2. 对同一个url请求没有上下文关系
> 3. 每次的请求都是独立的，它的执行情况和结果与前面的请求和之后的请求是无直接关系的，它不会受前面的请求应答情况直接影响，也不会直接影响后面的请求应答情况
> 4. 服务器中没有保存客户端的状态，客户端必须每次带上自己的状态去请求服务器
> 5. 人生若只如初见


### 设置cookie

```python

from flask imoprt Flask,make_response
@app.route('/cookie')
def set_cookie():
	resp = make_response('this is to set cookie')
	resp.set_cookie('username', 'itcast')
	return resp
```

![设置cookie](/assets/cookie.png)


### 获取cookie

```python

from flask import Flask,request
#获取cookie
@app.route('/request')
def resp_cookie():
    resp = request.cookies.get('username')
    return resp

```

![获取cookie](/assets/获取cookie.png)

### session数据的设置与获取

session:请求上下文对象，用于处理http请求中的一些数据内容
> 记得设置secret_key: app.secret_key = 'itheima'
> secret_key的作用：https://segmentfault.com/q/1010000007295395
	
```python
from flask import Flask, session, redirect, url_for
@app.route('/set_session')
def set_session():
	session['username'] = 'itcast'
	return redirect(url_for('get_session'))
	
@app.route('/get_session')
def get_session():
	return session.get('username')
```



### Flask的session存放位置

flask和之前用过的其他框架有一点不同的是，它的session默认是完全保留在客户端浏览器中的，也就是说往flask的session中写入数据，最终这些数据将会以json字符串的形式，经过base64编码写入到用户浏览器的cookie里，也就是说无须依赖第三方数据库保存session数据，也无需依赖文件来保存
![](/assets/Flask中Session存放位置.png)
