#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    '''
    Finds all multiples of 2 in a list.
    Returns a new list of True/False values of the same length.
    '''
    return [num % 2 == 0 for num in my_list]
