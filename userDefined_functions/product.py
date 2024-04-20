#!/usr/bin/python3

def product(nums):
    """function to find product of numbers"""
    total = 1
    for num in nums:
        total *= num
    return total


result = (lambda **kwargs: product(kwargs.values()))
print(result(a=10, b=20, c=30),
      result(a=10, b=20, c=30, d=40, e=50), sep="\n")
