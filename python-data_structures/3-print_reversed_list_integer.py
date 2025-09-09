#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''
    Function:
        print_reversed_list_integer(my_list=[]): 
        prints all integers of a list in reverse order

    Parameters:
        my_list (list): list of integers

    Returns:
        None
    '''
    if my_list is None:
        return
    for number in reversed(my_list):
        print("{:d}".format(number))
