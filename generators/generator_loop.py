#!/usr/bin/python3

"""simple generator function to generate natural numbers
from 1 to 20"""


def mygen():
    for i in range(1, 20):
        yield i


# my_gen = mygen()

"""for i in my_gen:
    print(i)"""
num = list(mygen())
print(num)
