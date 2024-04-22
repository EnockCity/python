#!/usr/bin/python3

"""Here, we have created the inner() function
inside the outer() function"""


def outer(x):
    def inner(y):
        return x + y
    return inner


add_five = outer(5)
result = add_five(6)
print(result)  # prints 11

# Output: 11
