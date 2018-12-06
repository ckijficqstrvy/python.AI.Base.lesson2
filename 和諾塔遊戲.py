# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:55:46 2018

@author: ckijf
"""

def hanoi(n, x, y, z):
    if n == 1:
        print(x, '-->', z)
    else:
        hanoi(n-1, x, z, y) #n-1個盤子移到Y上
        print(x, '-->', z) #將X最底下(最大)的盤子移到Z上
        hanoi(n-1, y, x, z) #將y上n-1的盤子移動到Z上
        
n = int(input('請輸入層數: '))
hanoi(n, 'X', 'Y', 'Z')