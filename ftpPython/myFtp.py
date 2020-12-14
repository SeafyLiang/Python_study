# coding=utf-8
# @Time : 2020/11/27 14:14 
# @Author : SeafyLiang 
# @Version：V 0.1
# @File : myFtp.py
# @desc :

import parser
from ftplib import FTP
import os
import sys
import time
import socket
import datetime
import errno
from dateutil import parser


class MyFTP:
    """
        ftp自动下载、自动上传脚本，可以递归目录操作
    """

    def __init__(self, host, port):
        """ 初始化 FTP 客户端
        参数:
                 host:ip地址

                 port:端口号
        """
        # print("__init__()---> host = %s ,port = %s" % (host, port))

        self.host = host
        self.port = port
        self.ftp = FTP()
        # 重新设置下编码方式
        self.ftp.encoding = 'gbk'
        self.log_file = open("log.txt", "a")
        self.file_list = []

    def login(self, username, password):
        """ 初始化 FTP 客户端
            参数:
                  username: uftp2

                 password: uftp2
            """
        try:
            timeout = 600
            socket.setdefaulttimeout(timeout)
            # 0主动模式 1 #被动模式
            self.ftp.set_pasv(True)
            # 打开调试级别2，显示详细信息
            # self.ftp.set_debuglevel(2)

            self.debug_print('开始尝试连接到 %s' % self.host)
            self.ftp.connect(self.host, self.port)
            self.debug_print('成功连接到 %s' % self.host)

            self.debug_print('开始尝试登录到 %s' % self.host)
            self.ftp.login(username, password)
            self.debug_print('成功登录到 %s' % self.host)

            self.debug_print(self.ftp.welcome)
        except Exception as err:
            self.deal_error("FTP 连接或登录失败 ，错误描述为：%s" % err)
            pass

    def formatSize(self, bytes):
        """
         # 字节bytes转化kb\m\g
        :return: str
        """
        try:
            bytes = float(bytes)
            kb = bytes / 1024
        except:
            print("传入的字节格式不对")
            return "Error"

        if kb >= 1024:
            M = kb / 1024
            if M >= 1024:
                G = M / 1024
                return "%fG" % (G)
            else:
                return "%fM" % (M)
        else:
            return "%fkb" % (kb)

    def is_same_size(self, local_file, remote_file):
        """判断远程文件和本地文件大小是否一致

           参数:
             local_file: 本地文件

             remote_file: 远程文件
        """
        try:
            ssize = self.ftp.size(remote_file)
            remote_file_size = self.formatSize(ssize)
        except Exception as err:
            # self.debug_print("is_same_size() 错误描述为：%s" % err)
            remote_file_size = -1

        try:
            local_file_size = self.formatSize(os.path.getsize(local_file))
        except Exception as err:
            # self.debug_print("is_same_size() 错误描述为：%s" % err)
            local_file_size = -1

        self.debug_print('local_file_size:%s  , remote_file_size:%s' % (local_file_size, remote_file_size))
        if remote_file_size == local_file_size:
            return 1
        else:
            return 0

    def download_file(self, local_file, remote_file):
        """从ftp下载文件
            参数:
                local_file: 本地文件

                remote_file: 远程文件
        """
        self.debug_print("download_file()---> local_path = %s ,remote_path = %s" % (local_file, remote_file))

        if self.is_same_size(local_file, remote_file):
            self.debug_print('%s 文件大小相同，无需下载' % local_file)
            return
        else:
            try:
                self.debug_print('>>>>>>>>>>>>下载文件 %s 到 %s ... ...' % (remote_file, local_file))
                # buf_size = 1024
                file_handler = open(local_file, 'wb')
                self.ftp.retrbinary('RETR %s' % remote_file, file_handler.write)
                file_handler.close()
                self.debug_print('>>>>>>>>>>>>下载完成  ... ...')
            except Exception as err:
                self.debug_print('下载文件出错，出现异常：%s ' % err)
                return

    def download_file_tree(self, local_path, remote_path):
        """从远程目录下载多个文件到本地目录
                       参数:
                         local_path: 本地路径

                         remote_path: 远程路径
                """
        print("download_file_tree()--->  local_path = %s ,remote_path = %s" % (local_path, remote_path))
        try:
            self.ftp.cwd(remote_path)
        except Exception as err:
            self.debug_print('远程目录%s不存在，继续...' % remote_path + " ,具体错误描述为：%s" % err)
            return

        if not os.path.isdir(local_path):
            self.debug_print('本地目录%s不存在，先创建本地目录' % local_path)
            os.makedirs(local_path)

        self.debug_print('切换至目录: %s' % self.ftp.pwd())

        self.file_list = []
        # 方法回调
        self.ftp.dir(self.get_file_list)

        remote_names = self.file_list
        self.debug_print('远程目录 列表: %s' % remote_names)
        for item in remote_names:
            file_type = item[0]
            file_name = item[1]
            local = os.path.join(local_path, file_name)
            if file_type == 'd':
                print("download_file_tree()---> 下载目录： %s" % file_name)
                self.download_file_tree(local, file_name)
            elif file_type == '-':
                print("download_file()---> 下载文件： %s" % file_name)
                self.download_file(local, file_name)
            self.ftp.cwd("..")
            self.debug_print('返回上层目录 %s' % self.ftp.pwd())
        return True

    def upload_file(self, local_file, remote_file):
        """从本地上传文件到ftp

           参数:
             local_path: 本地文件

             remote_path: 远程文件
        """
        if not os.path.isfile(local_file):
            self.debug_print('%s 不存在' % local_file)
            return

        if self.is_same_size(local_file, remote_file):
            self.debug_print('跳过相等的文件: %s' % local_file)
            return

        buf_size = 2048
        file_handler = open(local_file, 'rb')
        try:
            self.ftp.storbinary('STOR %s' % remote_file, file_handler, buf_size)
            file_handler.close()
        except IOError as e:
            if e.errno == errno.EPIPE:
                print(e.errno)
        self.debug_print('上传: %s' % local_file + "成功!")

    def upload_file_tree(self, local_path, remote_path):
        """从本地上传目录下多个文件到ftp
           参数:

             local_path: 本地路径

             remote_path: 远程路径
        """
        if not os.path.isdir(local_path):
            self.debug_print('本地目录 %s 不存在' % local_path)
            return

        self.ftp.cwd(remote_path)
        self.debug_print('切换至远程目录: %s' % self.ftp.pwd())

        local_name_list = os.listdir(local_path)
        for local_name in local_name_list:
            src = os.path.join(local_path, local_name)
            if os.path.isdir(src):
                try:
                    self.ftp.mkd(local_name)
                except Exception as err:
                    self.debug_print("目录已存在 %s ,具体错误描述为：%s" % (local_name, err))
                self.debug_print("upload_file_tree()---> 上传目录： %s" % local_name)
                self.upload_file_tree(src, local_name)
            else:
                self.debug_print("upload_file_tree()---> 上传文件： %s" % local_name)
                self.upload_file(src, local_name)
        self.ftp.cwd("..")

    def close(self):
        """ 退出ftp
        """
        self.debug_print("close()---> FTP退出")
        self.ftp.quit()
        self.log_file.close()

    def debug_print(self, s):
        """ 打印日志
        """
        self.write_log(s)

    def deal_error(self, e):
        """ 处理错误异常
            参数：
                e：异常
        """
        log_str = '发生错误: %s' % e
        self.write_log(log_str)
        sys.exit()

    def write_log(self, log_str):
        """ 记录日志
            参数：
                log_str：日志
        """
        time_now = time.localtime()
        date_now = time.strftime('%Y-%m-%d %H:%M:%S', time_now)
        format_log_str = "%s ---> %s \n " % (date_now, log_str)
        print(format_log_str)
        self.log_file.write(format_log_str)

    def get_file_list(self, line):
        """ 获取文件列表
            参数：
                line：
        """
        file_arr = self.get_file_name(line)
        # 去除  . 和  ..
        if file_arr[1] not in ['.', '..']:
            self.file_list.append(file_arr)

    def get_file_name(self, line):
        """ 获取文件名
            参数：
                line：
        """
        pos = line.rfind(':')
        while (line[pos] != ' '):
            pos += 1
        while (line[pos] == ' '):
            pos += 1
        file_arr = [line[0], line[pos:]]
        return file_arr

    def get_upload_file_exist(self):
        path_current = "/Users/seafyliang/DEV/Code_projects/Python_projects/2020学习/2020Study/ftpPython"
        files = os.listdir(path_current)  # 得到文件夹下的所有文件名称
        for file in files:
            if file.__contains__("py"):
                path_file = path_current + "/" + file
                return path_file, file
            if file.__contains__("linux"):
                path_file = path_current + "/" + file
                file_create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getctime(path_file)))

                m2_tmp = str(datetime.datetime.now() + datetime.timedelta(minutes=-2000))
                index = m2_tmp.find('.')  # 第一次出现的位置
                m2 = m2_tmp[:index]

                if file_create_time >= m2:
                    print("%s 创建时间: %s" % (file, file_create_time))
                    return path_file, file

        print(str(datetime.datetime.now()) + " 没有新文件产生")
        return "", ""

    def get_file_form_ftp(self):
        self.ftp.cwd("/package")  # 设置FTP当前操作的路径
        files = self.ftp.nlst()
        for file in files:
            if file.__contains__("linux"):
                timestamp = self.ftp.voidcmd("MDTM /package/" + file)[4:].strip()
                time = parser.parse(timestamp)

                m2_tmp = str(datetime.datetime.now() + datetime.timedelta(minutes=-3))
                index = m2_tmp.find('.')  # 第一次出现的位置
                m2 = m2_tmp[:index]

                print("%s 修改时间: %s" % (file, time))
                if str(time) >= m2:
                    return file
        return ""


if __name__ == "__main__":
    my_ftp = MyFTP("10.211.55.3", 2121)
    my_ftp.login("ftpuser", "123456")

    # 上传
    while True:
        path_file, file = my_ftp.get_upload_file_exist()
        if path_file:
            print(path_file)
            my_ftp.upload_file(path_file, "/upload" + file)
        time.sleep(120)  # 每2分钟轮询一次

    # 下载
    # while True:
    #     file = my_ftp.get_file_form_ftp()
    #     if file:
    #         # 下载单个文件
    #         my_ftp.download_file("/home/qboxserver/juncheng/" + file, "/package/" + file, )
    #         # os.system('bash update_pandora.sh ' + file)
    #     time.sleep(120)  # 每2分钟轮询一次
