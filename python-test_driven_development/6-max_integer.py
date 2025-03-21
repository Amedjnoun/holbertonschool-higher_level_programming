#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if list is None:
        raise TypeError("list must be a list of integers")
    if len(list) == 0:
        return None
    max_int = list[0]
    for i in list:
        if i > max_int:
            max_int = i
    return max_int
