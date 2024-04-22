#!/usr/bin/python3

"""decorator: This is a decorator function,
it accepts another function as an argument and
"decorates it" which means that it modifies it in some
way and returns the modified version.
Inside the decorator function, we are defining another
inner function called wrapper. This is the actual function
that does the modification by wrapping the passed function func.
decorator returns the wrapper function.
say_hello: This is an ordinary function that we need to decorate.
Here, all it does is print a simple statement."""


def decorator(func):
    def wrapper():
        print("This is printed before the function is called")
        func()
        print("This is printed after the function is called")

    return wrapper


def say_hello():
    print("Hello! The function is executing")


say_hello = decorator(say_hello)


say_hello()
