# pandas-数据透视表

> 数据透视表(pivot table) 是一种类似GroupBy的操作方法，常见于Excel中。数据透视表将每一列数据作为输入，输出将数据不断细分为多个维度累计信息的二维数据表。

![image-20210408210124718](https://i.loli.net/2021/04/08/cGHkVdoFByugmEP.png)

## 使用语法

DataFrame 的pivot_table 方法的完整签名如下所示：

```python
pandas.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All', observed=False) 

```

## 参数解析

- data：dataframe格式数据
- values：需要汇总计算的列，可多选
- index：行分组键，一般是用于分组的列名或其他分组键，作为结果DataFrame的行索引
- columns：列分组键，一般是用于分组的列名或其他分组键，作为结果DataFrame的列索引
- aggfunc：聚合函数或函数列表，默认为平均值
- fill_value：设定缺失替换值
- margins：是否添加行列的总计
- dropna：默认为True，如果列的所有值都是NaN，将不作为计算列，False时，被保留
- margins_name：汇总行列的名称，默认为All
- observed：是否显示观测值



## 代码实践

![image-20210408211726370](https://i.loli.net/2021/04/08/VOshbZ6S9n4W5kw.png)

```python
import numpy as np
import pandas as pd
import seaborn as sns
titanic = sns.load_dataset('titanic')

titanic.pivot_table(index='sex', columns='class')
```

![image-20210408211709352](https://i.loli.net/2021/04/08/u53hxNz7f4QOIRn.png)

```python
# 默认对所有列进行聚合，这时我们给与values参数，只计算想要的结果
agg = pd.cut(titanic["age"],[0,18,80])	# 对年龄数据列进行分段，便于观看
titanic.pivot_table(index=['sex','age'], columns='class',values=['survived','fare'])
```

![image-20210408211754228](https://i.loli.net/2021/04/08/bA7xUEwyNs5lLaV.png)

```python
# 在实际使用中，并不一定每次都要均值，使用aggfunc指定累计函数
titanic.pivot_table(index='sex', columns='class',aggfunc={'survived':sum, 'fare':'mean'})
```

![image-20210408211818426](https://i.loli.net/2021/04/08/yj8ucSqzlJD4gZw.png)

```python
# 当需要计算每一组的总数时，可以通过margins 参数来设置：
# margin 的标签可以通过margins_name 参数进行自定义，默认值是"All"。
titanic.pivot_table('survived', index='sex', columns='class', margins=True)
```

![image-20210408211840989](https://i.loli.net/2021/04/08/yOGPEw8Wr5mCshu.png)