#!/usr/bin/python3
"""The ``0-rectangle`` module
Module that implements a Rectangle class
"""


class Rectangle:
    """A rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """The class constructor

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Returns the area of the rectangle
        ``width * height``
        """
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle
        2(width + height)
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns the string rep of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([f'{self.print_symbol}' *
                          self.width for _ in range(self.height)])

    def __repr__(self):
        """Returns the machine rep of the object in string"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Called when an instance is deleted"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1


if __name__ == '__main__':
    my_rectangle_1 = Rectangle(8, 4)
    print(my_rectangle_1)
    print("--")
    my_rectangle_1.print_symbol = "&"
    print(my_rectangle_1)
    print("--")

    my_rectangle_2 = Rectangle(2, 1)
    print(my_rectangle_2)
    print("--")
    Rectangle.print_symbol = "C"
    print(my_rectangle_2)
    print("--")

    my_rectangle_3 = Rectangle(7, 3)
    print(my_rectangle_3)

    print("--")

    my_rectangle_3.print_symbol = ["C", "is", "fun!"]
    print(my_rectangle_3)

    print("--")
