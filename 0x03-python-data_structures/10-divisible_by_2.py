#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    i = 0
    new = []
    while i < len(my_list):
        if my_list[i] % 2 == 1:
            new.append(0)
        else:
            new.append(1)
        i += 1
    return new
