# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 17:36:15 2018

@author: ckijf
"""

import numpy as np
arr1 = np.arange(9)
arr2 = np.reshape(arr1, (3, 3))
arr3 = arr2[:2, :2]
print(np.linalg.det(arr3))