#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    '''
    Function:
        replace_in_list(my_list, idx, element): replaces an element in a list

    Parameters:
        my_list (list): the list of elements
        idx (int): index of the element to replace
        element: the new value to insert
    Returns:
        list:
            - The modified list if idx is valid
    '''
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return (my_list)
