#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

#一次积分
import scipy.integrate
from numpy import exp
f = lambda x: exp(-x**2)
i = scipy.integrate.quad(f,0,1)
print(i)

#二次积分
from math import sqrt
f = lambda x,y: 16*x*y
g = lambda x: 0
h = lambda y : sqrt(1-4*y**2)
i = scipy.integrate.dblquad(f,0,0.5,g,h)
print(i)



