#!/usr/bin/python3

"""generator expression for generating even numbers"""

gen = (i for i in range(40) if i % 2 == 0)

for i in gen:
    print(i)
