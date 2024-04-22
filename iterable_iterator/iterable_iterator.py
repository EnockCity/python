#!/usr/bin/python3

my_list = ["Enock", "Joseph", "Paul", "Benjamin", "Rose", "Elijah"]

# create an iterator object using iter()
iterator = iter(my_list)
# return first element in the iterator stream
print(next(iterator))
# return next element in the iterator stream
print(next(iterator))

print(iterator.__next__()) #return the first element in the iterator
print(iterator.__next__()) #return next element in the iterator
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
