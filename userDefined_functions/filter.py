#!/usr/bin/python3

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def odd(num):
    if num % 2 == 1:
        return True
    else:
        return False


# filter function filter mu_list and returns odd numbers
odd_num = list(filter(odd, my_list))
print(odd_num)
