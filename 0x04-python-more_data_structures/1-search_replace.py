#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for x in my_list:
        if x == search:
            pos = new.index(search)
            del(new[pos])
            new.insert(pos, replace)
    return new
