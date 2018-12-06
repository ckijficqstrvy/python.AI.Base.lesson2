# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 23:18:27 2018

@author: ckijf
"""

#1 test
from functools import reduce
def convert_string(string):
    map_string = list(map(int, string))
    return reduce(lambda x, y: x*10 + y, map_string)
    
print(convert_string("65535"))

#2 test

a = [1, 2, 3, 4]
b = ['apple', 'banana', 'cherry']

for i, tup in enumerate(zip(a,b)):
    print(i, tup)
    
#3 test

line = "Love all, trust a few, do wrong to none."
new_line = line.lower()
new_line = new_line.replace(',', '')
new_line = new_line.replace('.', '')
fin_line = new_line.split(' ')
print(fin_line)

