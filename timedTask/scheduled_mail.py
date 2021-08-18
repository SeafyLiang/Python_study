#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   scheduled_mail.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/8/18 19:40   SeafyLiang   1.0       发邮件，带附件发送
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

if __name__ == '__main__':
    fromaddr = 'xxx@163.com'
    password = '授权码'
    toaddrs = ['<xxx@qq.com>', '<xxx@qq.com>']

    content = '这里是content'
    textApart = MIMEText(content)

    imageFile = '/Users/seafyliang/Downloads/myplot.jpg'
    imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
    imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)
    #
    # pdfFile = '算法设计与分析基础第3版PDF.pdf'
    # pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
    # pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)
    #
    # zipFile = '算法设计与分析基础第3版PDF.zip'
    # zipApart = MIMEApplication(open(zipFile, 'rb').read())
    # zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

    htmlFile = 'scatter_visualmap_color.html'
    htmlApart = MIMEApplication(open(htmlFile, 'rb').read())
    htmlApart.add_header('Content-Disposition', 'attachment', filename=htmlFile)

    m = MIMEMultipart()
    m.attach(textApart)
    m.attach(imageApart)
    # m.attach(pdfApart)
    # m.attach(zipApart)
    m.attach(htmlApart)
    m['Subject'] = '邮件标题'
    m['From'] = fromaddr


    try:
        server = smtplib.SMTP('smtp.163.com')
        server.login(fromaddr, password)
        for toaddr in toaddrs:
            m['To'] = toaddr
            server.sendmail(fromaddr, toaddr, m.as_string())
        print('success')
        server.quit()
    except smtplib.SMTPException as e:
        print('error:', e)  # 打印错误
