# 控制代码块

### if语句

Jinja2 语法中的if语句跟 Python 中的 if 语句相似,后面的布尔值或返回布尔值的表达式将决定代码中的哪个流程会被执行:

```python
{%if user.is_logged_in() %}
    <a href='/logout'>Logout</a>
{% else %}
    <a href='/login'>Login</a>
{% endif %}
```

过滤器可以被用在 if 语句中:

```python
{% if comments | length > 0 %}
    There are {{ comments | length }} comments
{% else %}
    There are no comments
{% endif %}
```

### 循环

* 我们可以在 Jinja2 中使用循环来迭代任何列表或者生成器函数

```python
{% for num in my_list %}
    {% if num > 3 %}
        {{ num }}
    {% endif %} <br>
{% endfor %}
```

* 循环和if语句可以组合使用

```python
{% for num in my_list if num > 3 %}
    {{ num }} <br>
{% endfor %}
```

- 在一个 for 循环块中你可以访问这些特殊的变量:

| 变量 | 描述 |
| :--- | :--- |
| loop.index | 当前循环迭代的次数（从 1 开始） |
| loop.index0 | 当前循环迭代的次数（从 0 开始） |
| loop.revindex | 到循环结束需要迭代的次数（从 1 开始） |
| loop.revindex0 | 到循环结束需要迭代的次数（从 0 开始） |
| loop.first | 如果是第一次迭代，为 True 。 |
| loop.last | 如果是最后一次迭代，为 True 。 |
| loop.length | 序列中的项目数。 |
| loop.cycle | 在一串序列间期取值的辅助函数。见下面示例程序。 |



* 在循环内部,你可以使用一个叫做loop的特殊变量来获得关于for循环的一些信息

  * 比如：要是我们想知道当前被迭代的元素序号，则可以使用loop变量的index属性,例如:

```python
{% for num in my_list %}
    {{ loop.index }} -
    {% if num > 3 %}
        {{ num }}
    {% endif %} <br>
{% endfor %}
```

  * 假设my_list=[1, 3, 5, 7, 9]会输出这样的结果

```python
1-
2-
3-5
4-7
5-9
```

  * cycle函数会在每次循环的时候,返回其参数中的下一个元素,可以拿上面的例子来说明:

```python
{% for num in my_list %}
    {{ loop.cycle('a', 'b') }} -
    {{ num }} <br>
{% endfor %}
```

* 会输出这样的结果：

```python
a-
b-
a-5
b-7
a-9

```

* 可以在循环的开始和结束位置放置一个 `-` 号去除for循环不换行情况下产生的空格

```python
{% for num in my_list -%}
    {{ num }}
{%- endfor %}
```



