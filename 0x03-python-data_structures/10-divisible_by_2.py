#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) > 0:
        multiple = []
        for i in my_list:
            multiple.append(True if i % 2 == 0 else False)
        return (multiple)
    return ([])
