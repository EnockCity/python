#!/usr/bin/python3

"""In the example below, the calculate() function
takes a function as its argument. While calling calculate()
we are passing the add() function as the argument.
In the calculate() function, arguments: func, x, y
become add, 4, and 6 respectively."""


def add(x, y):
    return x + y


def calculate(func, x, y):
    return func(x, y)


result = calculate(add, 4, 6)
print(result)  # prints 10
