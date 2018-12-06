# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 21:37:20 2018

@author: ckijf
"""

from functools import reduce
c = range(101)
sum_nums = reduce(lambda x, y: x + y, c)