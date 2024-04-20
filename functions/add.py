#!/usr/bin/python3

def add(*args):
    result = 0
    numbers = input("Enter 3 numbers separated by space: ").split()
    numbers = [int(num) for num in numbers]
    for num in numbers:
        result += num
    return result


if__name__ == "__main__":
    print(add())
