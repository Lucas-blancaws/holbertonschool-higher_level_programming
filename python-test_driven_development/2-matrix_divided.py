#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains the function matrix_divided to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The divisor.

    Raises:
        TypeError: If matrix elements are not lists of ints/floats,
                   or if rows are not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        New matrix with elements divided by div, rounded to 2 decimals.
        """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == float('inf') or div == float('-inf'):
        return [[0.0 for _ in row] for row in matrix]
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )

    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
