#!/usr/bin/python3
"""
Checks if object is an
instance of a class
"""


def is_same_class(obj, a_class):
    """ Uses type function """

    if type(obj) == a_class:
        return True
    else:
        return False
