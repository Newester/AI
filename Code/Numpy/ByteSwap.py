#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import numpy as np 

# numpy.ndarray.byteswap() -- 大端小端切换
a = np.array([1,256,8755], dtype= np.int16)
b = map(hex,a)
print(b)
print(a.byteswap(True))
b = map(hex,a)
print(b)
