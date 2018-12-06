# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 15:48:03 2018

@author: ckijf
"""

import numpy as np
#np文件操作方式txt
part_data1 = np.loadtxt('data_table1.txt', skiprows=1)
print(part_data1)
print('------------')

#np文件操作方式CSV
part_data2 = np.loadtxt('data_table2.csv', skiprows=1, delimiter=',', usecols=(2, 4))
print(part_data2)