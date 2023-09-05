#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    a_dict = list(a_dictionary.items())
    max_int = a_dict[0][1]
    max_key = a_dict[0][0]
    for i in a_dict:
        if i[1] > max_int:
            max_int = i[1]
            max_key = i[0]
    return max_key
    # a_dict = [(i[1], i[0]) for i in a_dict]
    # a_dict.sort()
    # return a_dict[-1][1]
