#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = list_length * [0]
    for v in range(0, list_length):
        try:
            result[v] = my_list_1[v] / my_list_2[v]
        except (ZeroDivisionError):
            print("division by 0")
        except (ValueError, TypeError):
            print("wrong type")
        except (IndexError):
            print("out of range")
    return result
