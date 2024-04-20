#!/usr/bin/python3

from functools import reduce

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum_all = reduce(lambda a, b: a + b, list(map(lambda num: num * 2,
                 list(filter(lambda num: num % 2 == 1, my_list)))))

print(sum_all)
