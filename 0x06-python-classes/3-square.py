#!/usr/bin/python3
"""This module contains a `square class`
"""


class Square:
    """The Square class
    """

    def __init__(self, size=0):
        """Initializes the class instance

        Args:
            size (int, optional): Size of the Square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size > 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self) -> int:
        """Computes the area of the Square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2


if __name__ == '__main__':
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))
