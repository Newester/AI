#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import numpy as np 

# numpy.nditer -- numpy 的迭代器对象
a = np.arange(0,60,5)
a = a.reshape(3,4)
print(a)
for x in np.nditer(a):
    print(x)

#迭代的顺序只考虑内容布局，不考虑特定的顺序
b = a.T 
print(b)
for x in np.nditer(b):
    print(x)

# C 风格
c = b.copy(order='C')
print(c)
for x in np.nditer(c):
    print(x)

# F 风格
d = b.copy(order='F')
print(d)
for x in np.nditer(d):
    print(x)

# 显式指定 nditer 的排序风格
for x in np.nditer(a, order='C'):
    print(x)
for x in np.nditer(a, order='F'):
    print(x)

# op_flags 指定读写模式 -- read(默认) write readwrite
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2 * x
print(a)

# flags 指定索引输出规则 -- c_index f_index multi_index external_loop
for x in np.nditer(a, flags=['external_loop'],order='F'):
    print(x)

# 广播迭代
b = np.array([1,2,3,4], dtype=int)
for x,y in np.nditer([a,b]):
    print("(%d,%d)" % (x,y))
