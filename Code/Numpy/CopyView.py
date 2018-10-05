#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import numpy as np 

# 简单赋值不会创建数组对象的副本。
a = np.arange(6)
print(id(a))
b = a
print(id(b))

# 对 b 的修改会作用到 a
b.shape = 3,2
print(b)
print(a)

# numpy.view() 
# 视图或浅复制，新的数组对象可以查看但不会改变原数组的数据
a = np.arange(6).reshape(3,2)
b = a.view()
print(id(a))
print(id(b))
print(b)
b.shape = 2,3
print(a)
# 数组的切片会创建视图
a = np.array([[10,10],[2,3],[4,5]])
s = a[:,:2]
print(s)

# numpy.copy() 
# 创建数组及其数据的完整副本，不与原数组共享
a = np.array([[10,10],[2,3],[4,5]])
b = a.copy()
b[0,0] = 100
print(a[0,0])