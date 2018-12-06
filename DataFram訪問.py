# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 15:03:03 2018

@author: ckijf
"""

import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(10, size=(6, 4)),
                    index=['A', 'B', 'C', 'D', 'E', 'F'],
                    columns=['a', 'b', 'c', 'd'])
print(df)

# print(df.loc[['A','C'], ['b', 'd']])
# print(df.loc[:, 'a':'c'])
# print(df.loc['B':'E'])
# print(df.iloc[1:3, :3])

print(df['d']['B'])
print(df['a'])
print(df.a)