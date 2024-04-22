#!/usr/bin/python3

""" Return a Function as a Value
In the example below, the return hello statement
returns the inner hello() function.
This function is now assigned to the greet variable.
That's why, when we call greet() as a function
we get the output"""


def greetings(name):
    def hello():
        return "Hello, " + name + "!"
    return hello


greet = greetings("Atlantis")
print(greet())  # prints "Hello, Atlantis!"

# Output: Hello, Atlantis!
