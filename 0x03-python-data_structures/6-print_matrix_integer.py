#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            print("{}{:d}".format(("" if i == 0 else " "), row[i]), end='')
        print()
