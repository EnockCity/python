#!/usr/bin/python3

from functools import reduce

doubles = [2, 6, 10, 14, 18]

sum_all = reduce(lambda a, b: a + b, doubles)
print(sum_all)
