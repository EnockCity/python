#!/usr/bin/python3

"""A function can be passed to any other function
just like a normal variable.
The do_twice function accepts a function and
calls it twice in its body.
We defined another function say_hello and passed
it to the do_twice function, thus getting Hello!
two times in the output.
"""


def do_twice(func):
    func()
    func()


def say_hello():
    print("Hello Enock!")


do_twice(say_hello)
