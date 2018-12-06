# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 17:45:46 2018

@author: ckijf
"""

import pandas as pd
'''
#series
series_a = pd.Series([10, 5, 8])
print(series_a)
series_a.index = ['a', 'b', 'c']
print(series_a.index)
series_b = pd.Series([10, 5, 8], index= ['apple', 'banana', 'peach'])
print(series_a)
print(series_b)

series_c = pd.Series(3, index= ['apple', 'banana', 'peach'])

print(series_c)

d = {'apple':10, 'banana':5, 'peach':8}
series_d = pd.Series(d)
print(series_d)
'''
#DataFrame
data = [['apple', 5], ['banana', 49], ['peach', 40]]
df = pd.DataFrame(data, columns=['fruit', 'price'])
print(df)