#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# bool_ 一个字节的bool
# int_ 默认整数，相当于 Ｃ 语言的 long ，通常为 int32 int64
# intc 相当于 C 的 int ，通常为 int32 或 int64
# intp 用于索引的整数，相当于 C 的 size_t ，通常为 int32 或者 int64
# int8 字节（-128~127）
# int16 16位整数 int32 32位整数 int64 64位整数
# uint8 8位无符号整数 uint16 16位无符号整数 uint32 32位无符号整数 uint64 64位无符号整数
# float_ float64 简写
# float16 半精度浮点数：符号位，5位指数，10位尾数
# float32 单精度浮点数：符号位，8位指数，23位尾数
# float64 双精度浮点数：符号位，11位指数，52位尾数
# complex_ complex128 的简写
# complex64 复数，两个32位浮点数表示实部和虚部
# complex128 复数，两个64位浮点数表示实部和虚部

# 数据类型对象 dtype
# 数据类型对象 --> 对应于数组的固定内存块的解释
# 数据类型
# 数据大小
# 字节序 <前缀：小端 >前缀：大端
# 字段的名称、数据类型、内存块偏移地址和大小
# 子序列数据类型的形状和元素数据类型

# 构造dtype numpy.dtype(object, align, copy)
# object 被转换为数据类型的对象； align 是否像 C 语言结构体一样字节对齐； copy 是否值拷贝

import numpy as np

dt = np.dtype(np.int32)
print(dt)



# int8 <--> 'i1' int16 <--> 'i2' int32 <--> 'i4' int64 <--> 'i8'
dt = np.dtype('i8')
print(dt)

#使用端记号（字节序标记）
dt = np.dtype('>i4')
print(dt)

# 结构化数据类型的使用

dt = np.dtype([('age',np.int8)])
print(dt)

a = np.array([(10,),(20,),(30,)], dtype=dt)
print(a)
print(a['age'])

# 自定义结构化类型
student = np.dtype([('name','S20'),('age','i1'),('marks','f4')])
print(student)
a = np.array([('abc',21,50),('xyz',18,75)],dtype=student)
print(a)

# 内建类型的字符代码
# 'b' 布尔值；'i' 符号数；'u' 无符号整数；'f' 浮点数；'c' 复数浮点；'m' 时间间隔；'M' 日期时间；'O' python对象；'S','a' 字节串；'U' Unicode；'V' void
