#!/usr/bin/python3
def best_score(a_dictionary):
    x = -1
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > x:
                x = v
                y = k
        return y
    else:
        return None
