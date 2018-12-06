# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 21:05:24 2018

@author: ckijf
"""
def reverse_string(x):
    string_len = len(x)
    after_string ='' 
    for i in range(string_len-1, -1, -1):
        after_string += x[i]
    return after_string