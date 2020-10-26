# 部署

## 一. 使用gunicorn和nginx部署
当我们执行下面的hello.py时，使用的flask自带的服务器，完成了web服务的启动。在生产环境中，flask自带的服务器，无法满足性能要求，我们这里采用Gunicorn做wsgi容器，来部署flask程序。Gunicorn（绿色独角兽）是一个Python WSGI的HTTP服务器。从Ruby的独角兽（Unicorn ）项目移植。该Gunicorn服务器与各种Web框架兼容，实现非常简单，轻量级的资源消耗。Gunicorn直接用命令启动，不需要编写配置文件，相对uWSGI要容易很多。

区分几个概念：

**WSGI**：全称是Web Server Gateway Interface（web服务器网关接口），它是一种规范，它是web服务器和web应用程序之间的接口。它的作用就像是桥梁，连接在web服务器和web应用框架之间。

**uwsgi**：是一种传输协议，用于定义传输信息的类型。

**uWSGI**：是实现了uwsgi协议WSGI的web服务器。

我们的部署方式： nginx + gunicorn + flask

### 使用Gunicorn：
web开发中，部署方式大致类似。简单来说，前端代理使用Nginx主要是为了实现分流、转发、负载均衡，以及分担服务器的压力。Nginx部署简单，内存消耗少，成本低。Nginx既可以做正向代理，也可以做反向代理。

正向代理：请求经过代理服务器从局域网发出，然后到达互联网上的服务器。

特点：服务端并不知道真正的客户端是谁。

反向代理：请求从互联网发出，先进入代理服务器，再转发给局域网内的服务器。

特点：客户端并不知道真正的服务端是谁。

区别：正向代理的对象是客户端。反向代理的对象是服务端。

**安装gunicorn**

```
pip install gunicorn

```

**查看命令行选项**： 安装gunicorn成功后，通过命令行的方式可以查看gunicorn的使用信息。

```
$gunicorn -h

```

**直接运行**：

```
#直接运行，默认启动的127.0.0.1:8000
gunicorn 运行文件名称:Flask程序实例名
```

**指定进程和端口号**： -w: 表示进程（worker）。 -b：表示绑定ip地址和端口号（bind）。-D：表示以守护进程方式运行。


```
$gunicorn -w 4 -b 127.0.0.1:5001 -D 运行文件名称:Flask程序实例名

```

### 安装Nginx

```
$ sudo apt-get install nginx
```


### Nginx配置
默认安装到/usr/local/nginx/目录，进入目录。


```
$ sudo /usr/local/nginx/conf/nginx.conf
```


### 启动nginx

```
#启动
sudo sbin/nginx
#查看
ps aux | grep nginx
#停止
sudo sbin/nginx -s stop
#重启
sudo sbin/nginx -s reload
```


打开/usr/local/nginx/conf/nginx.conf文件

```
server {
    # 监听80端口
    listen 80;
    # 本机
    server_name localhost; 
    # 默认请求的url
    location / {
        #请求转发到gunicorn服务器
        proxy_pass http://127.0.0.1:5001; 
        #设置请求头，并将头信息传递给服务器端 
        proxy_set_header Host $host; 
    }
}
```



## 二. 使用uWSGI和nginx进行服务器部署

区分几个概念：

**WSGI**：

* 全称是Web Server Gateway Interface（web服务器网关接口）
* 它是一种规范，它是web服务器和web应用程序之间的接口
* 它的作用就像是桥梁，连接在web服务器和web应用框架之间
* 没有官方的实现，更像一个协议。只要遵照这些协议，WSGI应用\(Application\)都可以在任何服务器\(Server\)上运行

**uwsgi**：是一种传输协议，用于定义传输信息的类型。常用于在uWSGI服务器与其他网络服务器的数据通信

**uWSGI**：是实现了uwsgi协议WSGI的web服务器。

## 阿里云服务器

* 选择云服务器:阿里云服务器 [https://www.aliyun.com](https://www.aliyun.com)
* 购买服务器:在首页最底下有一个免费使用的优惠购买：最便宜的套餐为9.9元，送一个入门级别的云服务器ECS和其他的一些服务器
* 购买后,再次进入首页最底下,点击免费获取 [https://free.aliyun.com/](https://free.aliyun.com/)
  ![免费获取1](/assets/free_get1.png)
* 进入如下图所示的界面,点击第一项云服务器ECS的立即开通\(由于本人已经创建,故:没有显示立即开通,而是前往控制台\)
  ![免费获取2](/assets/free_get2.png)
  ![创建服务器](/assets/server_create.png)
* 创建服务器选择ubuntu16.04 64位的操作系统
  ![](/assets/QQ20171031-150105@2x.png)
* 进入控制台,查看实例创建情况
  ![控制台](/assets/instance.png)
  
* 给安全组配置规则，添加5000端口

![安全组](/assets/安全组.png)
![配置规则](/assets/配置规则.png)
![](/assets/添加安全组规则.png)
* 利用命令行进行远程服务器登录

```bash
ssh 用户名@ip地址
```

## 登陆后的相关软件安装

### 先更新apt软件源

```
sudo apt-get update
```

### python和pip

这两个环境是ubuntu16.04自带的

### uwsgi安装

* uwsgi是一个能够运行flask项目的高性能web服务器，需要先安装两个依赖

```
apt-get install build-essential python-dev
```

* 然后进行uwsgi的安装

```
pip install uwsgi
```

### nginx安装

```
apt-get install nginx
```

### mysql的安装:

```
apt-get install mysql-server
apt-get install libmysqlclient-dev
```

### 虚拟环境的安装

* virtualenv和virtualenvwrapper的安装：

```
pip install virtualenv
pip install virtualenvwrapper
```

* 使得安装的virtualenvwrapper生效，编辑~/.bashrc文件，内容如下:

```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/workspace
source /usr/local/bin/virtualenvwrapper.sh
```

* 使编辑后的文件生效

```
source ~/.bashrc
```

## hello world程序的部署

* 利用pycharm创建python项目
* 创建config.ini文件作为uwsgi的初始化配置文件

```ini
#需要声明uwsgi使得uwsgi能够识别当前文件
[uwsgi]
master = true
# 使用 nginx 配合连接时使用
# socket = :5000
# 直接做web服务器使用
http = :5000
# 设定进程数
processes = 4
# 设定线程数       
threads = 2
# 指定运行的文件
wsgi-file = app.py
#指定运行的项目的目录[自已项目在哪个目录就用哪个目录]
chdir = /root/home/hello_world
# 指定运行的实例
callable = app
# 指定uwsgi服务器的缓冲大小
buffer-size = 32768
# 在虚拟环境中运行需要指定python目录
pythonpath = /root/.virtualenvs/Flask_test/lib/python2.7/site-packages
# 设置进程id文件
pidfile = uwsgi.pid
# 以守护的形式运行，设置log输出位置
daemonize = uwsgi.log
```

* 利用scp命令将整个项目上传到远程服务器中

```
scp -r 本地目录 用户名@ip地址:远程目录

scp -r /home/python/Desktop/hello_world/ root@39.106.21.198:/root/home
```

* 通过指令运行uwsgi.ini服务器

```
uwsgi --ini config.ini
```

- 查看

```
ps ajx|grep uwsgi
```

- 停止

```
uwsgi --stop uwsgi.pid
```


> 其中  
> --ini config.ini 表示指定运行的配置文件  
> -d uwsgi.log 表示uwsgi在后台运行,运行过程中产生的日志会存储在uwsgi.log中

* 配置nginx服务器

编辑文件:/etc/nginx/sites-available/default

修改为如下内容:

```
server {
    listen 80 default_server;

    server_name 59.110.240.237;    

    location / {
        include uwsgi_params;
        uwsgi_pass 59.110.240.237:5000;
        uwsgi_read_timeout 100;
    }
}
```

将server中原有的,上述配置中不能存在的内容注释或删除掉

* 启动和停止nginx服务器

```
/etc/init.d/nginx start #启动
/etc/init.d/nginx stop  #停止
```

## 本地项目的远程部署

* 3,创建虚拟环境

```
mkvirtualenv 虚拟环境名称
```

* 4,在虚拟环境中安装项目所需要的依赖

```
pip install -r 依赖文件(requirements.txt)
```

* 5,通过scp命令将整个项目上传到远程服务器

```
scp -r 本地目录 用户名@ip地址:远程目录
```

* 6,创建config.ini文件,配置和之前一致,但要加入一个虚拟环境的配置

```
pythonpath = /root/.virtualenvs/flask_test/lib/python2.7/site-packages #表示指定虚拟环境目录,使用虚拟环境中安装的扩展
```

* 7,运行uwsgi和之前操作一致,但要修改项目目录

```python
uwsgi --ini config.ini
```

* 8,运行nginx和之前操作一致,但要修改项目目录

```python
/etc/init.d/nginx start
```



