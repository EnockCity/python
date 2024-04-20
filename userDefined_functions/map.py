#!/usr/bin/python3

odd_num = [1, 3, 5, 7, 9]


def twice(num):
    return num * 2


doubles = list(map(twice, odd_num))
print(doubles)
