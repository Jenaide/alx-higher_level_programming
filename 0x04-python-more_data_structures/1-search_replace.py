#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    function that replaces all occurrences of an
    element by another in a new list.
    """
    return ([elememt if element != search else replace for element in my_list])
