#!/usr/bin/python3

"""We created a class called Browser. The class contains
a getter and setter for the page attribute created with
the @property decorator.
It contains a class method called with_incognito which
acts as a factory method to create incognito window objects.
It also contains a static method to get the information
for the browser which will be the same for
all objects (windows)."""


class Browser:
    __NO_OF_WINDOWS = 0  # private member

    def __init__(self, page):
        self._page = page
        self.is_incognito = False

        Browser.__NO_OF_WINDOWS += 1

    @property
    def page(self):   # Getter
        return self._page

    @page.setter
    def page(self, new_page):
        if type(new_page) is not str:
            raise TypeError("Page must be a string")
        self._page = new_page

    @classmethod
    def with_incognito(cls, new_page):  # factory method for incognito window
        instance = cls(new_page)
        instance.is_incognito = True
        return instance

    @staticmethod
    def get_browser_info():
        return {
                "name": "Google Chrome",
                "version": "96.0.4664.110",
                "OS": "Windows"
                }
