# 数据库迁移

- 在开发过程中，需要修改数据库模型，而且还要在修改之后更新数据库。最直接的方式就是删除旧表，但这样会丢失数据。
- 更好的解决办法是使用数据库迁移框架，它可以追踪数据库模式的变化，然后把变动应用到数据库中。
- 在Flask中可以使用Flask-Migrate扩展，来实现数据迁移。并且集成到Flask-Script中，所有操作通过命令就能完成。
- 为了导出数据库迁移命令，Flask-Migrate提供了一个MigrateCommand类，可以附加到flask-script的manager对象上。

首先要在虚拟环境中安装Flask-Migrate。

```
pip install flask-migrate
```
- 代码文件内容：

```python
#coding=utf-8
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Shell,Manager

app = Flask(__name__)
manager = Manager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/Flask_test'
db = SQLAlchemy(app)

#第一个参数是Flask的实例，第二个参数是Sqlalchemy数据库实例
migrate = Migrate(app,db) 

#manager是Flask-Script的实例，这条语句在flask-Script中添加一个db命令
manager.add_command('db',MigrateCommand)

#定义模型Role
class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    user = db.relationship('User', backref='role')

    #repr()方法显示一个可读字符串，
    def __repr__(self):
        return 'Role:'.format(self.name)

#定义用户
class User(db.Model):
    __talbe__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    #设置外键
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'User:'.format(self.username)


if __name__ == '__main__':
    manager.run()

```

###创建迁移仓库

```
#这个命令会创建migrations文件夹，所有迁移文件都放在里面。
python database.py db init
```

![创建迁移仓库](/assets/db_init.png)

###创建迁移脚本

- 自动创建迁移脚本有两个函数
	- upgrade()：函数把迁移中的改动应用到数据库中。
	- downgrade()：函数则将改动删除。
- 自动创建的迁移脚本会根据模型定义和数据库当前状态的差异，生成upgrade()和downgrade()函数的内容。
- 对比不一定完全正确，有可能会遗漏一些细节，需要进行检查

```
python database.py db migrate -m 'initial migration'
```

![创建迁移脚本](/assets/migration.png)

### 更新数据库
```
python database.py db upgrade
```

### 返回以前的版本

可以根据history命令找到版本号,然后传给downgrade命令:

```
python app.py db history

输出格式：<base> ->  版本号 (head), initial migration

```
- 回滚到指定版本

```
python app.py db downgrade 版本号
```
###实际操作顺序:
- 1.python 文件 db init
- 2.python 文件 db migrate -m"版本名(注释)"
- 3.python 文件 db upgrade 然后观察表结构
- 4.根据需求修改模型
- 5.python 文件 db migrate -m"新版本名(注释)" 
- 6.python 文件 db upgrade 然后观察表结构
- 7.若返回版本,则利用 python 文件 db history查看版本号
- 8.python 文件 db downgrade(upgrade) 版本号