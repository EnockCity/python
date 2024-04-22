#!/usr/bin/python3

"""A basic example of a Python decorator
In this example, simple_decorator is a decorator that
adds some behavior before and after the say_hello function
is called, without modifying the function itself
"""


def simple_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@simple_decorator
def say_hello():
    print("Hello!")


say_hello()
