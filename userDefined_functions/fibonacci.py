#!/usr/bin/python3

def fibonacci(num):
    """function that finds fibonacci of a number"""
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


nums = int(input("How many fibonacci do you want to generate: "))

for num in range(nums):
    print(fibonacci(num))
