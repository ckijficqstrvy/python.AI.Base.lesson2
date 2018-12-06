# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 23:27:54 2018

@author: ckijf
"""

import numpy as np
arr = np.arange(0, 10)
print(arr[2])
print('-------------')
#創建arange的多維矩陣
arr_2d = np.arange(1, 21).reshape(4, 5)
print(arr_2d)
#切片
print('-------------')
print(arr_2d[2])
print('-------------')
print(arr_2d[2, 3])
print(arr_2d[2][3])
print('-------------')
print(arr_2d[1:3])
print('-------------')
print(arr_2d[1:])
print('-------------')
print(arr_2d[1: , 2:4])
print('-------------')
#倒置
print(arr_2d[1, ::-1])
print('-------------')
#倒置跳步
print(arr_2d[1, ::-2])
print('-------------')
#等同arr_2d[1]也等同arr_2d[1, :]
print(arr_2d[1, ...])
print('-------------')
#等同arr_2d[:, 1]
print(arr_2d[..., 1])

print('-------------')
#列表索引[[row1, row2, row3], [col1, col2, col3]]
arr_2d_index = arr_2d[[0, 2, 2], [0, 1, 0]]
print(arr_2d_index)

print('-------------')
#布爾索引
print(arr_2d[arr_2d > 13])
print(arr_2d > 13)

