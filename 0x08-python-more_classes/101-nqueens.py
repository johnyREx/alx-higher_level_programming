#!/usr/bin/python3
"""The ``101-nqueens`` module
This module contains a function that solves the ``N queens puzzle``

The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.

This implementation is a translation of Niklaus Wirth's solution, with
some modifications
"""


def n_queens(n, i, a, b, c):
    """Yields the possible solutions for an ``nxn`` board"""
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                yield from n_queens(n, i+1, a+[j], b+[i+j], c+[i-j])
    else:
        yield [[c[i] + a[i], a[i]] for i in range(len(a))]


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print('N must be a number')
        exit(1)

    if int(sys.argv[1]) < 4:
        print('N must be at least 4')
        exit(1)

    for solution in n_queens(int(sys.argv[1]), 0, [], [], []):
        print(solution)
