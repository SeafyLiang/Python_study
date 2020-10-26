# -*- coding:utf-8 -*-
'''

In [1]: from Flask_SQLalchemy_demo import *

添加数据

In [2]: role = Role(name='admin')

In [3]: db.session.add(role)

In [4]: db.session.commit()

In [5]: user = User(name='heima', role_id=role.id)

In [6]: db.session.add(user)

In [7]: db.session.commit()



修改数据
In [8]: user.name = 'chengxuyuan'

In [9]: db.session.commit()


删除数据
In [10]: db.session.delete(user)

In [11]: db.session.commit()

'''



'''


In [1]: from Flask_SQLalchemy_demo import * 

添加一个角色和两个用户
In [2]: role = Role(name='admin')

In [3]: db.session.add(role)

In [4]: db.session.commit()

In [5]: user1 = User(name='zs', role_id=role.id)

In [6]: user2 = User(name='ls', role_id=role.id)

In [7]: db.session.add_all([user1, user2])

In [8]: db.session.commit()

实现关系引用查询

In [9]: role.users
Out[9]: [<User: zs 1 None None>, <User: ls 2 None None>]

In [10]: user1.role
Out[10]: <Role: admin 1>

In [11]: user2.role.name
Out[11]: u'admin'

'''


'''
In [1]: from Flask_SQLalchemy_demo import * 

In [2]: User.query.all()
Out[2]: 
[<User: wang 1 wang@163.com 123456>,
 <User: zhang 2 zhang@189.com 201512>,
 <User: chen 3 chen@126.com 987654>,
 <User: zhou 4 zhou@163.com 456789>,
 <User: tang 5 tang@itheima.com 158104>,
 <User: wu 6 wu@gmail.com 5623514>,
 <User: qian 7 qian@gmail.com 1543567>,
 <User: liu 8 liu@itheima.com 867322>,
 <User: li 9 li@163.com 4526342>,
 <User: sun 10 sun@163.com 235523>]

In [3]: User.query.count()
Out[3]: 10L

In [4]: User.query.first()
Out[4]: <User: wang 1 wang@163.com 123456>

In [5]: User.query.get(4)
Out[5]: <User: zhou 4 zhou@163.com 456789>

In [6]: User.query.filter_by(id=4).first()
Out[6]: <User: zhou 4 zhou@163.com 456789>

In [7]: User.query.filter(User.id==4).first()
Out[7]: <User: zhou 4 zhou@163.com 456789>


filter_by: 属性=
filter: 对象.属性==
filter功能更强大, 可以实现更多的一些查询, 支持比较运算符
'''