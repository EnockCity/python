#!/usr/bin/python3

from decorators import do_twice

"""This function reuses the do_twice decorator
any number of times by importing it from decorators.py
We imported and used the do_twice decorator on
both the functions and called them. Therefore,
we will get two outputs for each function.
"""


@do_twice
def say_hello():
    print("Hello!")


@do_twice
def say_bye():
    print("Bye!")


say_hello()
say_bye()
