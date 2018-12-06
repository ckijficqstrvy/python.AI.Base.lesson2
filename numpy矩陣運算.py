# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 16:27:29 2018

@author: ckijf
"""

import numpy as np
A = np.array([(1, 2), (-1, -2)])
print(A)
print('---------------')
#轉置
print(A.transpose())
print('---------------')
#求行列式的值
print(np.linalg.det(A))
#求矩陣相加
B = np.array([(1, 2, 3), (4, 5, 6)])
C = np.array([(1, 3, 5), (2, 4, 6)])
print('---------------')
print(B + C)


print(A * 3)
print(A / 2)

#計算dot內積
D = np.array([(1, 3, 5), (2, 4, 6), (1, 2, 3)])
print(np.dot(B, D))

#創單位矩陣，任何矩陣與單位矩陣dot還是本身
arr_i = np.identity(3, dtype=int)
print(arr_i)
print(np.dot(arr_i, D))

#逆矩陣(反矩陣)
E = np.array([(4, 2, 1), (4, 8, 3), (1, 1, 0)])
print(np.linalg.inv(E))