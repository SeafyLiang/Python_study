# 拉取基础镜像
FROM python:3.8.2

# 维护者信息
MAINTAINER SeafyLiang  SeafyLiang@icloud.com

# 把当前所有文件拷贝到容器的/code文件夹里，并根据requirements.txt安装python依赖包
RUN mkdir /code \
&& apt-get update -y \
&& apt-get install -y libsm6 \
&& pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY . /code
RUN pip install -r /code/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# 设置code文件夹是工作目录
WORKDIR /code

# 安装支持
RUN pip install -r requirements.txt

CMD ["python", "/code/argparseTest.py"]

