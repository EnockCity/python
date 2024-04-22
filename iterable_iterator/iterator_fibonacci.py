#!/usr/bin/python3

class myfibonacci:
    """This iterator produces fibonacci numbers"""
    def __init__(self):
        self.prev = 0
        self.cur = 0

    def __iter__(self):
        self.prev = 0
        self.cur = 1
        return self

    def __next__(self):
        if self.cur <= 50:
            val = self.cur
            self.cur += self.prev
            self.prev = val
            return val
        else:
            raise StopIteration


myfibo = myfibonacci()
iteration = iter(myfibo)
for i in iteration:
    print(i)
