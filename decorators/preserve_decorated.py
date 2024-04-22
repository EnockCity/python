#!/usr/bin/python3

import functools

"""Preserving the Original Name and Docstring
of the Decorated Function
In Python, functions have a name attribute and
a docstring to help with debugging and documentation.
But, when we decorate a function its identity is
changed to the wrapper function
As the say_hello now points to the wrapper function
it is showing its information instead of the original function.
To fix this, we need to use another decorator
called wraps on the wrapper function.
The wraps decorator is imported from the
in-built functools modules.
Use the functools.wraps decorator to
preserve the original name and docstring
of the decorated function
"""


def decorator(func):
    @functools.wraps(func)
    def wrapper():
        print("This is printed before the function is called")
        func()
        print("This is printed after the function is called")

    return wrapper


@decorator
def say_hello():
    """This function says hello when called"""
    print("Hello! The function is executing")


print(say_hello.__name__)
help(say_hello)
