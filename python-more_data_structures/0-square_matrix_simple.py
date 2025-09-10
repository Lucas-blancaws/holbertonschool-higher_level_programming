#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
    Returns a new matrix with the square of all values of the input matrix.
    '''
    new_matrix = []
    for row in matrix:
        new_row = []
        for x in row:
            new_row.append(x ** 2)
        new_matrix.append(new_row)
    return new_matrix
