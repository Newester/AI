#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from __future__ import print_function
import torch
x = torch.Tensor(5,3)
print(x)
print(x.size())

y = torch.rand(5,3)
print(x + y)

print(torch.add(x,y))

result = torch.Tensor(5,3)
torch.add(x,y,out=result)
print(result)

# 就地操作
y.add_(x)
print(y)
# 任何改变张量的操作方法都是以_结尾的
print(x[:, 1])

# 改变张量的大小 torch.view()

x = torch.randn(4,4)
y = x.view(16)
z = x.view(-1,8)
print(x.size(),y.size(),z.size())
