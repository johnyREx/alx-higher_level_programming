#!/usr/bin/python3
"""
Converts class to dict
within the class
"""


class Student:
    """
    Class Student
    No class attributes
    """
    def __init__(self, first_name, last_name, age):
        """
        3 instance attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Converts self to json
        """
        if attrs is not None:
            new_dict = {}
            for i in attrs:
                try:
                    new_dict[i] = self.__dict__[i]
                except Exception:
                    continue
            return new_dict
        else:
            return self.__dict__
