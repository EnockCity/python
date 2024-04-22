#!/usr/bin/python3

def mygen():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n

    n += 1
    yield n

    n += 1
    yield n


my_gen = mygen()

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
