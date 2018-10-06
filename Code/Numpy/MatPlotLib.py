#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import numpy as np 
from matplotlib import pyplot as plt 

# 线性图
x = np.arange(1,11)
y = 2 * x + 5
plt.title('Matplotlib Demo')
plt.xlabel('x axis caption')
plt.ylabel('y axis caption')
plt.plot(x,y)
plt.show()

# 格式化字符串
# ’-‘ 实线；
# ’--‘ 短横线；
# ’-.‘ 点划线；
# ’：‘ 虚线；
# ’.‘ 点标记；
# ’,‘ 像素标记；
# ’o‘ 圆标记；
# ’v‘ 倒三角标记；
# ’^‘ 正三角标记；
# ’&lt;’ 左三角标记；
# ‘&gt;’ 右三角标记；
# ‘1’ 下箭头标记
# ‘2’ 上箭头标记
# ‘3’ 左箭头标记
# ‘4’ 右箭头标记
# ‘s’ 正方形标记
# ‘p’ 五边形标记
# ‘*’ 星形标记
# ‘h’ 六边形标记1
# ‘H’ 六边形标记2
# ‘+’ 加号标记
# ‘x’ X标记
# ‘D’ 菱形标记
# ‘d’ 窄菱形标记
# ‘&#124;’ 竖直线标记
# ‘_’ 水平线标记

# 颜色缩写
# 'b' blue
# 'g' green
# 'r' red
# 'c' 青色
# 'm' 品红色
# 'y' yellow
# 'k' black
# 'w' white

# 绿色圆来代表点
plt.plot(x,y,'og')
plt.show()

# 绘制正弦波
x = np.arange(0,3 * np.pi, 0.1)
y = np.sin(x)
plt.title('sine wave form')
plt.plot(x,y)
plt.show()

# subplot()

x = np.arange(0,3*np.pi,0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.subplot(2,1,1)
plt.title('Sine')
plt.plot(x,y_sin)

plt.subplot(2,1,2)
plt.title('Cosine')
plt.plot(x,y_cos)
plt.show()

# bar() -- 条形图
x = [5,8,10]
y = [12,16,6]
x2 = [6,9,11]
y2 = [6,15,7]
plt.bar(x,y,align='center')
plt.bar(x2,y2,color='g',align='center')
plt.title('Bar graph')
plt.xlabel('X aixs')
plt.ylabel('Y axis')
plt.show()

#  numpy.histogram() -- 数据的频率分布
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
np.histogram(a,bins=[0,20,40,60,80,100])
hist,bins = np.histogram(a,bins=[0,20,40,60,80,100])
print(hist)
print(bins)

# hist() -- 直方图
plt.hist(a,bins)
plt.title('histogram')
plt.show()

