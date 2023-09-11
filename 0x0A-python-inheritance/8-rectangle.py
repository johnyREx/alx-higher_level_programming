#!/usr/bin/python3
"""
Class rectangle that inherits from
BaseGeometry
Private instance elements width and height
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
