#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PCA.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/4/23 11:22   SeafyLiang   1.0       PCA算法的实现与使用
"""
import numpy as np
import matplotlib.pyplot as plt

# 1. 准备数据
X = np.empty([100, 2])
X[:, 0] = np.random.uniform(0., 100., size=100)
X[:, 1] = 0.75 * X[:, 0] + 3. + np.random.normal(0., 10., size=100)
plt.scatter(X[:, 0], X[:, 1])
plt.show()


# 2. 函数实现
# 2.1 均值归0
def demean(X):
    # axiS=0按列计算均值,即每个属性的均值,1则是计算行的均值
    return X - np.mean(X, axis=0)


X_demean = demean(X)
# 注意看数据分布没变,但是坐标已经以原点为中心了
plt.scatter(X_demean[:, 0], X_demean[:, 1])
plt.show()


# 2.2 对目标(方差)函数和梯度(导数)函数的定义
# 2.2.1 目标函数
def f(w, X):
    return np.sum((X.dot(w) ** 2)) / len(X)


# 2.2.2 求梯度
def df_math(w, X):
    return X.T.dot(X.dot(w)) * 2. / len(X)


# 2.2.3 一种用于验证梯度求解是否正确的方法。现在对 其稍加改造,可以验证我们之前计算的梯度表达式的结果是否正确
# 验证梯度求解是否正确,使用梯度调试方法:
def df_debug(w, X, epsilon=0.0001):
    # 先创建一个与参数组等长的向量
    res = np.empty(len(w))
    # 对于每个梯度,求值
    for i in range(len(w)):
        w_1 = w.copy()
        w_1[i] += epsilon
        w_2 = w.copy()
        w_2[i] -= epsilon
        res[i] = (f(w_1, X) - f(w_2, X)) / (2 * epsilon)
    return res


# 使用np中的线性代数库 inal里面的norm()方法,求第二范数,也就是求算术平方根
def direction(w):
    return w / np.linalg.norm(w)


# 梯度上升法代码
def gradient_ascent(df, X, initial_w, eta, n_iters=1e4, epsilon=1e-8):
    w = direction(initial_w)
    cur_iter = 0
    while cur_iter < n_iters:
        gradient = df_math(w, X)
        last_w = w
        w = last_w + eta * gradient
        w = direction(w)  # 将w转换成单位向量
        if abs(f(w, X) - f(last_w, X)) < epsilon:
            break
        cur_iter += 1
    return w


# 线性回归中,通常将特征系数θ的值设为全部为0的向量。但在主成分分析中w的初始值不能为0!!!这是因为如果
# 将W=0带入梯度求导的公式中,也是每次求梯度得到的都是没有任何方向的0。所以要设置一组随机数。
initial_w = np.random.random(X.shape[1])
eta = 0.001

w = gradient_ascent(df_debug, X_demean, initial_w, eta)
# 输出
# array([0.76567331, 0.64322965])

# 3 结果可视化
# 进行可视化,轴对应的方向,即将样本映射到该轴上的方差最大,这个轴就是一个主成分(第一主成分)
plt.scatter(X_demean[:, 0], X_demean[:, 1])
plt.plot([0, w[0] * 30], [0, w[1] * 30], color='red')
plt.show()

# 4 求第二主成分的实现
X_new = X - X.dot(w).reshape(-1, 1) * w
plt.scatter(X_new[:, 0], X_new[:, 1])
plt.show()

w_new = gradient_ascent(df_math, X_new, initial_w, eta)
print(w_new)


# 输出
# array([-0.64320916, 0.76569052])

# 5 求前n主成分
def first_n_component(n, X, eta=0.001, n_iters=1e4, epsilon=1e-8):
    X_pca = X.copy()
    X_pca = demean(X_pca)
    res = []
    for i in range(n):
        initial_w = np.random.random(X_pca.shape[1])
        w = gradient_ascent(df_math, X_pca, initial_w, eta)
        res.append(w)
        X_pca = X_pca - X_pca.dot(w).reshape(-1, 1) * w
    return res
