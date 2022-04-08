#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   file_server.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/4/8 15:09   SeafyLiang   1.0        fastAPI实现文件上传下载服务
"""
from typing import List
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
import uvicorn
import pandas as pd
from fastapi.responses import FileResponse, StreamingResponse
import io

app = FastAPI()


# 第一种读取文件方法，读取二进制文件
@app.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    # 保存文件名
    with open('保存文件名字', 'wb') as f:
        f.write(files[0])
    return {"file_sizes": [len(file) for file in files]}


# 第二种读取文件的方法，会保存文件名，文件本身等信息
@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...), token: str = Form(...), newTime: int = Form(...)):
    print(token)
    print(newTime)
    # 保存文件
    data = await files[0].read()
    with open(files[0].filename, 'wb') as f:
        f.write(data)
    return {"filenames": [file.filename for file in files], "token": token, "newTime": newTime}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


file_path = "test.zip"


# 假设有个pandas DataFrame文件文件需要保存
@app.get("/from_data/")
def main():
    df = pd.DataFrame([1, 2, 3])
    stream = io.StringIO()
    df.to_csv(stream, index=False)
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    return response


# 假设我们预定了文件的路径
@app.get("/from_path/")
def main():
    return FileResponse(path=file_path, filename=file_path, media_type='py')


if __name__ == '__main__':
    uvicorn.run(app=app, port=8900)
