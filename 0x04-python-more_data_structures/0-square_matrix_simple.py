#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    return [list(map(lambda x: x * x, row)) for row in matrix]
