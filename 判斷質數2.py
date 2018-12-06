# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

count = 1
print('2 is prime number')
is_prime = True
for n in range(3, 31):
    if n % 2 == 0:
        continue
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime == True:
        print('{} is prime number'.format(n))
        try:
            count += 1
            if count == 6:
                break
        except:
            print('error')
    else:
        is_prime = True
