#!/usr/bin/python3

result = (lambda **kwargs: sum(kwargs.values()))
print(result(a=10, b=20, c=30),
      result(a=10, b=20, c=30, d=40, e=50), sep="\n")
