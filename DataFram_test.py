# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 14:44:40 2018

@author: ckijf
"""

import pandas as pd
data = [['apple', 10], ['banana', 8], ['peach', 5]]
df = pd.DataFrame(data, columns=[furit', 'number'])
df.to_csv('DataFram_test.csv')
print('ok')