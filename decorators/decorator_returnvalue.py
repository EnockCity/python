#!/usr/bin/python3

import functools

"""Returning Values from Decorated Functions
We are calling the func twice in the wrapper function.
But this time, we made sure to return the value of the
second call back to the caller
The wrapper function should return the return value
of the decorated function, otherwise, it would be lost
"""


def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


@do_twice
def add(num1, num2):
    print(f"Adding {num1} and {num2}")
    return num1 + num2


print("The sum is:", add(1, 2))
