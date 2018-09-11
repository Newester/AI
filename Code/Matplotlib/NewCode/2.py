#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,6,7]
x2 = [1,2,3]
y2 = [10,12,14]

plt.plot(x,y,label='First Line')
plt.plot(x2,y2,label='Second Line')

plt.xlabel('Plot Number')
plt.ylabel('Important Var')
plt.title('Interesting Graph\nCheck it out')
plt.legend() #生成默认图例
plt.show()
