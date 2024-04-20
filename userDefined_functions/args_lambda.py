#!/usr/bin/python3

result = (lambda *args: sum(args))
print(result(10, 20), result(10, 20, 30, 40), sep="\n")
