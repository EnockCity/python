#!/usr/bin/python3

import functools
"""do_twice is a simple decorator that calls
the decorated function two times"""


def do_twice(func):
    @functools.wraps(func)
    def wrapper():
        func()
        func()

    return wrapper
