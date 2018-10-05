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

#用于执行算术运算 add() subtract() multiply() divide() 的输入数组必须具有相同的形状或者符合广播规则
a = np.arange(9,dtype=np.float_).reshape(3,3)
b = np.array([10,10,10])
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))

# numpy.recoprocal()
# 求倒数，参数绝对值 >1，返回0；参数 =0，报警告
b = np.array([100], dtype= int)
print(np.reciprocal(b))

# numpy.power()
# 求幂
a = np.array([10,100,1000])
b = np.array([1,2,3]) 
print(np.power(a,b))

# numpy.mod()
# numpy.remainder()
# 返回输入数组中相应元素的除法余数
a = np.array([10,20,30])
b = np.array([3,5,7])
print(np.mod(a,b))
print(np.remainder(a,b))


# 复数操作
# nunmpy.real() -- 返回实部
# numpy.imag() -- 返回虚部
# numpy.conj() -- 返回共轭复数
# numpy.angle(arr,deg=False) -- 返回复数参数的角度, deg = True 角度制，否则弧度制
a = np.array([-5.6j, 0.2j, 11., 1+1j])
print(np.real(a))
print(np.imag(a))
print(np.conj(a))
print(np.angle(a))
print(np.angle(a,deg=True))