#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   my_fastApi.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/2/7 15:51   SeafyLiang   1.0          fastApi_demo，接口描述，实体类传参
"""
from typing import Optional
from typing import List
from fastapi import FastAPI, Path
from pydantic import BaseModel, Field
import pickle
import pandas as pd
import json

"""

fastApi==0.70.0

uvicorn my_fastApi:app 命令含义如下:
● main：my_fastApi.py 文件（一个 Python「模块」）。
● app：在 my_fastApi.py 文件中通过 app = FastAPI() 创建的对象。
● --reload：让服务器在更新代码后重新启动。仅在开发时使用该选项。

启动成功后，访问url就是访问接口
http://127.0.0.1:8000/【url】：接口访问
http://127.0.0.1:8000/docs：交互式API文档
http://127.0.0.1:8000/redoc：可选的API文档
http://127.0.0.1:8000/openapi.json ：openAPI，所有api的json描述
"""


# 接口文档标题及描述
app = FastAPI(title='算法服务', description='xxx预测算法')


# 实体类，用于传参
class testItem(BaseModel):
    id: str = Field(title="id，唯一标识")
    tmstmp: int = Field(title="时间戳（13位）")


# 接口定义 get
@app.get("/", summary='测试接口1注释', description='接口1描述', tags=['测试'])
async def root():
    return {"message": "Hello fastApi"}


# 接口定义 post
@app.post("/charge/predict", summary='xxx预测算法', description='通过id, tmstmp预测xxx', tags=['算法'])
async def time_predict(charge_item: List[testItem]):
    # list可传入数组，实体类对象列表
    # list 拼接成 json
    json_arr = '['
    for i in range(len(charge_item)):
        if i < len(charge_item) - 1:
            json_arr = json_arr + str(charge_item[i].json()) + ', '
        else:
            json_arr = json_arr + str(charge_item[i].json())
    json_arr = json_arr + ']'
    print(json_arr)

    # 解析json成pandas.df对象
    df = pd.read_json(json_arr)
    print(df)
    # # 加载模型
    # xgb_model = pickle.load(open("models/XGBRegressor.pickle.dat", "rb"))
    # column_list = ['id', 'tmstmp']
    # # 预测结果
    # result = xgb_model.predict(df[column_list])
    result = str(df)
    return str(result)
