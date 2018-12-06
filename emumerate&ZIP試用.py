# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 22:32:01 2018

@author: ckijf
"""

#enumerate1
seasons = ['spring', 'sumer', 'autumn', 'winter']
for i, season in enumerate(seasons, 1): print(i, season)


#enumerate2
c = list(enumerate(seasons, 3))
print('\n', c,'\n')


#ZIP1
a = [1, 2, 3]
b = ['one', 'two', 'three']
c = ['A', 'B', 'C', 'D', 'E']
d = list(zip(a, b, c))
print(d)

#ZIP2
new_a, new_b, new_c = list(zip(*d))
print('\n',new_a, new_b, new_c)