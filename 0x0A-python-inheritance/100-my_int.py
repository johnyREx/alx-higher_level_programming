#!/usr/bin/python3
"""
A rebel class called MyInt
"""


class MyInt(int):
    """MyInt is a subclass of int"""
    def __eq__(self, other):
        return int(str(self)) != other

    def __ne__(self, other):
        return int(str(self)) == other
