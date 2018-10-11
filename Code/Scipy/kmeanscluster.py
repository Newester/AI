#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from scipy.cluster.vq import kmeans,vq,whiten
from numpy import vstack,array
from numpy.random import rand

data = vstack((rand(100,3) + array([.5,.5,.5]),rand(100,3)))
print(data)

data = whiten(data)
print(data)
print('------------------')
centriods,_ = kmeans(data,3)
print(centriods)

clx,_ = vq(data,centriods)
print(clx)