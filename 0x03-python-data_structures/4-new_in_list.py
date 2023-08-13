#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list[:]
    if idx in range(0, len(copy)):
        copy[idx] = element
    return (copy)
