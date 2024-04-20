#!/usr/bin/python3

def userDetails(licenseNo, *args, phoneNo=0, **kwargs):
    print("license No :", licenseNo)
    j = ""
    for i in args:
        j += i
    print("Full Name :", j)
    print("Phone Number :", phoneNo)
    for key, val in kwargs.items():
        print("{} : {}".format(key, val))


name = ["Enock", " ", "Mbaraka"]
mydict = {"Name": "Enock", "ID": 33993899,
          "Age": 25, "Country": "Kenya",
          "Language": "English"}
userDetails("KPMG", *name, phoneNo="0727722840", **mydict)
