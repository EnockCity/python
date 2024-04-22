#!/usr/bin/python3

"""The output and working are the same as the previous example
the only thing that changed is that we are using @decorator
instead of say_hello = decorator(say_hello)
We can easily decorate a function using the @decorator syntax
"""


def decorator(func):
    def wrapper():
        print("This is printed before the execution is called")
        func()
        print("The is printed after the function is called")

    return wrapper


@decorator
def say_hello():
    print("Hello! The function is executing")


say_hello()
