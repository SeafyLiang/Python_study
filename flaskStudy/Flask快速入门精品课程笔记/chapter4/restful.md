# RESTful

2000年，Roy Thomas Fielding博士在他的博士论文《Architectural Styles and the Design of Network-based Software Architectures》中提出了几种软件应用的架构风格，REST作为其中的一种架构风格在这篇论文中进行了概括性的介绍。

REST:Representational State Transfer的缩写，翻译：“具象状态传输”。一般解释为“表现层状态转换”。

REST是设计风格而不是标准。是指客户端和服务器的交互形式。我们需要关注的重点是如何设计REST风格的网络接口。

* REST的特点：
* 具象的。一般指表现层，要表现的对象就是资源。比如，客户端访问服务器，获取的数据就是资源。比如文字、图片、音视频等。

* 表现：资源的表现形式。txt格式、html格式、json格式、jpg格式等。浏览器通过URL确定资源的位置，但是需要在HTTP请求头中，用Accept和Content-Type字段指定，这两个字段是对资源表现的描述。

* 状态转换：客户端和服务器交互的过程。在这个过程中，一定会有数据和状态的转化，这种转化叫做状态转换。其中，GET表示获取资源，POST表示新建资源，PUT表示更新资源，DELETE表示删除资源。HTTP协议中最常用的就是这四种操作方式。

  * RESTful架构：
  * 每个URL代表一种资源；
  * 客户端和服务器之间，传递这种资源的某种表现层；
  * 客户端通过四个http动词，对服务器资源进行操作，实现表现层状态转换。

## 如何设计符合RESTful风格的API：

### 一、域名：

将api部署在专用域名下：

```
http://api.example.com

```

或者将api放在主域名下：

```
http://www.example.com/api/

```

### 二、版本： {#二、版本：}

将API的版本号放在url中。

```
http://www.example.com/app/1.0/info
http://www.example.com/app/1.2/info
```

### 三、路径：

路径表示API的具体网址。每个网址代表一种资源。 资源作为网址，网址中不能有动词只能有名词，一般名词要与数据库的表名对应。而且名词要使用复数。

错误示例：

```
http://www.example.com/getGoods
http://www.example.com/listOrders

```

正确示例：

```
#获取单个商品

http://www.example.com/app/goods/1
#获取所有商品

http://www.example.com/app/goods
```

### 四、使用标准的HTTP方法： {#四、使用标准的http方法：}

对于资源的具体操作类型，由HTTP动词表示。 常用的HTTP动词有四个。

```
GET     SELECT ：从服务器获取资源。
POST    CREATE ：在服务器新建资源。
PUT     UPDATE ：在服务器更新资源。
DELETE  DELETE ：从服务器删除资源。

```

示例：

```
#获取指定商品的信息

GET http://www.example.com/goods/ID

#新建商品的信息

POST http://www.example.com/goods

#更新指定商品的信息

PUT http://www.example.com/goods/ID

#删除指定商品的信息

DELETE http://www.example.com/goods/ID

```

### 五、过滤信息：

如果资源数据较多，服务器不能将所有数据一次全部返回给客户端。API应该提供参数，过滤返回结果。 实例：

```
#指定返回数据的数量

http://www.example.com/goods?limit=10
#指定返回数据的开始位置

http://www.example.com/goods?offset=10
#指定第几页，以及每页数据的数量

http://www.example.com/goods?page=2&per_page=20
```

### 六、状态码： {#六、状态码：}

服务器向用户返回的状态码和提示信息，常用的有：

```
200 OK  ：服务器成功返回用户请求的数据
201 CREATED ：用户新建或修改数据成功。
202 Accepted：表示请求已进入后台排队。
400 INVALID REQUEST ：用户发出的请求有错误。
401 Unauthorized ：用户没有权限。
403 Forbidden ：访问被禁止。
404 NOT FOUND ：请求针对的是不存在的记录。
406 Not Acceptable ：用户请求的的格式不正确。
500 INTERNAL SERVER ERROR ：服务器发生错误。
```

### 七、错误信息： {#七、错误信息：}

一般来说，服务器返回的错误信息，以键值对的形式返回。

```
{
    error: 'Invalid API KEY'
}

```

### 八、响应结果： {#八、响应结果：}

针对不同结果，服务器向客户端返回的结果应符合以下规范。

```
#返回商品列表

GET    http://www.example.com/goods

#返回单个商品

GET    http://www.example.com/goods/cup

#返回新生成的商品

POST   http://www.example.com/goods

#返回一个空文档

DELETE http://www.example.com/goods

```

### 九、使用链接关联相关的资源：

在返回响应结果时提供链接其他API的方法，使客户端很方便的获取相关联的信息。

### 十、其他：

服务器返回的数据格式，应该尽量使用JSON，避免使用XML。

