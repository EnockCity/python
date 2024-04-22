#!/usr/bin/python3

class myiter:

    """ This iterator produces natural numbers from 1-10 """
    def __init__(self):
        self.num = 0

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


my_num = myiter()
iterator = iter(my_num)
for i in iterator:
    print(i)
