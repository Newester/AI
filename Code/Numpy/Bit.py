#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# bitwise_and -- 对数组元素执行位与操作
# bitwise_or -- 对数组执行位或操作
# invert -- 计算位非
# left_shift -- 向左移动二进制表示的位
# right_shift -- 向右移动二进制表示的位

import numpy as np
a,b  = 13,17 
print(bin(a),bin(b))
print(np.bitwise_and(13,17))

print(np.bitwise_or(13,17))

print(np.invert(np.array([13],dtype=np.uint8)))
print(np.binary_repr(13,width=8))
print(np.binary_repr(242,width=8))

print(np.left_shift(10,2))
print(np.binary_repr(10,width=8))
print(np.binary_repr(40,width=8))

print(np.right_shift(40,2))
print(np.binary_repr(40,width=8))
print(np.binary_repr(10,width=8))

