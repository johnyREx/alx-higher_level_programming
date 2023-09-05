#!/usr/bin/python3
"""The ``5-text_indentation`` module
"""


def text_indentation(text: str):
    """prints a text with 2 new lines after each of these
    characters: ., ? and :

    Args:
        text (str): The text to print
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    for c in text:
        if c == '.' or c == '?' or c == '!':
            print('\n\n', end="")
            continue
        print(c, end="")
