# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 15:06:40 2018

@author: ckijf
"""

import numpy as np

#np.array(裡面放的是list或tuple)
arr1 = np.array([[1, 2, 3],[4, 5, 6]])
arr2 = np.array([(1, 2, 3),(4, 5, 6)])


arr_e = np.zeros((2, 3))
print(arr_e)
print('-------')
arr_f = np.ones((3, 2))
print(arr_f)
print('-------')
arr_g = np.full((2, 3),8)
print(arr_g)
print('-------')
arr_h = np.empty((4,2))
print(arr_h)
print('-------')
arr_i = np.arange(0, 20, 2)
print(arr_i)
print('-------')
arr_j = np.linspace(2, 10, 6)
print(arr_j)
print('-------')

#2數據類型轉換
print(arr1.dtype)
print('-------')
print(arr1.astype(str))
print('-------')
print(np.float32(arr1))

