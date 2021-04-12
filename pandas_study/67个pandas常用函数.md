# 67个pandas常用函数

## 目录：

- 导⼊数据
- 导出数据
- 查看数据
- 数据选取
- 数据处理
- 数据分组和排序
- 数据合并



## 导入数据

```python
pd.DataFrame() # 自己创建数据框，用于练习

pd.read_csv(filename) # 从CSV⽂件导⼊数据

pd.read_table(filename) # 从限定分隔符的⽂本⽂件导⼊数据

pd.read_excel(filename) # 从Excel⽂件导⼊数据

pd.read_sql(query,connection_object) # 从SQL表/库导⼊数据

pd.read_json(json_string) # 从JSON格式的字符串导⼊数据

pd.read_html(url) # 解析URL、字符串或者HTML⽂件，抽取其中的tables表格
```



## 导出数据

```python
df.to_csv(filename) #导出数据到CSV⽂件

df.to_excel(filename) #导出数据到Excel⽂件

df.to_sql(table_name,connection_object) #导出数据到SQL表

df.to_json(filename) #以Json格式导出数据到⽂本⽂件

writer=pd.ExcelWriter('test.xlsx',index=False) 
df1.to_excel(writer,sheet_name='单位')和writer.save()，将多个数据帧写⼊同⼀个⼯作簿的多个sheet(⼯作表)
```



## 查看数据

```python
df.head(n) # 查看DataFrame对象的前n⾏

df.tail(n) # 查看DataFrame对象的最后n⾏

df.shape() # 查看⾏数和列数

df.info() # 查看索引、数据类型和内存信息

df.columns() # 查看字段（⾸⾏）名称

df.describe() # 查看数值型列的汇总统计

s.value_counts(dropna=False) # 查看Series对象的唯⼀值和计数

df.apply(pd.Series.value_counts) # 查看DataFrame对象中每⼀列的唯⼀值和计数

df.isnull().any() # 查看是否有缺失值

df[df[column_name].duplicated()] # 查看column_name字段数据重复的数据信息

df[df[column_name].duplicated()].count() # 查看column_name字段数据重复的个数
```



## 数据选取

```python
df[col] # 根据列名，并以Series的形式返回列

df[[col1,col2]] # 以DataFrame形式返回多列

s.iloc[0] # 按位置选取数据

s.loc['index_one'] # 按索引选取数据

df.iloc[0,:] # 返回第⼀⾏

df.iloc[0,0] # 返回第⼀列的第⼀个元素

df.loc[0,:] # 返回第⼀⾏（索引为默认的数字时，⽤法同df.iloc），但需要注意的是loc是按索引,iloc参数只接受数字参数

df.ix[[:5],["col1","col2"]] # 返回字段为col1和col2的前5条数据，可以理解为loc和
iloc的结合体。

df.at[5,"col1"] # 选择索引名称为5，字段名称为col1的数据

df.iat[5,0] # 选择索引排序为5，字段排序为0的数据
```



## 数据处理

```python
df.columns= ['a','b','c'] # 重命名列名（需要将所有列名列出，否则会报错）

pd.isnull() # 检查DataFrame对象中的空值，并返回⼀个Boolean数组

pd.notnull() # 检查DataFrame对象中的⾮空值，并返回⼀个Boolean数组

df.dropna() # 删除所有包含空值的⾏

df.dropna(axis=1) # 删除所有包含空值的列

df.dropna(axis=1,thresh=n) # 删除所有⼩于n个⾮空值的⾏

df.fillna(value=x) # ⽤x替换DataFrame对象中所有的空值，⽀持

df[column_name].fillna(x)

s.astype(float) # 将Series中的数据类型更改为float类型

s.replace(1,'one') # ⽤‘one’代替所有等于1的值

s.replace([1,3],['one','three']) # ⽤'one'代替1，⽤'three'代替3

df.rename(columns=lambdax:x+1) # 批量更改列名

df.rename(columns={'old_name':'new_ name'}) # 选择性更改列名

df.set_index('column_one') # 将某个字段设为索引，可接受列表参数，即设置多个索引

df.reset_index("col1") # 将索引设置为col1字段，并将索引新设置为0,1,2...

df.rename(index=lambdax:x+1) # 批量重命名索引
```



## 数据分组和排序

```python
df.sort_index().loc[:5] # 对前5条数据进⾏索引排序

df.sort_values(col1) # 按照列col1排序数据，默认升序排列

df.sort_values(col2,ascending=False) # 按照列col1降序排列数据

df.sort_values([col1,col2],ascending=[True,False]) # 先按列col1升序排列，后按col2降序排列数据

df.groupby(col) # 返回⼀个按列col进⾏分组的Groupby对象

df.groupby([col1,col2]) # 返回⼀个按多列进⾏分组的Groupby对象

df.groupby(col1)[col2].agg(mean) # 返回按列col1进⾏分组后，列col2的均值,agg可以接受列表参数，agg([len,np.mean])

df.pivot_table(index=col1,values=[col2,col3],aggfunc={col2:max,col3:[ma,min]}) # 创建⼀个按列col1进⾏分组，计算col2的最⼤值和col3的最⼤值、最⼩值的数据透视表

df.groupby(col1).agg(np.mean) # 返回按列col1分组的所有列的均值,⽀持

df.groupby(col1).col2.agg(['min','max'])

data.apply(np.mean) # 对DataFrame中的每⼀列应⽤函数np.mean

data.apply(np.max,axis=1) # 对DataFrame中的每⼀⾏应⽤函数np.max

df.groupby(col1).col2.transform("sum") # 通常与groupby连⽤，避免索引更改
```



## 数据合并

```python
df1.append(df2) # 将df2中的⾏添加到df1的尾部

df.concat([df1,df2],axis=1,join='inner') # 将df2中的列添加到df1的尾部,值为空的对应⾏与对应列都不要

df1.join(df2.set_index(col1),on=col1,how='inner') # 对df1的列和df2的列执⾏SQL形式的join，默认按照索引来进⾏合并，如果df1和df2有共同字段时，会报错，可通过设置lsuffix,rsuffix来进⾏解决，如果需要按照共同列进⾏合并，就要⽤到set_index(col1)

pd.merge(df1,df2,on='col1',how='outer') # 对df1和df2合并，按照col1，⽅式为outer

pd.merge(df1,df2,left_index=True,right_index=True,how='outer') # 与 df1.join(df2, how='outer')效果相同
```

