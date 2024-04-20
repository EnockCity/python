#!/usr/bin/python3

def userDetails(**kwargs):
    #print(kwargs)
    for key, val in kwargs.items():
        print("{} : {}".format(key, val))


userDetails(Name="Enock", ID=33993899, Age=25, Country="Kenya")
