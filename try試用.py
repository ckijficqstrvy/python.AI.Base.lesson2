# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 16:36:31 2018

@author: ckijf
"""
profiles = {}
attributes = [('name', str), ('age', int), ('height',float)]

for attr_name, attr_type in attributes:
    valid_value = None
    while valid_value is None:
        try:
            value = input('Pelease enter you %s: ' % attr_name)
            valid_value = attr_type(value)
        except ValueError:
            print("Cannot convert %s'%s' to type %s.\n" "Please try again."%(attr_name, value, attr_type.__name__))
        else:
            print('We have got your %s.\n' % attr_name)
    profiles[attr_name] = valid_value