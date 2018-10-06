#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import numpy.matlib 
import numpy as np 

# 填充为随机数据
print(np.matlib.empty((2,2)))

# 以 0 填充
print(np.matlib.zeros((2,2)))

# 以 1 填充
print(np.matlib.ones((2,2)))

# 以 1 填充对角线，以 0 填充其他位置
# numpy.matlib.eye(n,M,k,dtype)
# n -- 行数
# M -- 列数，默认 = n
# k -- 对角线的首行起始索引
# dtype -- 数据类型
print(np.matlib.eye(n=3, M=4, k=0, dtype= float))

# 单位阵
# numpy.matlib.identity(n,dtype)
print(np.matlib.identity(5,dtype=float))

# 给定大小的填充随机值的矩阵
print(np.matlib.rand(3,3))

# 矩阵总是二维的， ndarray 是 n 维数组，可以相互转换
i = np.matrix('1,2;3,4')
print(i)
j = np.asarray(i)
print(j)
k = np.asmatrix(j)
print(k)
print(type(i))
print(type(j))
print(type(k))
