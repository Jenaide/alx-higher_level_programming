#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    function that prints a dictionary
    by ordered keys.
    """
    order = list(a_dictionary.keys())
    order.sort()
    for i in order:
        print("{}: {}".format(i, a_dictionary.get(i)))    
