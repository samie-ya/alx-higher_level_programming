#!/usr/bin/python3
"""Defining matrix_divided"""


def matrix_divided(matrix, div):
    """ This function is used to divide each element
        in matrix with the given div.

        Args:
            matrix (list): the list of lists containing
            the numbers
            div (int): the number used for division
        Returns:
            New matrix containing the divided results
    """
    new_matrix = [[]]
    if not((type(div) is int) or (type(div) is float)):
        raise TypeError("div must be a number")
    elif (div == 0):
        raise ZeroDivisionError("division by zero")
    else:
        for i in range(len(matrix)):
            if (len(matrix[i - 1]) != len(matrix[i])):
                raise TypeError("Each row of the matrix\
 must have the same size")
            for j in matrix[i]:
                if not((type(j) is int) or (type(j) is float)):
                    raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
        new_matrix = [[round(j / div, 2) for j in matrix[i]]
                      for i in range(len(matrix))]
        return new_matrix
