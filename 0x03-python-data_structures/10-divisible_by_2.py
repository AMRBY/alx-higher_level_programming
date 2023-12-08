#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    i = 0
    new = []
    while i < len(my_list):
        if (my_list[i] % 2) == 1:
            new.append('')
        else:
            new.append('True')
        i += 1
    return new
