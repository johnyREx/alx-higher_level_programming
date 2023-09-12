#!/usr/bin/python3
"""
Prints Pascal's triangle
for a number n
"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal's triangle of n"""
    if n <= 0:
        return []

    triangle = []
    prev = []  # holds value of previous row in triangle
    for i in range(n):
        if i == 0:  # first row
            triangle.append([1])
        elif i == 1:  # second row
            triangle.append([1, 1])
            prev = [1, 1]
        else:
            new = [1]  # new refers to new row added to triangle
            for i in range(len(prev) - 1):
                new.append(prev[i] + prev[i+1])
            new.append(1)  # set last element to be 1
            triangle.append(new)  # add row to triangle
            prev = new

    return triangle
