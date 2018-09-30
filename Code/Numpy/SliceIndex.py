#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import numpy as np

a = np.arange(10)
s = slice(2,7,2) #起始 终止 步长
print(a[s])

t = a[2:7:2]
print(a[t])

print(a[5])

print(a[2:])

print(a[2:5])

# 多维 ndarray
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a)

print(a[1:])

# 使用省略号 ...

# 第二列
print(a[...,1])

# 第二行
print(a[1,...])

# 第 2 到 n 列
print(a[...,1:])

# 高级索引，返回数据的副本

# 整数索引
x = np.array([[1,2],[3,4],[5,6]])
y = x[[0,1,2],[0,1,0]] # (0,0) (1,1) (2,0)
print(y)

# 切片与高级索引切片（可能导致不同的内存布局）
x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
z = x[1:4,1:3]
print(z)
y = x[1:4,[1,2]]
print(y)

# 布尔索引
print(x[ x > 5 ])

a = np.array([np.nan,1,2,np.nan,3,4,5])
print(a[~np.isnan(a)])

a = np.array([1,2+6j,5,3.5+5j])
print(a[np.iscomplex(a)])

