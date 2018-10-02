# /usr/bin/env python3
# _*_ coding: utf-8 _*_

import numpy as np 

# 三角函数
a = np.array([0,30,45,60,90])
print(np.sin(a*np.pi/180))
print(np.cos(a*np.pi/180))
print(np.tan(a*np.pi/180))

sin = np.sin(a*np.pi/180)
cos = np.cos(a*np.pi/180)
tan = np.tan(a*np.pi/180)

inv = np.arcsin(sin)
print(inv/np.pi*180)

inv = np.arccos(cos)
print(inv/np.pi*180)

inv = np.arctan(tan)
print(inv/np.pi*180)

print(np.degrees(inv))

# numpy.around(a,decimals=0)
# 四舍五入
a = np.array([1.0,5.55,123,0.567,1.412])
print(np.around(a))
print(np.around(a,decimals=1))
print(np.around(a,decimals=-1))

# numpy.floor()
# nump.ceil()
a = np.array([-1.7,1.5,-0.2,0.6,10])
print(np.floor(a))
print(np.ceil(a))





