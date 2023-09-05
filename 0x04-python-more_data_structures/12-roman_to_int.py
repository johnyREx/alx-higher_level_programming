#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    if roman_string == '':
        return 0

    rmn = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    prev = 0

    for i in roman_string:
        if i not in rmn:
            return 0
        if rmn[i] > prev:
            num = num + rmn[i] - (2 * prev)
        else:
            num = num + rmn[i]

        prev = rmn[i]
    return num
