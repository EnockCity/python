#!/usr/bin/python3

import functools

"""Classes as Decorators in Python
Classes can also be used as decorators by implementing
the __call__ method and passing the function to __init__
as an argument
we use functools.update_wrapper instead of functools.wraps
in case of a class as a decorator
After decoration, the __call__ method of the class
is called instead of the say_hello method.
"""


class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print("Hello!")


say_hello()
say_hello()
