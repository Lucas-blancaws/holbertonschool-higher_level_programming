#!/usr/bin/python3
def no_c(my_string):
    '''
    Function:
        no_c(my_string): returns new string with 'c' and 'C' characters remove

    Parameters:
        my_string (str): the original string

    Returns:
        str: the new string without 'c' and 'C'
    '''
    return "".join([ch for ch in my_string if ch != 'c' and ch != 'C'])
