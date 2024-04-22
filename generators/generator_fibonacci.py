#!/usr/bin/python3

"""This function generates 10 numbers of fibonacci series"""


def myfibo():
    num1, num2 = 0, 1
    count = 0
    while count < 10:
        yield num1
        num1, num2 = num2, (num1 + num2)
        count += 1


# fibo = myfibo()

"""for i in fibo:
    print(i)"""

my_list = list(myfibo())
print(my_list)
