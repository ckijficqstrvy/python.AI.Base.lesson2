# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 16:43:54 2018

@author: ckijf
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6, 4),
                  index=['a', 'b', 'c', 'd', 'e', 'f'],
                  columns=['A', 'B', 'C', 'D'])
print(df)
df1 = df.drop(['a', 'e'])  #用索引名刪除
#print(df1)
df2 = df.drop(df.index[1:4])  #用索引位置刪除
#print(df2)
df3 = df.drop('B', axis=1)  #刪除列要用axis=1參數
#print(df3)
df4 = df[df.C < 0]  #找C列小於0的行
print(df4)


