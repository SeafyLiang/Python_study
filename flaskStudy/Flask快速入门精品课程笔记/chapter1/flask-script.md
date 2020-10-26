# Flask-Script

### 命令行启动服务器
通过使用Flask-Script扩展，我们可以在Flask服务器启动的时候，通过命令行的方式启动。

```python
from flask import Flask
from flask_script import Manager

app = Flask(__name__)
# 把 Manager 类和应用程序实例进行关联
manager = Manager(app)

@app.route('/')
def index():
return '床前明月光'

if __name__ == "__main__":
manager.run()
```

### script的命令行参数
传入参数而不仅仅通过app.run()方法中传参，比如我们可以通过：

```python
python hello.py runserver -host ip地址
```
以上代码告诉服务器在哪个网络接口监听来自客户端的连接。默认情况下，服务器只监听来自服务器所在的计算机发起的连接，即localhost连接。


 我们可以通过python hello.py runserver --help来查看参数。

 ![命令行](/assets/terminator.png)

