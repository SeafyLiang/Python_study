# pandas-groupby常见用法



## groupby过程图解

> ​	总的来说，`groupby`的过程就是将原有的`DataFrame`按照`groupby`的字段（这里是`company`），划分为若干个`分组DataFrame`，被分为多少个组就有多少个`分组DataFrame`。**所以说，在`groupby`之后的一系列操作（如`agg`、`apply`等），均是基于`子DataFrame`的操作。**理解了这点，也就基本摸清了Pandas中`groupby`操作的主要原理。下面来讲讲`groupby`之后的常见操作。

> 内容参考自  [知乎-Pandas之超好用的Groupby用法详解](https://zhuanlan.zhihu.com/p/101284491?utm_source=wechat_session)

![img](https://i.loli.net/2021/04/03/oZDLJ53mvxbTfM8.jpg)



## 8个常见用法

### 代码地址(可在线预览)💻📲

[pandas-groupby常见用法-github](https://github.com/SeafyLiang/Python_study/blob/master/pandas_study/pandas_groupby.ipynb)

[pandas-groupby常见用法-gitee](https://gitee.com/seafyLiang/Python_study/blob/master/pandas_study/pandas_groupby.ipynb)

### 加载 sklearn-鸢尾花 公开数据集

```python
import pandas as pd
from sklearn import datasets

# 加载数据集和目标
data, target = datasets.load_iris(return_X_y=True, as_frame=True)
# 合并数据集和目标
iris = pd.concat([data, target], axis=1, sort=False)
iris
```

![image-20210403233004022](https://i.loli.net/2021/04/03/dVqHvo5N7yUu9lB.png)

### 生成groupby对象

```python
iris_gb = iris.groupby('target')
type(iris_gb)
```

> pandas.core.groupby.generic.DataFrameGroupBy



### 1. 创建频率表

​	假如我想知道每个species类中的数量有多少，那么直接使用groupby的size函数即可

```python
iris_gb.size()
```

![image-20210403233139187](https://i.loli.net/2021/04/03/Xur3hmLDOdCgWc8.png)

### 2. 计算常用的描述统计量

min、max()、medianhe、std等

```python
# 计算均值
iris_gb.mean()
```

![image-20210403233219925](https://i.loli.net/2021/04/03/y4RTpg7MaVu8U92.png)

```python
# 单列
iris_gb['sepal length (cm)'].mean()
```

![image-20210403233242014](https://i.loli.net/2021/04/03/GORgxwqjJITpVC1.png)

```python
# 双列
iris_gb[['sepal length (cm)', 'sepal width (cm)']].mean()
```

![image-20210403233301947](https://i.loli.net/2021/04/03/tbiw1pQexaZROvo.png)

### 3. 查找最大值（最小值）索引

```python
# 查找每个组的最大值或最小值的索引
iris_gb.idxmax()
```

![image-20210403233351208](https://i.loli.net/2021/04/03/e93tDjXyrHn8WUd.png)

```python
# 查找每组sepal_length最大值对应的整条记录时，就可以这样用。注意，这里是整条记录，相当于按sepal_length最大值这个条件进行了筛选。
sepal_largest = iris.loc[iris_gb['sepal length (cm)'].idxmax()]
sepal_largest
```

![image-20210403233424691](https://i.loli.net/2021/04/03/1CtDMRuQFwv37GI.png)

### 4. groupby后重置索引

很多时候，在groupby处理后还要进行其他操作。也就是说，我们想重置分组索引以使其成为正常的行和列。 第一种方法可能大家常用，就是通过reset_index()让乱序索引重置。

```python
iris_gb.max().reset_index()
```

![image-20210403233502840](https://i.loli.net/2021/04/03/JHyEpP3QT7KDZqI.png)

但其实，还有一个看上去更加友好的用法。可以在groupby的时候就设置as_index参数，也可以达到同样效果。

```python
iris.groupby('target', as_index=False).max()
```

![image-20210403233528586](https://i.loli.net/2021/04/03/x2r3zAtQHOXEp8n.png)

### 5. 多种统计量汇总

上面都是单个统计量的操作，那如果我想同时操作好几个呢？

groupby还有一个超级棒的用法就是和聚合函数agg连起来使用。

```python
iris_gb[['sepal length (cm)', 'sepal width (cm)']].agg(["min", "mean"])
```

![image-20210403233619564](https://i.loli.net/2021/04/03/auZD3ntXHL6e8Ss.png)

### 6. 特定列的聚合

上面是的多个操作对于每个列都是一样的。实际使用过程中，我们可能对于每个列的需求都是不一样的。

所以在这种情况下，可以通过为不同的列单独设置不同的统计量。

```python
iris_gb.agg({"sepal length (cm)": ["min", "max"], "sepal width (cm)": ["mean", "std"]})
```

![image-20210403233658396](https://i.loli.net/2021/04/03/IU4vMdZDfrYcNRj.png)

### 7. NamedAgg命名统计量

上面的多级索引看起来有点不太友好，我想把每个列下面的统计量和列名分别合并起来。可以使用NamedAgg来完成列的命名。

```python
iris_gb.agg(
     sepal_min=pd.NamedAgg(column="sepal length (cm)", aggfunc="min"),
     sepal_max=pd.NamedAgg(column="sepal length (cm)", aggfunc="max"),
     petal_mean=pd.NamedAgg(column="petal length (cm)", aggfunc="mean"),
     petal_std=pd.NamedAgg(column="petal length (cm)", aggfunc="std")
 )
```

![image-20210403233739806](https://i.loli.net/2021/04/03/3zws94tD2VriMEA.png)

因为NamedAgg是一个元组，所以我们也可以直接赋值元组给新的命名，效果一样，但看上去更简洁。

```python
iris_gb.agg(
    sepal_min=("sepal length (cm)", "min"),
    sepal_max=("sepal length (cm)", "max"),
    petal_mean=("petal length (cm)", "mean"),
    petal_std=("petal length (cm)", "std")
)
```

![image-20210403233809354](https://i.loli.net/2021/04/03/Q8rpHkEFovPu7yU.png)

### 8. 使用自定义函数

上面agg聚合函数中我们都是通过添加一个统计量名称来完成操作的，除此之外我们也可直接给一个功能对象。

```python
iris_gb.agg(pd.Series.mean)
```

![image-20210403233840902](https://i.loli.net/2021/04/03/R2xCzo3JISEwtsT.png)

不仅如此，名称和功能对象也可一起使用。

```python
iris_gb.agg(["min", pd.Series.mean])
```

![image-20210403233909210](https://i.loli.net/2021/04/03/SCA5UWjYBLTyP4I.png)

还可以自定义函数

```python
def double_length(x):
    return 2*x.mean()

iris_gb.agg(double_length)
```

![image-20210403233944541](https://i.loli.net/2021/04/03/AVhvBeDfUtTcu1r.png)

如果想更简洁，也可以使用lambda函数。总之，用法非常灵活，可以自由组合搭配。

```python
iris_gb.agg(lambda x: x.mean())
```

![image-20210403234008387](https://i.loli.net/2021/04/03/YjRXrkHa7ZqeyBl.png)

