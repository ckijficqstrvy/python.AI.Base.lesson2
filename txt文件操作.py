# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:20:12 2018

@author: ckijf
"""

with open('data.txt', 'a+') as f:
    f.write('\njust do your best in this test.')
    pos = f.seek(2, 0)
    string = f.read(35)
    print(string)



