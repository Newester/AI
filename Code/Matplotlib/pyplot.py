#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# matplotlib.pyplot 一个命令风格的函数集合
# 在 matplotlib.pyplot 中，各种状态跨函数调用，绘图函数始终指向当前轴域

import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
# 向 plot() 命令提供单个列表或数组，则 matplotlib 假定它是一个 y 值序列，并自动生成 x 值（从 0 开始）
plt.plot([1,2,3,4],[1,4,9,16])
plt.show()

plt.plot([1,2,3,4],[1,4,9,16],'ro')
#指定坐标坐标轴的范围
plt.axis([0,6,0,20])
plt.show()

#使用 numpy 的数组作为数据输入
import numpy as np

t = np.arange(0.,5.,0.2)

plt.plot(t, t, 'r--',t, t**2, 'bs', t, t**3, 'g^')
plt.show()

# 控制线条属性
# 线条属性 <-- matplotlib.lines.Line2D --> linewidth dash style antialiased

x = [0,1,2,3]
y = [0,2,4,8]
x1 = [0,1,2,3]
x2 = [0,1,2,3]
y1 = [0,1,2,3]
y2 = [0,1,2,4]
#  使用关键自参数设置线条属性
plt.plot(x, y, linewidth=2.0)
#  使用 Line2D 实例的 setter 方法
line1, line2 = plt.plot(x1, y1, x2, y2)
line, = plt.plot(x, y, '-')
line.set_antialiased(False)
#  使用 setp() 命令
lines = plt.plot(x1, y1, x2, y2)
#    使用 python 关键字参数
plt.setp(lines, color='r', linewidth=2.0)
#    使用 MATLAB 风格字符串/值对
plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
plt.show()



