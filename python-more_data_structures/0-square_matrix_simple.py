#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.
    Returns a new matrix of the same size with squared values.
    """
    return [[x**2 for x in row] for row in matrix]
