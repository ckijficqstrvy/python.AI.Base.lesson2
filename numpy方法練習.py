# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 16:12:50 2018

@author: ckijf
"""

import numpy as np
#1
arr1 = np.arange(9).reshape(3, 3)

arr2 = np.array([[5, 6, 7],
                 [2, 4, -5],
                 [5, 6, 3]])

print(np.concatenate((arr1, arr2), axis = 1))


#2
print(np.vstack((arr1, arr2)))
print(np.hstack((arr1, arr2)))