#!/usr/bin/python3

class myiter:
    """This iterator produces odd numbers"""
    def __init__(self):
        self.num = 0

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 20:
            val = self.num
            self.num += 2
            return val
        else:
            raise StopIteration


my_odd = myiter()
iteration = iter(my_odd)
for i in iteration:
    print(i)
