#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import numpy as np 

a = np.array([[3,7,5],[8,4,3],[2,4,9]])
# numpy.amin() -- 最小
# numpy.amax() --最大
print(np.amin(a,1))
print(np.amin(a,0))
print(np.amax(a))
print(np.amax(a,axis=0))

#numpy.ptp() 沿轴方向的范围：最大值 - 最小值
print(np.ptp(a,axis=1))

# numpy.percentile(a,q,axis)
#小于这个值的观察值占的百分比
# a -- 输入数组
# q -- 要计算的百分位数，在0~100之间
# axis -- 沿着的轴
a = np.array([[30,40,70],[80,20,10],[50,90,60]])
print(np.percentile(a,50))
print(np.percentile(a,50,axis=1))

# numpy.median()
# 中值 -- 将样本上半部分与下半部分分开的值
print(np.median(a))
print(np.median(a,axis=1))

# numpy.mean() -- 算数平均值
print(np.mean(a))
print(np.mean(a,axis=1))

# numpy.average() -- 加权平均值
a = np.array([1,2,3,4])
wts = np.array([4,3,2,1])
print(np.average(a,weights=wts))
print(np.average([1,2,3,4],weights=wts,returned=True))

# numpy.std() -- 标准差
print(np.std(a))

# numpy.var() -- 方差
print(np.var([1,2,3,4]))
