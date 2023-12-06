#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    del(new[search - 1])
    new.insert(search - 1, replace)
    return new
