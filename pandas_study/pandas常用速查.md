# pandas常用速查



### 引入依赖

```python
# 导入模块
import pymysql
import pandas as pd
import numpy as np
import time

# 数据库
from sqlalchemy import create_engine

# 可视化
import matplotlib.pyplot as plt
# 解决 plt 中文显示的问题 mymac
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# 设置显示中文 需要先安装字体 aistudio
plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
import seaborn as sns
# notebook渲染图片
%matplotlib inline
import pyecharts

# 忽略版本问题
import warnings
warnings.filterwarnings("ignore")  
```

```sh
# 下载中文字体
!wget https://mydueros.cdn.bcebos.com/font/simhei.ttf 
# 将字体文件复制到 matplotlib'字体路径
!cp simhei.ttf /opt/conda/envs/python35-paddle120-env/Lib/python3,7/site-packages/matplotib/mpl-data/fonts.

# 一般只需要将字体文件复制到系统字体田录下即可,但是在 studio上该路径没有写权限,所以此方法不能用 
# !cp simhei. ttf /usr/share/fonts/

# 创建系统字体文件路径
!mkdir .fonts
# 复制文件到该路径
!cp simhei.ttf .fonts/
!rm -rf .cache/matplotlib
```

![image-20210308164256130](https://i.loli.net/2021/03/08/oUIZVcMzwqBpE8C.png)

#### 算法相关依赖

```python
# 数据归一化
from sklearn.preprocessing import MinMaxScaler

# kmeans聚类
from sklearn.cluster import KMeans
# DBSCAN聚类
from sklearn.cluster import DBSCAN
# 线性回归算法
from sklearn.linear_model import LinearRegression
# 逻辑回归算法
from sklearn.linear_model import LogisticRegression
# 高斯贝叶斯
from sklearn.naive_bayes import GaussianNB
# 划分训练/测试集
from sklearn.model_selection import train_test_split
# 准确度报告
from sklearn import metrics
# 矩阵报告和均方误差
from sklearn.metrics import classification_report, mean_squared_error
```



### 获取数据

```python
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/ry?charset=utf8')

# 查询插入后相关表名及行数
result_query_sql = "use information_schema;"
engine.execute(result_query_sql)
result_query_sql = "SELECT table_name,table_rows FROM tables WHERE TABLE_NAME LIKE 'log%%' order by table_rows desc;"
df_result = pd.read_sql(result_query_sql, engine)
```

![image-20210309140418528](https://i.loli.net/2021/03/09/t6GIUMvRo7fFXJP.png)



### 生成df

```python
# list转df
df_result = pd.DataFrame(pred,columns=['pred'])
df_result['actual'] = test_target
df_result

# df取子df
df_new = df_old[['col1','col2']]

# dict生成df
df_test = pd.DataFrame({'A':[0.587221, 0.135673, 0.135673, 0.135673, 0.135673], 
                        'B':['a', 'b', 'c', 'd', 'e'],
                        'C':[1, 2, 3, 4, 5]})

# 指定列名
data = pd.DataFrame(dataset.data, columns=dataset.feature_names)

# 使用numpy生成20个指定分布(如标准正态分布)的数
tem = np.random.normal(0, 1, 20)
df3 = pd.DataFrame(tem)

# 生成一个和df长度相同的随机数dataframe
df1 = pd.DataFrame(pd.Series(np.random.randint(1, 10, 135)))
```



### 重命名列

```python
# 重命名列
data_scaled = data_scaled.rename(columns={'本体油位': 'OILLV'})
```



### 增加列

```python
# df2df
df_jj2yyb['r_time'] = pd.to_datetime(df_jj2yyb['cTime'])

# 新增一列根据salary将数据分为3组
bins = [0,5000, 20000, 50000]
group_names = ['低', '中', '高']
df['categories'] = pd.cut(df['salary'], bins, labels=group_names)
```



### 缺失值处理

```python
# 检查数据中是否含有任何缺失值
df.isnull().values.any()

# 查看每列数据缺失值情况
df.isnull().sum()

# 提取某列含有空值的行
df[df['日期'].isnull()]

# 输出每列缺失值具体行数
for i in df.columns:
    if df[i].count() != len(df):
        row = df[i][df[i].isnull().values].index.tolist()
        print('列名："{}", 第{}行位置有缺失值'.format(i,row))

# 众数填充
heart_df['Thal'].fillna(heart_df['Thal'].mode(dropna=True)[0], inplace=True)

# 连续值列的空值用平均值填充
dfcolumns = heart_df_encoded.columns.values.tolist()
for item in dfcolumns:
    if heart_df_encoded[item].dtype == 'float':
       heart_df_encoded[item].fillna(heart_df_encoded[item].median(), inplace=True)
```



### 独热编码

```python
df_encoded = pd.get_dummies(df_data)
```



### 替换值

```python
# 按列值替换
num_encode = {
    'AHD': {'No':0, "Yes":1},
}
heart_df.replace(num_encode,inplace=True)
```



### 删除列

```python
df_jj2.drop(['coll_time', 'polar', 'conn_type', 'phase', 'id', 'Unnamed: 0'],axis=1,inplace=True)


```



### 数据筛选

```python
# 取第33行数据
df.iloc[32]

# 某列以xxx字符串开头
df_jj2 = df_512.loc[df_512["transformer"].str.startswith('JJ2')]

df_jj2yya = df_jj2.loc[df_jj2["变压器编号"]=='JJ2YYA']

# 提取第一列中不在第二列出现的数字
df['col1'][~df['col1'].isin(df['col2'])]

# 查找两列值相等的行号
np.where(df.secondType == df.thirdType)

# 包含字符串
results = df['grammer'].str.contains("Python")

# 提取列名
df.columns

# 查看某列唯一值（种类）
df['education'].nunique()

# 删除重复数据
df.drop_duplicates(inplace=True)

# 某列等于某值
df[df.col_name==0.587221]
# df.col_name==0.587221 各行判断结果返回值(True/False)

# 查看某列唯一值及计数
df_jj2["变压器编号"].value_counts()

# 时间段筛选
df_jj2yyb_0501_0701 = df_jj2yyb[(df_jj2yyb['r_time'] >=pd.to_datetime('20200501')) & (df_jj2yyb['r_time'] <= pd.to_datetime('20200701'))]

# 数值筛选
df[(df['popularity'] > 3) & (df['popularity'] < 7)]

# 某列字符串截取
df['Time'].str[0:8]

# 随机取num行
ins_1 = df.sample(n=num)

# 数据去重
df.drop_duplicates(['grammer'])

# 按某列排序(降序)
df.sort_values("popularity",inplace=True, ascending=False)

# 取某列最大值所在行
df[df['popularity'] == df['popularity'].max()]

# 取某列最大num行
df.nlargest(num,'col_name')
# 最大num列画横向柱形图
df.nlargest(10).plot(kind='barh')
```

![image-20210304141053328](https://i.loli.net/2021/03/04/IXq7ev3gtxj4Nl8.png)



### 差值计算

```python
# axis=0或index表示上下移动， periods表示移动的次数，为正时向下移，为负时向上移动。
print(df.diff( periods=1, axis=‘index‘))
print(df.diff( periods=-1, axis=0))
# axis=1或columns表示左右移动，periods表示移动的次数，为正时向右移，为负时向左移动。
print(df.diff( periods=1, axis=‘columns‘))
print(df.diff( periods=-1, axis=1))

# 变化率计算
data['收盘价(元)'].pct_change()

# 以5个数据作为一个数据滑动窗口，在这个5个数据上取均值
df['收盘价(元)'].rolling(5).mean()
```



### 数据修改

```python
# 删除最后一行
df = df.drop(labels=df.shape[0]-1)

# 添加一行数据['Perl',6.6]
row = {'grammer':'Perl','popularity':6.6}
df = df.append(row,ignore_index=True)

# 某列小数转百分数
df.style.format({'data': '{0:.2%}'.format})

# 反转行
df.iloc[::-1, :]

# 以两列制作数据透视
pd.pivot_table(df,values=["salary","score"],index="positionId")

# 同时对两列进行计算
df[["salary","score"]].agg([np.sum,np.mean,np.min])

# 对不同列执行不同的计算
df.agg({"salary":np.sum,"score":np.mean})
```



### 时间格式转换

```python
# 时间戳转时间字符串
df_jj2['cTime'] =df_jj2['coll_time'].apply(lambda x: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(x)))

# 时间字符串转时间格式
df_jj2yyb['r_time'] = pd.to_datetime(df_jj2yyb['cTime'])

# 时间格式转时间戳
dtime = pd.to_datetime(df_jj2yyb['r_time'])
v = (dtime.values - np.datetime64('1970-01-01T08:00:00Z')) / np.timedelta64(1, 'ms')
df_jj2yyb['timestamp'] = v
```



### 设置索引列

```python
df_jj2yyb_small_noise = df_jj2yyb_small_noise.set_index('timestamp')
```



### 折线图

```python
fig, ax = plt.subplots()
df.plot(legend=True, ax=ax)
plt.legend(loc=1)
plt.show()
```

![image-20210304135130976](https://i.loli.net/2021/03/04/CYLDitEmfFjcZ5q.png)

```python
plt.figure(figsize=(20, 6))
plt.plot(max_iter_list, accuracy, color='red', marker='o',
         markersize=10)
plt.title('Accuracy Vs max_iter Value')
plt.xlabel('max_iter Value')
plt.ylabel('Accuracy')
```

![image-20210304140005204](https://i.loli.net/2021/03/04/9c4hNqpi7udzsRS.png)



### 散点图

```python
plt.scatter(df[:, 0], df[:, 1], c="red", marker='o', label='lable0')   
plt.xlabel('x')  
plt.ylabel('y')  
plt.legend(loc=2)  
plt.show()  
```

![image-20210304135235498](https://i.loli.net/2021/03/04/DSXJg7681sMGAlQ.png)



### 柱形图

```python
df = pd.Series(tree.feature_importances_, index=data.columns)
# 取某列最大Num行画横向柱形图
df.nlargest(10).plot(kind='barh')
```

![image-20210304141222188](https://i.loli.net/2021/03/04/oj4VNFutshkQpbl.png)

![image-20210304141147480](https://i.loli.net/2021/03/04/KDMA1zi6PeujFIc.png)



### 热力图

```
df_corr = combine.corr()
plt.figure(figsize=(20,20))
g=sns.heatmap(df_corr,annot=True,cmap="RdYlGn")
```

![image-20210304141345224](https://i.loli.net/2021/03/04/Oh2F4wrV5WZtLal.png)