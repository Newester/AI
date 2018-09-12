#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import numpy as np

# ndarray.shape 返回包含数组维度的元组，可用于调整数组大小
a = np.array([[1,2,3],[4,5,6]])
print(a.shape) #2行3列
# 调整数组大小
a = np.array([[1,2,3],[4,5,6]])
a.shape = (3,2)
print(a)
# reshape() 函数也可以调整数组大小
b = a.reshape(2,3)
print(b)

# ndarray.ndim 返回数组的维数
a = np.arange(24)
print(a)
print(a.ndim)
b = a.reshape(2,4,3)
print(b)
print(b.ndim)

# numpy.itemsize 返回数组中每个元素的字节单位长度
x = np.array([1,2,3,4,5],dtype=np.int8)
print(x.itemsize)
x = np.array([1,2,3,4,5],dtype=np.float32)
print(x.itemsize)

# numpy.flags
# 返回对象属性的当前值
# ndarray 对象有如下的属性
# C_CONTIGUOUS (C) -- 数组位于单一的、C风格的连续区段内
# F_CONTIGUOUS (F) -- 数组位于单一的、Fortran 风格的连续区段内
# OWNDATA (O) -- 数组的内存从他处借用
# WRITEABLE (W) -- 数据区域可写入
# ALIGNED (A) -- 数据和任何元素会为硬件适当对齐
# UPDATEIFCOPY (U) -- 是另一数组的副本，当这个数组被释放时，源数组会由这个数组中元素更新
x = np.array([1,2,3,4,5])
print(x.flags)