# _*_ coding: utf-8 _*_
# @Time : 2020/11/25 11:21 
# @Author : SeafyLiang 
# @Version：V 0.1
# @File : ftpStudy.py
# @desc : ftp上传下载文件学习

import os
from ftplib import FTP


def ftp_connect(host, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(host, 2121)
    ftp.login(username, password)
    return ftp


# 从ftp服务器下载文件
def download_file(ftp, remotepath, localpath):
    print("开始下载文件%s……" % remotepath)
    bufsize = 100
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()
    print("下载文件%s成功" % remotepath)


# 从本地上传文件到ftp
def upload_file(ftp, remotepath, localpath):
    print("开始上传文件%s……" % localpath)
    bufsize = 100
    fp = open(localpath, 'rb')

    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()
    print("上传文件%s成功" % localpath)


if __name__ == "__main__":
    ftp = ftp_connect("192.168.10.1","LIZEYU","lietuty")
    print(ftp.getwelcome())  # 打印出欢迎信息
    # download_file(ftp, "filename.txt", "filenameDownload.txt")

    ftp.quit()  # 退出ftp


# FTP对象常用方法
#
# ftp.cwd(path)                    设置FTP当前操作的路径，同linux中的cd
#
# ftp.dir()                             显示目录下所有信息
#
# ftp.nlst()                            获取目录下的文件，显示的是文件名列表
#
# ftp.mkd(directory)             新建远程目录
#
# ftp.rmd(directory)              删除远程目录
#
# ftp.rename(old, new)         将远程文件old重命名为new
#
# ftp.delete(file_name)          删除远程文件
#
# ftp.storbinary(cmd, fp, bufsize)             上传文件，cmd是一个存储命令，可以为"STOR filename.txt"， fp为类文件对象（有read方法），bufsize设置缓冲大小
#
# ftp.retrbinary(cmd, callback, bufsize)              下载文件，cmd是一个获取命令，可以为"RETR filename.txt"， callback是一个回调函数，用于读取获取到的数据块
