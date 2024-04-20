#!/usr/bin/python3

def even_odd(num):
    """function that checks if a number is even or odd"""
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")


userNumber = int(input("Which number do you want to check : "))

print(even_odd(userNumber))
