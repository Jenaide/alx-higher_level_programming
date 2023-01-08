#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Gets an element in a list at given index
    and returns it
    """
    if idx < 0 or idx > len(my_list) - 1:
        return 'None'
    else:
        return my_list[idx]
