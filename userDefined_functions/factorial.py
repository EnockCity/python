#!/usr/bin/python3

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


number = int(input("What number do you want factorial for: "))

print(factorial(number))