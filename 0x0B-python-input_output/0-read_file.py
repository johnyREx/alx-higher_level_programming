#!/usr/bin/python3
"""
Function to read a file
No permission
No file availability checks
"""


def read_file(filename=""):
    """
    Read and print the contents of a text file

    Args:
        filename (str, optional):The name of file to read

    Returns:
        None
    """

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    read_file()
