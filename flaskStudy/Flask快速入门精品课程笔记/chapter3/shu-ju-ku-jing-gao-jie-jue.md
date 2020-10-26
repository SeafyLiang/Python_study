# 数据库警告解决

连接数据库时, 控制台可能会输出一个警告信息

```
/home/python/.virtualenvs/flask_py/local/lib/python2.7/site-packages/sqlalchemy/dialects/mysql/base.py:1569: Warning: (1287L, u"'@@tx_isolation' is deprecated and will be removed in a future release. Please use '@@transaction_isolation' instead")
  cursor.execute('SELECT @@tx_isolation')
```

这个问题是因为Mysqld的高版本中, 对事务的处理进行了调整. 而SQLALChemy使用了低版本的方式, 导致了警告信息. SQLALChemy的作者已经发现了问题, 但并未将解决方案应用到扩展中.

https://github.com/zzzeek/sqlalchemy/pull/391/files

```
官方问题连接:
https://github.com/zzzeek/sqlalchemy/pull/391/filess

简单的处理办法是按照提示用@@transaction_isolation替换@@tx_isolation.
如果要考虑到版本兼容问题, 可以使用下图的方式
```
![](/assets/SQLAlchemy警告.png)


