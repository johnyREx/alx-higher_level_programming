#!/usr/bin/python3
"""This module contains a `square class`
"""


class Square:
    """The Square class
    """

    def __init__(self, size=0):
        """Initializes the square instance

        Args:
            size (int, optional): Size of the Square. Defaults to 0.
        """
        self.size = size

    def area(self) -> int:
        """Computes the area of the Square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    @property
    def size(self) -> int:
        """The `size` getter

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """The `size` setter

        Args:
            size (int): The size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size > 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size


if __name__ == '__main__':
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
