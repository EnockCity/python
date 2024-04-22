#!/usr/bin/python3

"""Returning a function from a function.
This function is returning the upper method of str from
the function return_to_upper. We called the function
and stored the reference to the returned function
in to_upper. Then used it to print
the upper case of "scaler topicstr.upper"""


def return_to_upper():
    return str.upper


to_upper = return_to_upper()

print(to_upper("scaler topics"))
