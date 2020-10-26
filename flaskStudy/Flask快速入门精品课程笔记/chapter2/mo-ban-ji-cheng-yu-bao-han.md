# 模板代码复用
## 一. 继承

模板继承是为了重用模板中的公共内容。一般Web开发中，继承主要使用在网站的顶部菜单、底部。这些内容可以定义在父模板中，子模板直接继承，而不需要重复书写。

- 标签定义的内容

```python
{% block top %} {% endblock %}
```

- 相当于在父模板中挖个坑，当子模板继承父模板时，可以进行填充。
- 子模板使用extends指令声明这个模板继承自哪个模板
- 父模板中定义的块在子模板中被重新定义，在子模板中调用父模板的内容可以使用super()


### 父模板

- base.html

```python
{% block top %}
    <h1>这是头部内容</h1>
{% endblock %}


{% block center %}
    这是父类的中间的内容
{% endblock %}


{% block bottom %}
    <h1>这是底部内容</h1>
{% endblock %}
```

### 子模板

- extends指令声明这个模板继承自哪

```python
{% extends 'base.html' %}

{% block content %}
    {{ super() }} <br>
    需要填充的内容 <br>
{% endblock content %}
```

### 模板继承使用时注意点：
    - 不支持多继承
    - 为了便于阅读，在子模板中使用extends时，尽量写在模板的第一行。
    - 不能在一个模板文件中定义多个相同名字的block标签。
    - 当在页面中使用多个block标签时，建议给结束标签起个名字，当多个block嵌套时，阅读性更好。

## 二. 包含

Jinja2模板中，包含(Include)的功能是将另一个模板整个加载到当前模板中，并直接渲染。

- include的使用

```python
{% include 'hello.html' %}
```

包含在使用时，如果包含的模板文件不存在时，程序会抛出**TemplateNotFound**异常，可以加上 `ignore missing` 关键字。如果包含的模板文件不存在，会忽略这条include语句。

- include的使用加上关键字ignore missing

```python
{% include 'hello.html' ignore missing %}
```


## 四. 模板代码复用方式小结
 继承(Block)、包含(include)均能实现代码的复用。
- 继承(Block)的本质是代码替换，一般用来实现多个页面中重复不变的区域。
- 包含(include)是直接将目标模板文件整个渲染出来。