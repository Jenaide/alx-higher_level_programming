#!/usr/bin/python3
def number_keys(a_dictionary):
    """
    function that returns the number of
    keys in a dictionary.
    """
    num = 0
    keys = list(a_dictionary)

    for i in keys:
        num = num + 1
    return num
