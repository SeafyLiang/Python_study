# _*_ coding: utf-8 _*_
# @Time : 2020/11/18 13:59 
# @Author : SeafyLiang 
# @Version：V 0.1
# @File : argparseTest.py
# @desc :

import argparse
import pandas as pd
import datetime

# 参数解析
def get_parser():
    print("start get_parser")
    parser_reader = argparse.ArgumentParser(description="测试参数解析")
    # parser_reader.add_argument("--input_dir", help="输入数据路径", required=True)
    # parser_reader.add_argument("--output_dir", help="输出数据路径", required=True)
    # parser_reader.add_argument("--faultDate", help="故障日期", required=True)
    # args_reader = parser_reader.parse_args()
    # if args_reader.input_dir:
    #     print("args_reader.input_dir：" + args_reader.input_dir)
    # if args_reader.output_dir:
    #     print("args_reader.output_dir：" + args_reader.output_dir)
    # if args_reader.faultDate:
    #     print("args_reader.faultDate：" + args_reader.faultDate)
    #     print(type(args_reader.faultDate))

    print("finish get_parser")
    return parser_reader


if __name__ == '__main__':
    print("start main")
    # parser = get_parser()
    # args = parser.parse_args()
    # input_dir = args.input_dir
    # output_dir = args.output_dir
    print("finish main")
    date = "2020/05/22"
    formatDate = datetime.datetime.strptime(date,"%Y/%m/%d")
    print(formatDate)
