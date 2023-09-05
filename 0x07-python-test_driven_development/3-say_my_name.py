#!/usr/bin/python3
"""The ``3-say_my_name`` module
This module contains a single function ``say_my_name``
"""


def say_my_name(first_name, last_name=""):
    """Prints the ``first_name`` and ``last_name``

    Args:
        first_name (str): The first name
        last_name (str, optional): The last name. Defaults to "".
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print('{} {}'.format(first_name, last_name))
