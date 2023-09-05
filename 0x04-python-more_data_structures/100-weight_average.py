#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total = 0
    num = 0
    for val in my_list:
        total += (val[1] * val[0])
        num += val[1]

    return total / num
