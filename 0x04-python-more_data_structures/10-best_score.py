#!/usr/bin/python3
def best_score(a_dictionary):
    """
    function that returns a key with the biggest
    integer value.
    """
    max_value = 0
    win = None
    if type(a_dictionary) is dict:
        for key, value in a_dictionary.items():
            if value > max_value:
                max_value = value
                win = key
    return win
