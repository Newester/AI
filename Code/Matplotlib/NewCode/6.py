#!/usr/bin/env python3 
# _*_ coding: utf-8 _*_

import matplotlib.pyplot as plt

slices = [7,2,3,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%')
plt.title('Interesting Graph\nCheck it out')

plt.show()


