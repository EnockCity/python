#!/usr/bin/python3

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_num = list(filter(lambda num: num % 2 == 1, my_list))
print(odd_num)
