def print_list_integer(my_list=None):
    '''
    Function:
        print_list_integer(my_list=None): prints all integers of a list

    Parameters:
        my_list: list of integers (default: None)

    Returns:
        None
    '''
    if my_list is None:
        my_list = []
    for number in my_list:
        print("{:d}".format(number))
