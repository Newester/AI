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

# numpy.arange(start, stop, step, dtype)
# start 范围的起始值
# stop 范围的终止值
# step 两个值的间隔，默认 1
# dtype 返回 ndarray 的数据类型，如果没有提供，默认为输入数据的类型

x = np.arange(5)
print(x)

x = np.arange(5, dtype = float)
print(x)

x = np.arange(10,20,2)
print(x)


# numpy.linspace(start, stop, num, endpoint, retstep, dtype)
# start 序列的起始值
# stop 序列的终止值，如果 endpoint 为 True ，则该值被包含在序列中
# num 要生成的等间隔样例数量，默认为 50
# endpoint 序列中是否包含 stop ，默认 True
# retstep 如果为 True ，返回样例，以及连续数字之间的步长
# dtype 输出 ndarray 的数据类型

x = np.linspace(10,20,5)
print(x)

x = np.linspace(10,20,5,endpoint = False)
print(x)

x = np.linspace(1,2,5,retstep= True)
print(x)

# numpy.logspace(start, stop, num, endpoint, base, dtype)
# start 起始值 （ base 的 start 次幂）
# stop 终止值 （ base 的 stop 次幂）
# num 范围内的数值数量，默认50
# endpoint 如果为 True ，终止值包含在输出数组中
# base 对数空间的底数，默认 10
# dtype 输出数组的数据类型，如果没有提供，则取决于其他参数

a = np.logspace(1.0, 2.0, num = 10)
print(a)

a = np.logspace(1, 10, num = 10, base = 2, dtype = int)
print(a)




