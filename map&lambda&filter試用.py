# -*- coding: utf-8 -*-

def double_number1(x):return x * 2
numbers = [1, 2, 3, 4]
double_numbers = list(map(double_number1, numbers))  #map函數僅反為跌代器，所以前加list轉換為列表輸出

map_list = list(map(lambda x, y: x * y, [1, 2, 3, 4], [2, 4, 6, 8]))



numbers = range(100)
is_odd = list(filter(lambda x: (x % 2 !=0)&(x < 67), numbers))


