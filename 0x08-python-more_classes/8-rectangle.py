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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        return max(rect_1, rect_2, key=lambda rect: rect.area())


if __name__ == '__main__':
    my_rectangle_1 = Rectangle(8, 4)
    my_rectangle_2 = Rectangle(2, 3)

    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1,
                                                   my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")

    my_rectangle_2.width = 10
    my_rectangle_2.height = 5
    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1,
                                                   my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")
