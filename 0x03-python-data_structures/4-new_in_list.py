#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    m_list = my_list
    if idx < 0 or idx >= len(my_list):
        return m_list
    else:
        m_list[idx] = element
        return m_list
