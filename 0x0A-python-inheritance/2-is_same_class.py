#!/usr/bin/python
"""
A function that returns True if the object 
is exactly an instance of the specified class ; 
otherwise False.
"""
def is_same_class(obj, a_class):
    """
    Checks if two objects are the same class.
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a type")
    return (type(obj) is a_class)
