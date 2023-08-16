#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return None
    L = list(a_dictionary.items())
    for val in L:
        if val[1] == value:
            del a_dictionary[val[0]]
    return a_dictionary
