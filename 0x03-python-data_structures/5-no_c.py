#!/usr/bin/python3
def no_c(my_string):
    my_list = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            my_list += i
    return my_list
