#!/usr/bin/python3

"""Defining a function inside other functions.
Such functions are called inner functions
or nested functions.Below is a function
with two inner functions.Created two functions inside
the function parent and then called both of them
in the parent function body.
"""


def parent():
    print("I am the parent function")

    def first_child():
        print("I am the first child function")

    def second_child():
        print("I am the second child function")

    first_child()
    second_child()


parent()
