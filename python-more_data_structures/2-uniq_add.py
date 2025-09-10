#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''
    Returns the sum of all unique integers in a list.
    '''
    uniq_integers = set(my_list)
    return sum(uniq_integers)
