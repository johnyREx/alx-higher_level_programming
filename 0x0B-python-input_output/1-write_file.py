#!/usr/bin/python3
"""
This function writes a string
into a text
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file.

    Args:
        filename (str, optional):
        text (str, optional):

    Returns:
        int: The number of characters.
    """
    try:
        with open(filename, "W", encoding="utf-8") as file:
            num_characters_written = file.write(text)
        return num_characters_written
    except FileNotFoundError:
        with open(filename, "x", encoding="utf-8") as file:
            num_characters_written = file.write(text)
        return num_characters_written
    except Exception as e:
        return 0


if __name__ == "__main__":

    result = write_file("example.txt", "Hello, World!")
    print(f"Number of characters written: {result}")
