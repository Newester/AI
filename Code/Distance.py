#!/home/anaconda3/bin/python3
#_*_ coding: utf-8 _*_

#欧里几德距离 Euclidean Distance
#二维
from numpy import *
def twoPointDistance2D(a, b):
    d = sqrt( (a[0] - b[0])**2 + (a[1] - b[1])**2 )
    retrun d

#三维
def twoPointDistance3D(a, b):
    d = sqrt( (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2 )
    return d

# 多维
def twoPointDistanceND(a, b):
    squareSum = 0
    for i in range(len(a)):
        squareSum = squareSum + (a[i] - b[i])**2
    return sqrt(squareSum)

#标准化距离
def twoPointDistanceNormalize(a, b):
    squareSum = 0
    for i in range(len(a)):
        avg_i = (a[i] - b[i])/2
        s_i = sqrt( (a[i] - avg_i)**2 + (b[i] - avg_i)**2 )
        squareSum = squareSum + ((a[i] - b[i])/s_i)**2
    return sqrt(squareSum)
