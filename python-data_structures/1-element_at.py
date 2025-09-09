def element_at(my_list, idx):
    '''
    Function:
        element_at(my_list, idx): retrieves an element from a list

    Parameters:
        my_list (list): list of elements
        idx (int): index of the element to retrieve

    Returns:
        - The element at position idx if it exists
        - None if idx is negative or out of range
        '''

    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    return my_list[idx]
