#!/usr/bin/python3
"""
Function to read a file
No permission
No file availability checks
"""


def read_file(filename=""):
    """
    Open file and print the contents
    Must use with
    """
    with open(filename) as file:
        read_data = file.read()
        print(read_data, end="")
