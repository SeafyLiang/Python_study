pip list 可查看本地环境依赖

### Python加载外部依赖 .whl

1. [whl文件库](https://www.lfd.uci.edu/~gohlke/pythonlibs/)下载到.whl文件
2. 切到whl文件同级目录，使用命令 pip install xxx.whl



### python导出依赖成whl文件

1. 安装wheel库 pip install wheel

2. 生成whl文件 新建一个**requirement.txt**

   > requirement.txt中写入要下载的库的名字，
>
   > 多个库名需要换行

3. 切到 requirement.txt文件同级目录，使用命令 pip wheel -r requirement.txt



### 镜像库

清华：https://pypi.tuna.tsinghua.edu.cn/simple

阿里云：http://mirrors.aliyun.com/pypi/simple/

中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/

华中理工大学：http://pypi.hustunique.com/

山东理工大学：http://pypi.sdutlinux.org/ 

豆瓣：http://pypi.douban.com/simple/

note：新版ubuntu要求使用https源，要注意。

**例如：pip3 install -i https://pypi.doubanio.com/simple/ 包名**



### 一键导出环境依赖及安装环境依赖

```shell
# 导出环境中的所有第三方包
pip freeze > requirements.txt

# 从文件循环安装第三方包（-i 使用清华镜像源）
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```



### 离线下载和安装python环境依赖

```shell
# 下载离线包
pip download  -r requestments.txt  -d  ./pip_packages    
# 从当前环境的网络中下载requestments.txt中写的包，下载到当前目录下的pip_packages目录中，这时候你会发现，里面有很多依赖，还有一些whl文件
```

```shell
# 安装离线包
pip install --no-index --find-links=d:\packages -r requirements.txt 
# --find-links指定的是包文件的存放地址，-r指定的是txt文件的位置
```

