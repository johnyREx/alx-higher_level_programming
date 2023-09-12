#!/usr/bin/python3
"""
Append to file
"""


def append_write(filename="", text=""):
    """
    open file and append test
    """
    with open(filename, 'a+') as file:
        return(file.write(text))
