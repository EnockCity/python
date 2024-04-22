#!/usr/bin/python3

import functools

"""Decorators with Arguments
The most inner function wrapper is taking a variable
number of arguments and then calling the decorated
function num_times times. It finally returns the
return value of the original decorated function.
One level above is the decorator_repeat function
which does the work of a normal decorator,
it returns the wrapper function.
On the outermost level is the repeat decorator
function that accepts an argument and provides it
to the inner functions using the closure pattern
Finally, we used the decorator with a parenthesis ()
unlike before to pass an argument.
"""


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
                return value

        return wrapper
    return decorator_repeat


@repeat(num_times=3)
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Kitty")
