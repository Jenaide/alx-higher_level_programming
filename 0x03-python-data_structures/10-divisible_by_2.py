#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    a function that finds all multiple
    of 2 in a list.
    """
    return [x for x in my_list if x % 2 == 0]
