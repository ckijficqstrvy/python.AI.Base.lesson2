# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:47:53 2018

@author: ckijf
"""

import pickle
d = dict(name = 'Bob', age = 20, score = 88)

#1
'''
fw = open('dump.pickle', 'wb')
pickle.dump(d, fw)
fw.close()
'''
#1.1
with open('dump.pickle', 'wb') as f:
    pickle.dump(d, f)

    