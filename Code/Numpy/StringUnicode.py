#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# 对 dtype 为 numpy.string_ 或者 numpy.unicode_ 类型的数组执行向量化字符串操作

import numpy as np 

# numpy.char.add()
# 按元素连接两个字符串
print(np.char.add(['hello'],[' xyz']))
print(np.char.add(['hello', 'hi'],[ ' abc',' xyz']))

# numpy.chr.multiply()
# 多重连接
print(np.char.multiply('Hello',3))

# numpy.char.center(arr,width,fillchar)
# 返回所需宽度的数组，以便字符串位于中心，并使用fillchar在左侧和右侧进行填充
print(np.char.center('hello',20,fillchar='*'))

# numpy.char.capitalize()
# 返回字符串的副本，其中第一个字母大写
print(np.char.capitalize('hello world'))

# numpy.char.title()
# 返回输入字符串的暗元素标题转换版本，其中每个单词的首字母都大写
print(np.char.title('hello how are you?'))

# numpy.char.lower()
# 元素全部转换为小写
print(np.char.lower(['HELLO','WORLD']))

# numpy.char.upper()
# 元素全部转换为大写
print(np.char.upper(['hello','world']))

# numpy.char.split()
# 返回字符串中的单词列表，默认分隔符为空格
print(np.char.split('hello how are you?'))
print(np.char.split('one,two,three,four,five',sep=','))

# numpy.char.splitlines()
print(np.char.splitlines('hello\nhow are you？\rI\'m fine,thanks,and you?'))

# numpy.char.strip()
# 移除元素开头结尾的特定字符
print(np.char.strip('ashok arora','a'))
print(np.char.strip(['arora','admin','java'],'a'))

# numpy.char.join()
# 单个字符由特定分隔符连接
print(np.char.join(':','dmy'))
print(np.char.join([':','-'],['dmy','ymd']))

# numpy.char.repalce()
print(np.char.replace('He is a good boy','is','was'))

# numpy.char.decode()
a = np.char.encode('hello','cp500')
print(a)
print(np.char.decode(a,'cp500'))


