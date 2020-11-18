from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
import pymysql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)


# # 配置数据库地址
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql"//root:root@127.0.0.1/ry'
# # 跟踪修改，开启会消耗性能  不建议开启
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# # SQLAlchemy教程：https://www.jianshu.com/p/637ede0939d1
# db = SQLAlchemy(app)


@app.route("/")
def index():
    df = getData()
    projectList, projectTimeList = calWorkTime(df)
    return render_template("echarts.html", projectList=projectList, projectTimeList=projectTimeList)


def getData():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "moa_final")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 查询数据sql
    sql = 'SELECT zb.GSZBRQN AS 年, zb.GSZBRQZ AS 周, mx.GSMXGS AS 工时, zyxm.XMMC AS 项目名称, rcgz.rcgzmc AS 项目类型, zb.KSRQ AS 开始日期, zb.JSRQ AS 结束日期  FROM gszb zb LEFT JOIN gsmxb mx ON zb.GSZBID = mx.GSZBID LEFT JOIN zyxmb zyxm ON mx.GSMXXMID = zyxm.XMID LEFT JOIN rcgzb rcgz ON mx.GSMXXMID = rcgz.rcgzid  WHERE zb.GSZBYGID = 4700'
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    # 使用fetchall() 方法获取所有返回数据
    results = cursor.fetchall()

    # 关闭数据库连接
    db.close()

    # 预览结果
    # results

    # 执行结果转化为dataframe
    df = pd.DataFrame(list(results),
                      columns=['year', 'week', 'workTime', 'projectName', 'workTimeType', 'weekStartTime',
                               'weekEndTime'])
    return df

def calWorkTime(df):
    # # 删除空值
    # df.dropna(how='all')
    # 合并两列 生成workType
    df['workType'] = df['projectName'].map(str) + df['workTimeType'].map(str)

    # 删除None值
    workTypeSeries = df['workType']
    for index in range(len(workTypeSeries)):
        if workTypeSeries[index].startswith('None'):
            workTypeSeries[index] = workTypeSeries[index][4:]
        if workTypeSeries[index].endswith('None'):
            workTypeSeries[index] = workTypeSeries[index][:-4]

    # df列替换，删除旧的两列
    df['workType'] = workTypeSeries
    df.drop("projectName", axis=1, inplace=True)
    df.drop("workTimeType", axis=1, inplace=True)
    # df

    projectList = []
    projectTimeList = []
    for index, data in df.groupby(by='workType'):
        # 对不同项目类型进行分组显示
        print(index)
        #     print(data)
        # 'workTime'列类型转换
        data = data.astype({'workTime': 'float'})
        print("合计：" + str(data['workTime'].sum()))
        projectList.append(str(index))
        projectTimeList.append(data['workTime'].sum())
        print('\n')
    return projectList, projectTimeList


if __name__ == '__main__':
    app.run(debug=True)