#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import numpy as np 

# numpy.reshape(arr,newshape,order)
# 不修改原来数据的情况下修改数组的形状
# arr -- 要修改形状的数组
# newshape -- 新的形状应当兼容旧的形状
# order -- 'C' C 风格； 'F' F 风格； 'A' 保留原顺序

a = np.arange(8)
print(a)

b = a.reshape(4,2) # 4 行 2 列
print(b)

# numpy.ndarray.flat
# 返回数组上的一维数组迭代器
print(b.flat[...])

# numpy.ndarray.flatten(order)
# order -- 'C' 按行； 'F' 按列； 'A' 按原顺序； 'k' 按内存中出现的顺序
print(b)
print(b.flatten())
print(b.flatten(order='F'))

# numpy.ravel(a, order)
print(b.ravel())
print(b.ravel(order='F'))

# numpy.transpose(arr, axes)
# arr 要转置的数组
# axes 整数的列表，对应维度，通常所有的维度都会翻转
print(np.transpose(b))

# numpy.ndarray.T
print(b.T)

# numpy.rollaxis(arr, axis, start=0)
# arr -- 输入数组
# axis -- 要向后滚动的轴，其他轴的相对位置不会改变
# 默认为 0 ，表示完整的滚动，会滚动到特定的位置

a = np.arange(8).reshape(2,2,2)
print(a)
# 将轴 2 滚动到轴 0
print(np.rollaxis(a,2))

# 将轴 0 滚动到轴 1
print(np.rollaxis(a,2,1))

# numpy.swapaxes(arr, axis1, axis2)
print(np.swapaxes(a,2,0))

# broadcast
x = np.array([[1],[2],[3]])
y = np.array([4,5,6])

b = np.broadcast(x,y)
r,c = b.iters

print(b.shape)
b = np.broadcast(x,y)
c = np.empty(b.shape)
print(c.shape)

c.flat =  [u + v for (u,v) in b]
print(c)

print(x + y)

# numpy.broadcast_to(array,shape,subok)
a = np.arange(4).reshape(1,4)
print(a)
print(np.broadcast_to(a,(4,4)))

# numpy.expand_dims(arr,axis)
# arr 输入数组
# axis 新插入的位置
x = np.array(([1,2],[3,4]))
y = np.expand_dims(x,0)
print(y)
print(x.shape,y.shape)
y = np.expand_dims(x,axis=1)
print(y)
print(x.ndim,y.ndim)
print(x.shape,y.shape)

#numpy.squeeze(arr,axis)
# 从给定数组中删除一维条目
# arr
# axis 整数或元组
x = np.arange(9).reshape(1,3,3)
y = np.squeeze(x)
print(y)
print(x.shape,y.shape)

# numpy.concatenate((a1,a2,...), axis)
# 沿指定轴连接相同形状的两个或者多个数组
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(np.concatenate((a,b)))
print(np.concatenate((a,b),axis=1))

# numpy.stack(arrays,axis)
# 沿新轴连接数组序列
print(np.stack((a,b),0))
print(np.stack((a,b),1))

# numpy.hstack
# 生成水平堆叠的单个数组
c = np.hstack((a,b))
print(c)

# numpy.vstack
# 生成竖直堆叠的单个数组
c = np.vstack((a,b))
print(c)

#数组分割
# numpy.split(array,indices_or_sections,axis)
a = np.arange(9)
#均分
b = np.split(a,3)
print(b)
# 位置分割
b = np.split(a,[4,7])
print(b)

a = np.arange(16).reshape(4,4)
b = np.hsplit(a,2)
print(b)
b = np.vsplit(a,2)
print(b)

# numpy.resize(arr,shape)
# 返回指定大小的新数组
a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)
b = np.resize(a,(3,2))
print(b)
b = np.resize(a,(3,3))
print(b)

# numpy.append(arr, values, axis)
# arr
# values
# axis
a = np.array([[1,2,3],[4,5,6]])
print(a)
print('-----------------')
print(np.append(a,[7,8,9]))
print('-----------------')
print(np.append(a,[[7,8,9]],axis=0))
print('-----------------')
print(np.append(a,[[5,5,5],[7,8,9]],axis=1))
print('-----------------')

# numpy.insert(arr,obj,values,axis)
# 在给定索引之前，沿给定轴在输入数组中插入值
# arr 输入数组
# obj 在其之前插入值的索引
# values 要插入的值
# axis 沿着它插入的轴，如果未提供，则数组会被展开
a = np.array([[1,2],[3,4],[5,6]])
print(a)
print(np.insert(a,3,[11,12]))
print(np.insert(a,1,[11],axis=0))
print(np.insert(a,1,11,axis=1))

# numpy.delete(arr,obj,axis)
# 从数组中删除指定子数组
a = np.arange(12).reshape(3,4)
print(np.delete(a,5))
print(np.delete(a,1,axis=1))

a = np.array([1,2,3,4,5,6,7,8,9,10])
print(np.delete(a,np.s_[::2]))

# numpy.unique(arr,return_index,return_inverse,return_counts)
# arr 输入数组，如果不是一维则会展开
# return_index 如果为 true 返回数组中的元素下标
# return_inverse 如果为 true 返回去重数组的下标
# return_counts 如果为 True 返回去重数组的元素在原数组中出现的次数
a = np.array([5,2,6,2,7,5,6,8,2,9])
print(a)
u = np.unique(a)
print(u)
u,indices = np.unique(a,return_index=True)
print(indices)
print(u)
u,indices = np.unique(a,return_inverse=True)
print(indices)
print(u)
u,indices = np.unique(a,return_counts=True)
print(indices)
