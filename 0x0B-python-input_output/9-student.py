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

    def to_json(self):
        """
        Converts self to json
        """
        return(self.__dict__)
