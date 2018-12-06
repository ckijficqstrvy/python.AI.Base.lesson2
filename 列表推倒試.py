# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:40:30 2018

@author: ckijf
"""
#1
number_list = [i**3 for i in range(13)]
print(number_list)

#2
odd_list = [x for x in number_list if x%2 !=0]
print(odd_list)

#3
even_list = [y if y%2==0 else print(y, 'not even number') for y in number_list]
print(even_list)

#4
phrase = "Nothing is true. Everything is permitted"
words = phrase.split(" ")
print(words)
select_words_list = [[w.title(), len(w)] for w in words if len(w)>2]
#for w in select_words_list:
#   print(w)
    
#4.5
another_words_list = list(map(lambda w:[w.title(), len(w)], filter(lambda lw: len(lw)>2, words)))
for w in select_words_list:
   print(w)