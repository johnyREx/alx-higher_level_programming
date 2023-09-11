#!/usr/bin/python3
"""
Class rectangle that inherits from
BaseGeometry
Private instance elements width and height
Public instance method area
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Private instance variables: width
                                    height"""
    def __init__(self, width, height):
        """Initializes class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def __str__(self):
        result = ""
        result += ("[Rectangle] " + str(self.__width))
        result += ("/" + str(self.__height))

        return result

    def __repr__(self):
        print("[Rectangle] " + str(self.__width), end="")
        print("/" + str(self.__height))

    def area(self):
        """Calculates rectangle area"""
        return self.__width * self.__height
