from flask import Flask, render_template, request

# hello world
# 创建应用程序
# web应用程序
app = Flask(__name__)  # __name__ 表示对应程序名称

# # 写一个函数来处理浏览器发送过来的请求
# # 路由，通过浏览器访问过来的请求交给谁处理
# @app.route("/")  # 当访问到127.0.0.1:5000/
# def index():
#     # 这里处理业务逻辑
#     return "hello flask"  # 返回的数据 -> 响应


# # 模板 -> html
# @app.route("/")
# def index():
#     return render_template("helloFlask.html")  # 此时会自动找templates文件夹里面的h5文件

# # 把变量发送到页面
# @app.route("/")
# def index():
#     testList = ['aaa', 'bbb', 'ccc']  # 定义一个数组变量
#     return render_template("helloFlask.html", prop=testList)  # 页面后加变量参数，参数名自定


# 案例-从页面接收数据：登录验证
@app.route("/")
def index():
    return render_template("login.html")


# @app.route("/login")  # 默认处理get请求
@app.route("/login", methods=['POST'])
def login():
    # 接收用户名和密码
    username = request.form.get("username")
    password = request.form.get("password")
    # request.args.get()  # url传参
    if "root" == username and "root" == password:
        return "登录成功"
    else:
        return "登录失败"


# 此方法必须写在最下面
if __name__ == '__main__':  # 固定的写法，程序的入口
    # app.run(debug=True)  # debug=True，不用重启服务器
    app.run()  # 启动应用程序 -> 启动一个flask项目
    # def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):


# requirements 文件
# 存储环境包和版本号
# 1.导出环境依赖
# pip freeze > fileName.txt
# 2.导入环境依赖 -r 循环遍历
# pip install -r fileName.txt

