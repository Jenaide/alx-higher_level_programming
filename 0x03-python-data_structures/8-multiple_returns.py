#!/usr/bin/python3
def multiple_returns(sentence):
    """
    function that returns a tuple with the length of
    a string and its first character.
    """
    if len(sentence) == None:
        my_tup = 0, "None"
    else:
        my_tup = len(sentence), sentence[0]
    return my_tup
