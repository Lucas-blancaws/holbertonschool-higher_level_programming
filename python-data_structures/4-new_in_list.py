#!/usr/bin/python3
'''
Returns a copy of the list with element at idx replaced if valid
otherwise returns a copy of the original list.
'''


def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx < 0:
        return new_list
    if idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return new_list
