#!/usr/bin/python3

from functools import reduce

doubles = [2, 6, 10, 14, 18]


def add(a, b):
    return a + b


sum_all = reduce(add, doubles)
print(sum_all)
