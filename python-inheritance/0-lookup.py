#!/usr/bin/python3
def lookup(obj):
    """
    lookup Returns the list of available attributes and methods of an object

    args:
        obj: object to be inspected

    returns:
        lookup_list: list of available attributes and methods of an object
    """
    lookup = dir(obj)
    return lookup
