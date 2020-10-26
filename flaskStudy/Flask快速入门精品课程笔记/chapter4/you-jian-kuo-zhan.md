# 邮件扩展
在开发过程中，很多应用程序都需要通过邮件提醒用户，Flask的扩展包Flask-Mail通过包装了Python内置的smtplib包，可以用在Flask程序中发送邮件。

Flask-Mail连接到简单邮件协议（Simple Mail Transfer Protocol,SMTP）服务器，并把邮件交给服务器发送。
###设置邮箱授权码
![设置授权码](/assets/identify_code.png)

如下示例，通过开启QQ邮箱SMTP服务设置，发送邮件。

```python
#coding:utf-8
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# 配置邮件：服务器／端口／安全套接字层／邮箱名／授权码
app.config['MAIL_SERVER'] = "smtp.126.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "huidongpeng@126.com"
app.config['MAIL_PASSWORD'] = "heima666"
app.config['MAIL_DEFAULT_SENDER'] = 'FlaskAdmin<huidongpeng@126.com>'

mail = Mail(app)


@app.route('/')
def hello_world():
    return '<a href="/send_mail">发送邮件</a>'


@app.route('/send_mail')
def send_mail():
    msg = Message('这是邮件的主题', recipients=['huidongpeng@126.com'],body='This is flask mail')
    mail.send(msg)
    return '已发送邮件'


if __name__ == '__main__':
    app.run(debug=True)
```