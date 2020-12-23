# _*_ coding: utf-8 _*_
# @Time : 2020/11/25 16:44 
# @Author : SeafyLiang 
# @Version：V 0.1
# @File : scriptStudy.py
# @desc : python控制终端脚本学习


import os


if __name__ == '__main__':
    # r = os.popen('docker run -it microsoftlocation:0.1 /bin/bash') #执行该命令
    # info = r.readlines()  # 读取命令行的输出到一个list
    # for line in info:  # 按行遍历
    #     line = line.strip('\r\n')
    #     print("line:" + line)
    # r = os.popen('python __main__.py') #执行该命令
    # info = r.readlines()  # 读取命令行的输出到一个list
    # for line in info:  # 按行遍历
    #     line = line.strip('\r\n')
    #     print("line:" + line)

    # os.chdir(path) 切换目录
    # os.chdir('/Users/seafyliang/DEV/Code_projects/docker_projects/microserviceLocation')
    # os.popen('cd /Users/seafyliang/DEV/Code_projects/docker_projects/microserviceLocation')
    # r = os.popen('ls') #执行该命令
    # info = r.readlines()  # 读取命令行的输出到一个list
    # for line in info:  # 按行遍历
    #     line = line.strip('\r\n')
    #     print("line:" + line)
    # os.system('python3 __main__.py --pre_dir /Users/seafyliang/DEV/Code_projects/hyetec_Algorithm/inputData'
    #           '/testInputData/microserviceLocation/preData/ --output_dir '
    #           '/Users/seafyliang/DEV/Code_projects/hyetec_Algorithm/outputData/transitionData/microserviceLocation/ '
    #           '--faultData_dir /Users/seafyliang/DEV/Code_projects/hyetec_Algorithm/inputData/testInputData'
    #           '/microserviceLocation/dataDescribe/0故障说明.xlsx --out_file_path '
    #           '/Users/seafyliang/DEV/Code_projects/hyetec_Algorithm/outputData/resultData/microserviceLocation/')
    print("test")
    # os.system('docker run -it microsoftlocation:0.1 /bin/bash ;  python __init__.py')
