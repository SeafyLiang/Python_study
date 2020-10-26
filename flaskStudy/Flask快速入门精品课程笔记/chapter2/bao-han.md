# Flask特有的变量和函数

你可以在自己的模板中访问一些Flask默认内置的函数和对象

#### config

你可以从模板中直接访问Flask当前的config对象:

```python
{{ config.root_path }}
/Users/Andy/Desktop/Codes/flask_demo
```

#### request

就是flask中代表当前请求的request对象：

```python
{{request.url}}
http://127.0.0.1:5000/
```

#### url\_for\(\)

url\_for会根据传入的路由器函数名,返回该路由对应的URL,在模板中始终使用url\_for\(\)就可以安全的修改路由绑定的URL,则不比担心模板中渲染出错的链接:

```python
url_for('hello_world')
/
```

如果我们定义的路由URL是带有参数的,则可以把它们作为关键字参数传入url\_for\(\),Flask会把他们填充进最终生成的URL中:

```python
{{ url_for('user', user_id=1)}}
/user/1
```

#### session

为Flask的session对象

```python
{{ session.get('name') }}
```

#### g
应用上下文, 可以再一次请求中方便的进行属性值的传递
```python
{{ g.age }}
```

##### get\_flashed\_messages\(\)

这个函数会返回之前在flask中通过flash\(\)传入的消息的列表，flash函数的作用很简单,可以把由Python字符串表示的消息加入一个消息队列中，再使用get\_flashed\_message\(\)函数取出它们并消费掉：

```python
{%for message in get_flashed_messages()%}
    {{message}}
{%endfor%}
```



