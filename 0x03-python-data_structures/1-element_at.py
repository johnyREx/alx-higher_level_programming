#!/usr/bin/python3
def element_at(my_list, idx):
    a = len(my_list)
    # if idx >= 0 and idx < a:
    if idx in range(0, a):
        return (my_list[idx])
    else:
        return
