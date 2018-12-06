# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:53:03 2018

@author: ckijf
"""

import pickle

with open('dump.pickle', 'rb') as F:
    d = pickle.load(F)
    
print(d)