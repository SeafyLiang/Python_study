# 蓝图(Blueprint)
### 模块化
随着flask程序越来越复杂,我们需要对程序进行模块化的处理,之前学习过python的模块化管理,于是针对一个简单的flask程序进行模块化处理

举例来说:

我们有一个博客程序,前台界面需要的路由为:首页,列表,详情等页面

```python
源程序app.py文件:
from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/list')
def list():
    return 'list'

@app.route('/detail')
def detail():
    return 'detail'

if __name__=='__main__':
    app.run()
```

如果博主需要编辑博客,要进入后台进行处理:后台主页,编辑,创建,发布博客

```python
改进后程序:
from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/list')
def list():
    return 'list'

@app.route('/detail')
def detail():
    return 'detail'

@app.route('/')
def admin_home():
    return 'admin_home'

@app.route('/new')
def new():
    return 'new'

@app.route('/edit')
def edit():
    return 'edit'

@app.route('/publish')
def publish():
    return 'publish'

if __name__=='__main__':
    app.run()
```

这样就使得我们在一个py文件中写入了很多路由,将来维护代码会非常麻烦,此时,同学们就考虑到了模块化的处理方式,将admin相关的路由写到一个admin.py文件中,那我们就顺着这个思路走下去

```python
修改后的代码:
app.py
from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/list')
def list():
    return 'list'

@app.route('/detail')
def detail():
    return 'detail'

if __name__=='__main__':
    app.run()

admin.py

@app.route('/')
def admin_home():
    return 'admin_home'

@app.route('/new')
def new():
    return 'new'

@app.route('/edit')
def edit():
    return 'edit'

@app.route('/publish')
def publish():
    return 'publish'
```
发现admin.py文件中的app直接报错,代码无法继续写下去,所以在flask程序中,使用传统的模块化是行不通的,需要flask提供一个特有的模块化处理方式,flask内置了一个模块化处理的类,即Blueprint
###Blueprint概念
简单来说，Blueprint 是一个存储操作方法的容器，这些操作在这个Blueprint 被注册到一个应用之后就可以被调用，Flask 可以通过Blueprint来组织URL以及处理请求。

Flask使用Blueprint让应用实现模块化，在Flask中，Blueprint具有如下属性：

- 一个应用可以具有多个Blueprint
- 可以将一个Blueprint注册到任何一个未使用的URL下比如 “/”、“/sample”或者子域名
- 在一个应用中，一个模块可以注册多次
- Blueprint可以单独具有自己的模板、静态文件或者其它的通用操作方法，它并不是必须要实现应用的视图和函数的
- 在一个应用初始化时，就应该要注册需要使用的Blueprint

但是一个Blueprint并不是一个完整的应用，它不能独立于应用运行，而必须要注册到某一个应用中。

###初识蓝图
蓝图/Blueprint对象用起来和一个应用/Flask对象差不多，最大的区别在于一个 蓝图对象没有办法独立运行，必须将它注册到一个应用对象上才能生效

使用蓝图可以分为三个步骤

- 1,创建一个蓝图对象

```python
admin=Blueprint('admin',__name__)
```
- 2,在这个蓝图对象上进行操作,注册路由,指定静态文件夹,注册模版过滤器

```python
@admin.route('/')
def admin_home():
	return 'admin_home'
```

- 3,在应用对象上注册这个蓝图对象

```python
app.register_blueprint(admin,url\_prefix='/admin')
```

当这个应用启动后,通过/admin/可以访问到蓝图中定义的视图函数

###运行机制

- 蓝图是保存了一组将来可以在应用对象上执行的操作，注册路由就是一种操作
- 当在应用对象上调用 route 装饰器注册路由时,这个操作将修改对象的url\_map路由表
- 然而，蓝图对象根本没有路由表，当我们在蓝图对象上调用route装饰器注册路由时,它只是在内部的一个延迟操作记录列表defered\_functions中添加了一个项
- 当执行应用对象的 register\_blueprint() 方法时，应用对象将从蓝图对象的 defered\_functions 列表中取出每一项，并以自身作为参数执行该匿名函数，即调用应用对象的 add\_url\_rule() 方法，这将真正的修改应用对象的路由表

###蓝图的url前缀

- 当我们在应用对象上注册一个蓝图时，可以指定一个url_prefix关键字参数（这个参数默认是/）
- 在应用最终的路由表 url\_map中，在蓝图上注册的路由URL自动被加上了这个前缀，这个可以保证在多个蓝图中使用相同的URL规则而不会最终引起冲突，只要在注册蓝图时将不同的蓝图挂接到不同的自路径即可

- url_for

```python
url_for('admin.index') # /admin/
```
###注册静态路由
和应用对象不同，蓝图对象创建时不会默认注册静态目录的路由。需要我们在 创建时指定 static_folder 参数。

下面的示例将蓝图所在目录下的static_admin目录设置为静态目录

```python
admin = Blueprint("admin",__name__,static_folder='static_admin')
app.register_blueprint(admin,url_prefix='/admin')
```

现在就可以使用/admin/static\_admin/<filename> 访问static\_admin目录下的静态文件了
定制静态目录URL规则 ：可以在创建蓝图对象时使用 static\_url_path 来改变静态目录的路由。下面的示例将为static\_admin文件夹的路由设置为 /lib

```python
admin = Blueprint("admin",__name__,static_folder='static_admin',static_url_path='/lib')
app.register_blueprint(admin,url_prefix='/admin')
```

###设置模版目录
蓝图对象默认的模板目录为系统的模版目录，可以在创建蓝图对象时使用 template_folder 关键字参数设置模板目录

```python
admin = Blueprint('admin',__name__,template_folder='my_templates')
```

注:如果在templates中存在和my_templates同名文件,则系统会优先使用templates中的文件,在使用templates目录同名的情况下,需要通过路径区分,例如:

my_templates存在两个,若使用admin目录下的my\_templates目录,则需要使用如下方式注册:

	admin = Blueprint('admin',__name__,template_folder='admin/my_templates')
