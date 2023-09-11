#!/usr/bin/python3
"""
Checks if object is a subclass of class
"""


def inherits_from(obj, a_class):
    """ Uses issubclass function """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
