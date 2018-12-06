# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 13:52:12 2018

@author: ckijf
"""

class Cat(object):
    def __init__(self, name, weight, hight):
        self.name = name
        self.weight = weight
        self.hight = hight
            
    def meow(self, meow_type):
        if meow_type==1:
            print(self.name, 'meow!')
        else:
            print(self.name, 'mooo!')
    
    def BMI(self):
        bmi = self.weight/self.hight**2
        if self.hight == 0:
            print('hight value is wrong')
        else:
            print("Cat's name is {0}.\n{0}'s BMI is {1:0.2f}.".format(self.name, bmi))