###创建表

```python
if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug=True)

```
- 查看创建结果

```sql
show tables;
```
![创建表](/assets/create_table.png)

###查看author表结构 
```sql
desc author;
```
![author表结构](/assets/author_table_struc.png)
###查看books表结构 

```sql
desc books;
```
![books表结构](/assets/books_table_struc.png)


### 添加测试数据

```python
#生成数据
au1 = Author(name='老王')
au2 = Author(name='主播')
au3 = Author(name='老刘')
# 把数据提交给用户会话
db.session.add_all([au1, au2, au3])
# 提交会话
db.session.commit()
bk1 = Book(name='老王回忆录', author_id=au1.id)
bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
# 把数据提交给用户会话
db.session.add_all([bk1, bk2, bk3, bk4, bk5])
# 提交会话
db.session.commit()
```

###生成数据后，查看数据

