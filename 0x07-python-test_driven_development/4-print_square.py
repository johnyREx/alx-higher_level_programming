#!/usr/bin/python3
"""The `4-print_square`` module
"""


def print_square(size: int):
    """prints a square with the character #.

    Args:
        size (int): length of the square
    """
    if type(size) not in [float, int] or type(size) is float and size < 0:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    size = int(size)
    for r in range(size):
        print('#' * size)
