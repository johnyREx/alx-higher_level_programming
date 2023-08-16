#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if not a_dictionary:
        return None
    return {x: v * 2 for x, v in a_dictionary.items()}
