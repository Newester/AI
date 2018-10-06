#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# numpy 包含 numpy.linalg 模块，提供线性代数的所有功能
# dot -- 两个数组的点积
# vdot -- 两个向量的点积
# inner -- 两个数组的内积
# matmul -- 两个数组的矩阵积
# determinant -- 数组的行列式
# solve -- 求解线性矩阵方程
# inv -- 寻找矩阵的乘法逆矩阵

import numpy.matlib
import numpy as np 

# numpy.dot() 
# 返回两个数组的点积
# 对于一维数组 -- 向量的内积
# 对于二维数组 -- 矩阵的乘法
# 对于 N 维数组 -- a 的最后一个轴上的和与 b 的倒数第二个轴的乘积
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
print(np.dot(a,b))

# numpy.vdot()
# 两个向量的点积，如果是多维数组会被展开
print(np.vdot(a,b))

# numpy.inner()
# 一维数组的向量内积，如果是多维数组，则是最后一个轴上的和的乘积
print(np.inner(np.array([1,2,3]),np.array([0,1,0])))
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
print(np.inner(a,b))

# numpy.matmul()
# 对于二维数组，就是矩阵乘法
# 对于一位数组提升为矩阵，计算完再去除
# 对于维度 >2 的数组，将其视为存在于最后两个索引的栈，进行广播
a = [[1,0],[0,1]]
b = [[4,1],[2,2]]
print(np.matmul(a,b))

b = [1,2]
print(np.matmul(a,b))
print(np.matmul(b,a))

a = np.arange(8).reshape(2,2,2)
b = np.arange(4).reshape(2,2)
print(np.matmul(a,b))

# numpy.linalg.det() -- 计算矩阵的行列式的值
a = np.array([[1,2],[3,4]])
print(np.linalg.det(a))

# numpy.linalg.solve(a,b) -- 解方程组 ax = b
# numpy.linalg.inv() -- 计算矩阵的逆
x = np.array([[1,2],[3,4]])
y = np.linalg.inv(x)
print(y)
print(np.dot(x,y))

a = np.array([[1,1,1],[0,2,5],[2,5,-1]])
b = np.array([6,-4,27])
x = np.linalg.solve(a,b) # 计算 x = a^(-1)b
print(x)
ainv = np.linalg.inv(a)
print(np.dot(ainv,b))


