#!/usr/bin/python3
"""
This module contains a function that adds two integers
"""


def add_integer(a, b) -> int:
    """Adds two numbers

    Args:
        a (int|float): The first number
        b (int|float): The second number

    Returns:
        int: The result of the sum
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')

    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    return int(a) + int(b)
