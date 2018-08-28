#!/home/sepro/anaconda3/bin/python3
# _*_ coding: utf-8 _*_
from sklearn import svm
X = [[0, 0], [1, 1], [1, 0]]
y = [0, 1, 1]
clf = svm.SVC()
clf.fit(X,y)
result = clf.predict([[2, 2]])
print(result)

import matplotlib.pyplot as plt
labels='frogs','hogs','dogs','logs'
sizes = 15,20,45,10
colors = 'yellowgreen','gold','lightskyblue','lightcoral'
explode = 0, 0.1, 0, 0
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=50)
plt.axis('equal')
plt.show()