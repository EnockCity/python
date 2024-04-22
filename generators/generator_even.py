#!/usr/bin/python3

def mygen():
    for i in range(1, 20):
        if i % 2 == 0:
            yield i


my_gen = mygen()

for i in my_gen:
    print(i)
