#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lista = []
    for v in range(0, list_length):
        try:
            div = my_list_1[v] / my_list_2[v]
        except (ZeroDivisionError):
            div = 0
            print("division by 0")
        except (ValueError, TypeError):
            div = 0
            print("wrong type")
        except (IndexError):
            div = 0
            print("out of range")
        finally:
            lista.append(div)
    return lista
