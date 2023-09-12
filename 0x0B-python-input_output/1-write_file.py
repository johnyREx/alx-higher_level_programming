#!/usr/bin/python3
"""
Opens and writes into
a file
"""


def write_file(filename="", text=""):
    """
    Open and write file
    Must use with
    """
    with open(filename, 'w+') as file:
        return(file.write(text))
