#!/usr/bin/python3

"""The function in the code below is a generator
that successively yield integers from 1 to 5"""


def generator(num):
    for x in range(1, num + 1):
        yield x
    return


it = generator(5)
while True:
    try:
        print(next(it))
    except StopIteration:
        break
