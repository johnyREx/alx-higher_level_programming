#!/usr/bin/python3
"""The ``0-rectangle`` module
Module that implements a Rectangle class
"""


class Rectangle:
    """A rectangle class"""
    def __init__(self, width=0, height=0):
        """The class constructor

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """The getter for the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """The setter for the width

        Args:
            width (int): The width

        Raises:
            TypeError: If width is not an integer
            ValueError: If width < 0
        """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        """The getter for the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """The setter for the height

        Args:
            height (int): The height

        Raises:
            TypeError: If height is not an integer
            ValueError: If height < 0
        """
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height


if __name__ == '__main__':
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
