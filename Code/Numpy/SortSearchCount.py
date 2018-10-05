#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
#  |种类|   |速度|  |最坏情况|  |稳定性|
# 快速排序    1     O(N^2)      否
# 归并排序     2     O(N*logN)  是
# 堆排序       3      O(N*logN) 否

import numpy as np 

# numpy.sort(a,axis,kind='quicksort',order)
# a -- 要排序的数组
# axis -- 沿着它排序数组的轴，如果没有数组会展开
# kind -- 排序类型： quicksort mergesort heapsort
a = np.array([[3,7],[9,1]])
print(np.sort(a))
print(np.sort(a,axis=0))

dt = np.dtype([('name','S10'),('age',int)])
a = np.array([('rayu',21),('anil',25),('ravi',17),('amar',27)], dtype = dt)
print(np.sort(a,order='name'))

# numpy.argsort()
# 对输入的数组沿指定的轴进行间接排序，返回索引数组
x = np.array([5,9,7])
y = np.argsort(x)
print(x[y])

# numpy.argmax()
# numpy.argmin()
# 沿指定轴返回最大和最小元素的索引
a = np.array([[30,40,70],[80,20,10],[50,90,60]])
print(np.argmax(a))
print(a.flatten())
maxindex = np.argmax(a,axis=0)
print(maxindex)
minindex = np.argmin(a,axis=1)
print(minindex)

# numpy.nonzero() -- 返回非零元素的索引
a = np.array([[30,40,0],[0,20,10],[50,0,60]])
print(np.nonzero(a))

# numpy.where()　-- 返回输入数组中满足给定条件的元素的索引
x = np.arange(9.).reshape(3,3)
y = np.where(x > 3)
print(y)
print(x[y])

# numpy.extract() -- 返回满足任何条件的元素
condition = np.mod(x,2) == 0
print(np.extract(condition,x))
