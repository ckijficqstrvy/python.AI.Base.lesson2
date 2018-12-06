# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:55:38 2018

@author: ckijf
"""

import json
import pickle

d = dict(name = 'Tracy', age = 19, score = 88)

with open('dump_ex.pickle', 'wb') as f:
    pickle.dump(d, f)

with open('data_ex.json', 'w') as j:
    json.dump(d, j)