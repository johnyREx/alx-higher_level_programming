#!/usr/bin/python3
"""
Class square that inherits from Rectangle
Private instance size
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Private instance attribute size"""

    def __init__(self, size):
        """ Initializes class """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __repr__(self):
        """ Prints square """
        print("[Square] " + str(self.__size), end="")
        print("/" + str(self.__size))

    def __str__(self):
        result = ""
        result += ("[Square] " + str(self.__size))
        result += ("/" + str(self.__size))

        return result

    def area(self):
        return self.__size ** 2
