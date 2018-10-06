#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import numpy as np 
# numpy.load() numpy.save() numpy.loadtxt() numpy.savetxt()

a = np.array([1,2,3,4,5]) 
np.save('outfile',a) # 将输入数组存储在 .npy 文件中
b = np.load('outfile.npy')
print(b)
np.savetxt('out.txt',a)
b = np.loadtxt('out.txt')
print(b)


