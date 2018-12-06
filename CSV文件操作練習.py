# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:53:05 2018

@author: ckijf
"""

import csv
#1


heads = ['name', 'age', 'sex', 'price']
rows = [('Fack', 45, 'M', 3040.43), ('Mary', 18, 'F', 400000.34), 
        ('Jack', 20, 'MIX', 503830)]
'''
fo = open('data.csv', 'w', newline='')
fw = csv.writer(fo)
fw.writerow(heads)

#1.1
#for i in range(len(rows)):
#    fw.writerow(rows[i])

fw.writerows(rows)

fo.close()
'''

#2這種寫法優先，系統自動幫你關閉檔案

with open('data.csv', 'w', newline='') as f:   #newline=''讓創建的CSV檔沒有多餘的換行
    f_csv = csv.writer(f)
    f_csv.writerow(heads)
    f_csv.writerows(rows)
    