#!/usr/bin/python3

import functools

"""Decorators Functions with Parameters
*args and **kwargs allow us to pass multiple
arguments or keyword arguments to a function.
Thus, we passed "Enock" as name to say_hello
which was received by the wrapper function and
the wrapper function used it
to call the actual func function.
Outputting Hello, Enock! twice.
"""


def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@do_twice
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Enock")
