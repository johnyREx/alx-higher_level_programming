#!/usr/bin/python3
"""
Class LockedClass
No class or object attributes
Prevents user from dynamically creating
new instance attributes except if the
new attribute is first_name
"""


class LockedClass:
    """Locked class"""
    __slots__ = ['first_name']
