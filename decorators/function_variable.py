#!/usr/bin/python3

"""Assigning a function to a variable
both foo and also_foo ppoints to the same
function object
"""


def foo():
    print("I am foo")


also_foo = foo

foo()

also_foo()
