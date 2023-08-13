#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    t = []
    for i in range(2):
        if len_a > i and len_b > i:
            t.append(tuple_a[i] + tuple_b[i])
        elif len_a > i and len_b <= i:
            t.append(tuple_a[i])
        elif len_a <= i and len_b > i:
            t.append(tuple_b[i])
        else:
            t.append(0)
    return (tuple(t))
