#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Ndarray N 维数组
# 创建 ndarray numpy.array
# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# object 类 array 对象； dtype 数组所需的数据类型； copy 对象是否被复制； order C 行；F 列；A 任意，默认
# subok 默认返回基类数组，为 True 返回子类数组

import numpy as np

a = np.array([1,2,3])
print(a)

a = np.array([[1,2],[3,4]])
print(a)

# 最小维度 ndmin
a = np.array([1,2,3,4,5], ndmin = 2)
print(a)

# dtype 元素类型
a = np.array([1,2,3], dtype=complex)
print(a)

# ndarray 对象由计算机内存中的一维连续区域组成，带有将每个元素映射到内存块中某个位置的索引方案
# 内存块以按行（C风格）或按列（FORTRAN 或 MatKab 风格）的方式保存元素




