#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PCA02.py
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021-04-23 20:12:12   SeafyLiang   1.0        PCA算法封装
"""
import numpy as np


class PCA:
    def __init__(self, n_components):
        # 主成分的个数n
        self.n_components = n_components
        # 具体主成分
        self.components_ = None

    def fit(self, X, eta=0.001, n_iters=1e4):
        '''均值归零'''

        def demean(X):
            return X - np.mean(X, axis=0)

        '''方差函数'''

        def f(w, X):
            return np.sum(X.dot(w) ** 2) / len(X)

        '''方差函数导数'''

        def df(w, X):
            return X.T.dot(X.dot(w)) * 2 / len(X)

        '''将向量化简为单位向量'''

        def direction(w):
            return w / np.linalg.norm(w)

        '''寻找第一主成分'''

        def first_component(X, initial_w, eta, n_iters, epsilon=1e-8):
            w = direction(initial_w)
            cur_iter = 0

            while cur_iter < n_iters:
                gradient = df(w, X)
                last_w = w
                w = w + eta * gradient
                w = direction(w)
                if (abs(f(w, X) - f(last_w, X)) < epsilon):
                    break
            cur_iter += 1

            return w

        # 过程如下
        # 归0操作
        X_pca = demean(X)
        # 初始化空矩阵,行为n个主成分,列为样本列数
        self.components_ = np.empty(shape=(self.n_components, X.shape[1]))
        # 循环执行每一个主成分
        for i in range(self.n_components):
            # 每一次初始化一个方向向量W
            initial_w = np.random.random(X_pca.shape[1])
            # 使用梯度上升法,得到此时的X_PCA所对应的第一主成分W
            w = first_component(X_pca, initial_w, eta, n_iters)
            # 存储起来
            self.components_[i:] = w
            # X_pca减去样本在W上的所有分量,形成一个新的X_pca,以便进行下一次循环
            X_pca = X_pca - X_pca.dot(w).reshape(-1, 1) * w
        return self

    # 将X数据集映射到各个主成分分量中
    def transform(self, X):
        assert X.shape[1] == self.components_.shape[1]
        return X.dot(self.components_.T)

    def inverse_transform(self, X):
        return X.dot(self.components_)


# Sklearn调用PCA
# 1. 准备数据
import numpy as np
import matplotlib.pyplot as plt

X = np.empty((100, 2))
X[:, 0] = np.random.uniform(0., 100., size=100)
X[:, 1] = 0.75 * X[:, 0] + 3. + np.random.normal(0, 10., size=100)

# 2.然后fit下,求出主成分
from sklearn.decomposition import PCA

# 初始化实例对象，传入主成分个数
pca = PCA(n_components=1)
pca.fit(X)

# 3.验证一下pca求出的主成分,是一个方向向
print(pca.components_)  # [[-0.76481933 -0.64424482]]

# 4.在得到主成分之后,使用 transform方法将矩阵X进行降维。得到一个特征的数据集
X_reduction = pca.transform(X)
print(X_reduction.shape)  # (100, 1)

# 使用PCA和KNN对手写数字数据集做测试
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

digits = datasets.load_digits()
X = digits.data
y = digits.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)

# 对原始数据集进行训练,看看识别的结果
knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train, y_train)
print(knn_clf.score(X_test, y_test))  # 0.9866666666666667

# 下面用PCA算法对数据进行降维:
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca.fit(X_train)
X_train_reduction = pca.transform(X_train)  # 训练数据集降维结果
X_test_reduction = pca.transform(X_test)  # 测试数据集降维结果

# 下面使用降维后的数据,观察其kNN算法的识别精度
knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train_reduction, y_train)
print(knn_clf.score(X_test_reduction, y_test))  # 0.6066666666666667

# 主成分解释方差比例
print(pca.explained_variance_ratio_)  # [0.14566817 0.13735469]
# PCA保持64维
pca = PCA(n_components=X_train.shape[1])
pca.fit(X_train)
print(pca.explained_variance_ratio_)

# 横轴是是样本X的i个特征数,纵轴是前i个轴解释方差比例的和
plt.plot([i for i in range(X_train.shape[1])],
         [np.sum(pca.explained_variance_ratio_[:i + 1]) for i in range(X_train.shape[1])])
plt.show()

# 查看一下降维后主成分的个数为28,即对于64维数据来说,28维数据就可以解释95%以上的方差。
pca = PCA(0.95)
pca.fit(X_train)
# PCA(copy=True, iterated_power='auto', n_components=0.95, random_state=None, svd_solver='auto', tol=0.0, whiten=False)
print(pca.n_components_)

# 然后用这种pca去重新使用kNN做训练,得到的结果较好。
X_train_reduction = pca.transform(X_train)
X_test_reduction = pca.transform(X_test)
knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train_reduction, y_train)
knn_clf.score(X_test_reduction, y_test)

# 数据降维还有一个作用是可视化,降到2维数据之后
pca = PCA(n_components=2)
pca.fit(X)
X_reduction = pca.transform(X)
for i in range(10):
    plt.scatter(X_reduction[y == i, 0], X_reduction[y == i, 1], alpha=0.8)
plt.show()
