#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import numpy as np

# numpy.empty(shape, dtype = float, order = 'C')
# shape 数组的形状,整数或者整数的元组
# dtype 数组类型
# order ['C','F'] C 风格或者 Frotran 风格
x = np.empty([3,2], dtype = np.int)
# 未被初始化
print(x)

# numpy.zeros(shape, dtype = float, order = 'C')
x = np.zeros(5)
print(x)

x = np.zeros((5,),dtype = np.int)
print(x)

x = np.zeros((2,2), dtype = [('x','i4'),('y','i4')])
print(x)

# numpy.ones(shape, dtype = None, order = 'C')
x = np.ones(5)
print(x)

x = np.ones([2,2], dtype = np.int)
print(x)

# numpy.asarray(a, dtype= None, order = None)
# a 列表，元组以及它们的组合
x = [1,2,3]
a = np.asarray(x)
print(a)

a = np.asarray(x, dtype = float)
print(a)

x = (1,2,3)
a = np.asarray(x)
# 输入为元组，输出为列表
print(a)

x = [(1,2,3),(4,5)]
a = np.asarray(x)
print(a)

# 将缓冲区解释为一维数组
# numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
# buffer 类缓冲区对象
# dtype
# count 需要读取的数量，-1表示读取所有数据
# offset 需要读取的起始位置

s =  bytearray('Hello World',encoding='utf-8')
a = np.frombuffer(s, dtype = 'S1')  
print(a)

# 从可迭代对象构建一维数组
# numpy.fromiter(iterable, dtype, count = -1)
l = list(range(5))
print(l)
it = iter(l)
x = np.fromiter(it, dtype = float)
print(x)
