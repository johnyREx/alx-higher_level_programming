#!/usr/bin/python3
"""The ``matrix_divided`` module
This module contains a single function ``matrix_divided`` that
divides every number in a matrix by a base number
"""


def matrix_divided(matrix, div) -> list:
    """Divides all elements of a matrix.

    Args:
        matrix (list): A list of list of int or float
        div (int|float): Number to use in the division

    Returns:
        list: A new list as a result of the division
    """
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []

    for r in range(len(matrix)):
        if type(matrix[r]) is not list:
            raise TypeError('matrix must be a matrix (list of \
lists) of integers/floats')

        if r > 0 and len(matrix[r]) != len(matrix[r-1]):
            raise TypeError('Each row of the matrix must have the same size')

        new_matrix.append([])
        for n in matrix[r]:
            if type(n) not in [float, int]:
                raise TypeError('matrix must be a matrix (list \
of lists) of integers/floats')

            new_matrix[r].append(round(n/div, 2))
    return new_matrix
