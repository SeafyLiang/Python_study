# 异常捕获

## abort 方法

抛出一个给定状态代码的 HTTPException，例如想要用一个页面未找到异常来终止请求，你可以调用 abort(404)。

参数: code – HTTP的错误状态码

```python
abort(404)
```
> 只能抛出HTTP协议的状态码

## errorhandler 装饰器

注册一个错误处理程序，当程序抛出指定错误状态码的时候，就会调用该装饰器所装饰的方法

参数：code_or_exception – HTTP的错误状态码或指定异常

- 例如统一处理状态码为500的错误给用户友好的提示：

```python
@app.errorhandler(404)
def internal_server_error(e):
    return '网页找不到了', 404
```

# 开启调试模式

开发时启动调试模式, 可以在浏览器中和编辑器控制台显示错误信息

```python
if __name__ == '__main__':
    app.run(debug=True)
```

