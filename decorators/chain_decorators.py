#!/usr/bin/python3

import functools

"""Chaining Decorators.Chaining the decorators means
that we can apply multiple decorators to a single function.
These are also called nesting decorator
The first one takes a function that returns a string and
then splits it into a list of words.
The second one takes a function that returns a string and
converts it into uppercase.
we will use both the decorators on a single function
by stacking them asshown below
"""


def split_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).split()

    return wrapper


def to_upper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper


@split_string
@to_upper
def say_hello(name):
    return f"Hello, {name}!"


print(say_hello("Kitty"))
