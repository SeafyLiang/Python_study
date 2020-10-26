# 自定义过滤器

过滤器的本质是函数。当模板内置的过滤器不能满足需求，可以自定义过滤器。自定义过滤器有两种实现方式：
- 一种是通过Flask应用对象的 **add_template_filter** 方法
- 一种是通过装饰器来实现自定义过滤器

**重要：自定义的过滤器名称如果和内置的过滤器重名，会覆盖内置的过滤器。**

## 示例:自定义数组反转过滤器
### 方式一
通过调用应用程序实例的add_template_filter方法实现自定义过滤器。该方法第一个参数是函数名，第二个参数是自定义的过滤器名称：

```python
def do_list_reverse(list):
    list.reverse()
    return list
app.add_template_filter(do_list_reverse, 'lsreverse')
```

### 方式二
用装饰器来实现自定义过滤器。装饰器传入的参数是自定义的过滤器名称。

```python
@app.template_filter('lsreverse')
def do_list_reverse(list):
    list.reverse()
    return list
```
