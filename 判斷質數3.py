# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:54:31 2018

@author: ckijf
"""
#埃拉托斯特尼篩法
noprime = [j for i in range(2, 14) for j in range(i*2, 200, i)]
prime = [n for n in range(2, 200) if n not in noprime]
print(prime)