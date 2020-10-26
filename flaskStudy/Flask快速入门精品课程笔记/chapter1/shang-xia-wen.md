# 上下文

上下文：相当于一个容器，保存了Flask程序运行过程中的一些信息。

Flask中有两种上下文，请求上下文和应用上下文。

## 请求上下文(request context)

Flask从客户端收到请求时，要让视图函数能访问一些对象，这样才能处理请求。请求对象是一个很好的例子，它封装了客户端发送的HTTP请求。

要想让视图函数能够访问请求对象，一个显而易见的方式是将其作为参数传入视图函数，不过这会导致程序中的每个视图函数都增加一个参数，除了访问请求对象,如果视图函数在处理请求时还要访问其他对象，情况会变得更糟。为了避免大量可有可无的参数把视图函数弄得一团糟，Flask使用上下文临时把某些对象变为全局可访问。

- request 和 session 都属于请求上下文对象。
	- request：封装了HTTP请求的内容，针对的是http请求。举例：user = request.args.get('user')，获取的是get请求的参数。
	- session：用来记录请求会话中的信息，针对的是用户信息。举例：session['name'] = user.id，可以记录用户信息。还可以通过session.get('name')获取用户信息。



- 当调用app = Flask(__name__)的时候，创建了程序应用对象app；
- request 在每次http请求发生时，WSGI server调Flask.call()；然后在Flask内部创建的request对象；
- app的生命周期大于request，一个app存活期间，可能发生多次http请求，所以就会有多个request。
- 最终传入视图函数，通过return、redirect或render_template生成response对象，返回给客户端。
	
## 应用上下文(application context)
它的字面意思是 应用上下文，但它不是一直存在的，它只是request context 中的一个对 app 的代理(人)，所谓local proxy。它的作用主要是帮助 request 获取当前的应用，它是伴 request 而生，随 request 而灭的。

应用上下文对象有：current_app，g

### current_app

应用程序上下文,用于存储应用程序中的变量，可以通过current_app.name打印当前app的名称，也可以在current_app中存储一些变量，例如：
- 应用的启动脚本是哪个文件，启动时指定了哪些参数
- 加载了哪些配置文件，导入了哪些配置
- 连了哪个数据库
- 有哪些public的工具类、常量
- 应用跑再哪个机器上，IP多少，内存多大

```python
current_app.name
```
### g变量
g作为flask程序全局的一个临时变量,充当者中间媒介的作用,我们可以通过它传递一些数据，g保存的是当前请求的全局变量，不同的请求会有不同的全局变量，通过不同的thread id区别

```python
g.name='abc'
```


### 两者区别：

- 请求上下文：保存了客户端和服务器交互的数据
- 应用上下文：flask 应用程序运行过程中，保存的一些配置信息，比如程序名、数据库连接、应用信息等

> 请求上下文和应用上下文原理实现：https://segmentfault.com/a/1190000004223296
